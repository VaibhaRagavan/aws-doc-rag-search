###Load the documents in document structure and chunck the documents
from langchain_community.document_loaders import PyMuPDFLoader,DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


#load the documents
def load_docs(directory):
    try:
        print("Loading documents from directory:",directory)
        files=DirectoryLoader(directory,glob="**/*.pdf",loader_cls=PyMuPDFLoader)
        docs=files.load()
        print(f"Loaded {len(docs)} documents")
    
    except Exception as e:
        print(f"Error loading documents: {e}")
    return docs

#chunk the documents
def chunk(docs,chunk_size=500,chunk_overlap=50):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n","\n"," ",""])
        
    print("Splitting documents into chunks...")
    chunks=text_splitter.split_documents(docs)
    print(f"Split into {len(chunks)} chunks")
   
    return chunks




