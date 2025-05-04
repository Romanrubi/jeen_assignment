from src.loader import load_document
from src.splitter import chunk_strategies
from src.store import create_vector_store


docs = load_document(r"C:\Users\Admin\Downloads\SpongeBob and Patrick's Krabby Patty Adventure.pdf")

chunks = chunk_strategies(docs)

vector_store = create_vector_store(
    chunks,
    persist_directory="vector_store"
)
