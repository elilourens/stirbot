import chromadb

def get_client(db_path="./chroma_db"):
    return chromadb.PersistentClient(path=db_path)
