import os
import yaml
import json
import logging
from tqdm import tqdm
import mlflow
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

config_path = os.path.join(os.path.dirname(__file__), '..', 'configs', 'indexing_config.yaml')
chunks_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'chunks')
# Load env
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load config
with open(config_path) as f:
    config = yaml.safe_load(f)

EMBEDDING_MODEL = config.get("embedding_model_cur", "all-mpnet-base-v2")
INDEX_NAME = config.get("index_name_cur", "epilepsy-chatbot")
METRIC = config.get("metric_cur", "cosine")
REGION = config.get("region_cur", "us-east-1")

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
if not PINECONE_API_KEY:
    raise ValueError("Missing PINECONE_API_KEY in .env")

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
model = SentenceTransformer(EMBEDDING_MODEL)
dimension = model.get_sentence_embedding_dimension()

# Start MLflow experiment
mlflow.set_experiment("Epilepsy-Indexing")
with mlflow.start_run(run_name="Indexing"):

    # Log parameters
    mlflow.log_param("embedding_model", EMBEDDING_MODEL)
    mlflow.log_param("index_name", INDEX_NAME)
    mlflow.log_param("metric", METRIC)
    mlflow.log_param("region", REGION)
    mlflow.log_param("embedding_dim", dimension)

    # Create index if not exists
    if INDEX_NAME not in pc.list_indexes().names():
        logger.info(f"Creating index {INDEX_NAME}")
        pc.create_index(
            name=INDEX_NAME,
            dimension=dimension,
            metric=METRIC,
            spec=ServerlessSpec(cloud="aws", region=REGION)
        )
        logger.info("Index created.")
    else:
        logger.info(f"Index {INDEX_NAME} already exists.")

    # Connect to the index
    index = pc.Index(INDEX_NAME)

    # Process and index all chunks
    files = os.listdir(chunks_dir)
    mlflow.log_param("num_chunks", len(files))

    for fname in tqdm(files, desc="Indexing chunks"):
        with open(os.path.join(chunks_dir, fname), encoding="utf-8") as f:
            text = f.read()
        embedding = model.encode(text).tolist()
        index.upsert([(fname, embedding, {"source": fname})])

    logger.info("Indexing complete.")
    mlflow.log_metric("indexing_done", 1)
