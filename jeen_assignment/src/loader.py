### Document Loading

def load_document(file):
    import os
    name, extensions = os.path.splitext(file)
    if extensions == '.pdf':
        from langchain.document_loaders import PyPDFLoader
        print(f'Loading {file}')
        loader = PyPDFLoader(file)
    elif extensions == '.docx':
        from langchain.document_loaders import Docx2txtLoader
        print(f'Loading {file}')
        loader = Docx2txtLoader(file)
    else:
        print("/n/nDocument format is not supported!/n/n")
        return None
    data = loader.load()
    print(f"Document {name} loaded successfully !")
    return data