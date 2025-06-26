import os
import logging
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Pinecone with proper error handling
load_dotenv()
api_key = os.getenv('PINECONE_API_KEY')
if not api_key:
    logger.error("Pinecone API key not found in environment variables")
    raise ValueError("PINECONE_API_KEY environment variable is required")

pc = Pinecone(api_key=api_key)
index_name = os.getenv('PINECONE_INDEX', 'epilepsy-chatbot')
region = os.getenv('PINECONE_REGION', 'us-east-1')

try:
    # Load model with proper error handling
    model_name = os.getenv('EMBEDDING_MODEL', 'all-mpnet-base-v2')
    model = SentenceTransformer(model_name)
    dimension = model.get_sentence_embedding_dimension()
    logger.info(f"Loaded embedding model '{model_name}' with dimension: {dimension}")
except Exception as e:
    logger.error(f"Failed to load embedding model: {str(e)}")
    raise

# Check if the index exists, if not create it
try:
    if index_name not in pc.list_indexes().names():
        logger.info(f"Creating new Pinecone index: {index_name}")
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric='cosine',  # Changed from euclidean to cosine which is better for semantic search
            spec=ServerlessSpec(
                cloud='aws',
                region=region
            )
        )
        logger.info(f"Successfully created index: {index_name}")
    else:
        logger.info(f"Index {index_name} already exists")
    
    # Connect to the index
    index = pc.Index(index_name)
    logger.info(f"Successfully connected to index: {index_name}")
except Exception as e:
    logger.error(f"Error with Pinecone operations: {str(e)}")
    raise

# Process each file in the chunks directory
for fname in os.listdir('data/chunks'):
    with open(os.path.join('data/chunks', fname), encoding='utf-8') as f:
        text = f.read()
    embedding = model.encode(text).tolist()
    index.upsert([(fname, embedding, {'source': fname})])
