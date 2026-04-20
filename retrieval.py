## Retreive the data from vector db
from typing import List,Dict
from vector_store import VectorStore
from embedding import Embedding


class Retriever:
    def __init__(self,vectordb=VectorStore,embedding=Embedding):
        self.vectordb=vectordb
        self.embedding=embedding
        print("installing retriever")
    
    def retrieve_similar(self,query:str,top_k=5,score_treshold:float=0.2):
        emb=Embedding()
        query_embedding=emb.create_embedding([query])#change query to vectors

        results=self.vectordb.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k,
        )
        recevied_result=[]
        try:
            if results["documents"] and results["documents"][0]:
                documents=results["documents"][0]
                metadatas=results["metadatas"][0]
                ids=results["ids"][0]
                scores=results["distances"][0]

                for doc,meta,id,score in zip(documents, metadatas,ids,scores):
                
                    similarity_score=1-score # convert distance to similarity score
                    if similarity_score>=score_treshold:
                        recevied_result.append({
                        "document":doc,
                        "metadata":meta,
                        "id":id,
                        "distance":score
                    })
                    print(f"Retrieved document: {doc[:100]}...")# Print first 100 characters"
                    print(f"Similarity Score: {similarity_score}")
        except Exception as e:
            print(f"Error retrieving similar documents: {e}")

        return recevied_result

      



        