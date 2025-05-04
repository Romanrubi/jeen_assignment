### Creating Vector Store

def create_vector_store(chunks, persist_directory):
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_community.vectorstores import Chroma
    from sentence_transformers import SentenceTransformer

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
    )
    vector_store = Chroma.from_documents(chunks, embeddings, persist_directory=persist_directory)
    print("Vector Store created and filled with embeddings !")
    return vector_store