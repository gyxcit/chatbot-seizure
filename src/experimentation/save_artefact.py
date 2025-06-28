import os
import json
import mlflow

def save_artifact(data, path, artifact_name=None):
    """
    Sauvegarde des données sous forme de JSON et log dans MLflow.
    
    :param data: objet Python sérialisable en JSON
    :param path: chemin local pour sauvegarder le fichier (relatif ou absolu)
    :param artifact_name: nom personnalisé pour l'artefact MLflow
    """
    # Crée le dossier si nécessaire
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # Écrit le fichier local
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    
    print(f"[INFO] Sauvegardé localement : {path}")

    # Log MLflow
    mlflow.log_artifact(path, artifact_path=artifact_name)
    print(f"[INFO] Loggé dans MLflow sous : {artifact_name or path}")