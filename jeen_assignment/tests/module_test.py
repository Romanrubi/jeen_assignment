from src.loader import load_document
from src.splitter import chunk_strategies
from src.store import create_vector_store


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path   = os.path.join(BASE_DIR,  'spongebob_and_patricks_story.pdf')


docs = load_document(data_path)
chunks = chunk_strategies(docs)
vector_store = create_vector_store(
    chunks,
    persist_directory="vector_store"
)
