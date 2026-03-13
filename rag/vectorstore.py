from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import CSVLoader

def build_vectorstore():
    loader1 = CSVLoader('datasets/camera.csv')
    loader2 = CSVLoader('datasets/laptop.csv')
    loader3 = CSVLoader('datasets/phone.csv')

    docs = loader1.load() + loader2.load() + loader3.load()

    embeddings = HuggingFaceEmbeddings(
        model_name = 'sentence-transformers/all-MiniLM-L6-v2'
    )

    vectorestore = FAISS.from_documents(docs, embeddings)

    vectorestore.save_local('electronics_index')