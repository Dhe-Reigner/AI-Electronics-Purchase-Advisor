from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def get_retriever():
    embeddings = HuggingFaceEmbeddings(
        model_name = 'sentence-transformers/all-MiniLM-L6-v2'
    )

    db = FAISS.load_local('electronics_index',embeddings)

    return db.as_retriever(search_kwargs={'k':5})