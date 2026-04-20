###Store the vectors in the vector database 
import chromadb
import doc_load,embedding
import os, uuid,numpy as np
from typing import List


class VectorStore:
    """Create a vector store using ChromaDB"""
    def __init__(self,
                 collection_name:str="awsdoc_vectordb"
                 ,persist_directory:str="../data/vectordb"):
        self.collection_name=collection_name
        self.persist_directory=persist_directory
        self.client=None
        self.collection=None
        self._load_store()
        print("calling vector store")

    def _load_store(self):
        os.makedirs(self.persist_directory,exist_ok=True)
        self.client=chromadb.PersistentClient(path=self.persist_directory)
        self.collection=self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"description": "Aws documents in vector format"}    
        )
        print("Vector store created successfully")
        print(f"No of vectors created{self.collection.count()}")
    
    def add_vectors(self,chunks:List[any],embedding:np.ndarray):
        if len(chunks) != len(embedding):
            raise ValueError("Number of chunks must match number of embeddings")
        batch_size=400
        for start  in range(0,len(chunks),batch_size):
            end=start+batch_size

            chunk_batch=chunks[start:end]
            embed_batch=embedding[start:end]
            print(f"Adding batch {start//batch_size + 1}: {len(chunk_batch)} chunks")
            ids=[]
            metadatas=[]
            documents=[]
            embedding_list=[]
            try:
                for i,(chunk,embed) in enumerate(zip(chunk_batch,embed_batch)):
                    doc_id=f"doc_{i}_{uuid.uuid4()}"#generate id 
           
                    metadata=dict(chunk.metadata)#get the metadata and add extra data
                    metadata["len"]=len(chunk.page_content)
                    metadata["doc_id"]=i
                    document_text=chunk.page_content# getting the txt content
                    embeddinglist=embed.tolist()# convert numpy array to list
            
                    ids.append(doc_id)
                    metadatas.append(metadata)
                    documents.append(document_text)
                    embedding_list.append(embeddinglist)

                self.collection.add(
                    ids=ids,
                    embeddings=embedding_list,
                    metadatas=metadatas,
                    documents=documents)
                
                print(f"Added {len(ids)} vectors to the collection")
                print("Vectors stored successfully")

            except Exception as e:
                print(f"Error adding vectors: {e}")


def intialize_Vdb():
    """Initialise the vector database"""
    docs=doc_load.load_docs('../data/documents')
    chunks=doc_load.chunk(docs)
    texts=[chunks[i].page_content for i in range(len(chunks))]
    emb=embedding.Embedding()
    embedded_text=emb.create_embedding(texts)
    vdb=VectorStore()
    vectors=vdb.add_vectors(chunks,embedded_text)
    print(vectors)
