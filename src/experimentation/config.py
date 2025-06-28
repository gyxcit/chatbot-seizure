experiment_configs = [
    {
        "name": "exp_0",
        "embedding_model": "all-mpnet-base-v2",
        "chunk_size": 256,
        "top_k": 3,
        "index_name": "index_mpnet_256"
    },
    
    {
        "name": "exp_1",
        "embedding_model": "multi-qa-mpnet-base-dot-v1",
        "chunk_size": 512,
        "top_k": 10,
        "index_name": "index_multiqa_512"
    }
]

# Global paths
RAW_TEXT_PATH = "../../data/raw_documents/"
CHUNKS_OUTPUT_PATH = "../../data/chunks/"
CSV_QUESTIONS_FILE = "../../data/csv/validation_auto_qg.csv"