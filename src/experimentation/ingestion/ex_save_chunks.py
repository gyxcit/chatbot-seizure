import os
import json
import mlflow
from dotenv import load_dotenv
from ..save_artefact import save_artifact

# Charger .env pour la cohérence
load_dotenv()

# Config basique
CHUNKS_DIR = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'chunks')
ARTIFACT_PATH = os.path.join(os.path.dirname(__file__), '..','results','indexing','chunk_list.json')

# Lister les fichiers
files = sorted(os.listdir(CHUNKS_DIR))
print(f"Found {len(files)} chunks.")

# Start MLflow run
mlflow.set_experiment("Epilepsy-Indexing")
with mlflow.start_run(run_name="Save Chunks Artifact"):
    # Paramètres loggés
    mlflow.log_param("chunks_dir", CHUNKS_DIR)
    mlflow.log_param("num_chunks", len(files))

    # Sauvegarde et log de l'artefact
    save_artifact(files, ARTIFACT_PATH, artifact_name="chunk_list")
