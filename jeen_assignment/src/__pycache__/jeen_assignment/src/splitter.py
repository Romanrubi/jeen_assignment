### Chunking Strategies

def chunk_strategies(data, chunk_size=256, overlap=10):
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["\n\n", "."]
    )
    chunks = text_splitter.split_documents(data)
    print("Document splitted succesfully")
    return chunks