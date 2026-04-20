from flask import Flask,request
from vector_store import VectorStore,intialize_Vdb
from embedding import Embedding
import retrieval
import generate_result
app = Flask(__name__)   

# initialise the vector db(for first time only to store the doucments)
"""
store_vector=vector_store.intialize_vdb()
"""
@app.route('/')
def hello():
    vdb=VectorStore()
    emb=Embedding()
    ret=retrieval.Retriever(vdb,emb)
    query="what are ml models in aws"
    context=ret.retrieve_similar(query)
    output=generate_result.generate_llm(query,context)
    print(f"Generated Result:{output}")
    return output


if __name__=="__main__":
    app.run(debug=True, use_reloader=False)