
# AWS Document RAG Search

A Retrieval-Augmented Generation (RAG) project built using Flask, ChromaDB, Sentence Transformers, and OpenAI.

This application allows users to ask questions related to AWS documents / whitepapers and generates answers using semantic search + LLM response generation.

---
## Project Summary

AWS Document RAG Search is an AI-powered question-answering system that uses Retrieval-Augmented Generation (RAG) to answer questions from AWS PDF documents and whitepapers.

The system converts documents into embeddings, stores them in a vector database, retrieves relevant content using similarity search, and uses an LLM to generate accurate responses.

---
## Tech Stack

- Python
- Flask
- ChromaDB
- Sentence Transformers
- LangChain
- OpenAI API
- PyMuPDF

---

## Project Architecture

```text
PDF Files
   ↓
Load Documents
   ↓
Chunk Text
   ↓
Create Embeddings
   ↓
Store in ChromaDB
   ↓
-------------------
User Query
   ↓
Embedding
   ↓
Similarity Search
   ↓
Top Matching Chunks
   ↓
LLM Generation
   ↓
Answer
```
---
## Folder Structure
```
project/
│── app.py 
│── doc_load.py  #load and chunk the pdfs
│── embedding.py  #convert chunks to vector
│── vector_store.py  # store the vector in database
│── retrieval.py  #fetch the similar content
│── generate_result.py #generate the result 
│── .env #store the api key
│── requirements.txt 
│── data/
│   └── documents/  # sourse PDFs
│   └── vectordb/      # Created locally after initialization
```
## Vector Database Setup

The `data/vectordb/` folder is created locally when you run the initialization step.

It stores ChromaDB vector embeddings generated from the PDF documents and is excluded from GitHub.

## Create .env 
Store your api key:
```
OPENAI_API_KEY=your_key_here
```

## Run Vector DB Initialization
Uncomment  and Run the flask app 
```
store_vector=intialiseVdb()
```
## Run the Application
In Bash
```
flask run
```
Visit:
```
http://127.0.0.1:5000/
```
---

## Example
Query
```
what are ml models in aws?
```
Result
```
  - ML models in AWS can be built, trained, and deployed for any use case.
  - Amazon SageMaker AI and Amazon Bedrock provide access to open-source foundational models on AWS.
  - AWS offers specialized infrastructure for ML frameworks, providing greater flexibility and control over machine learning workflows.
  - Purpose-built AWS AI services, like speech, vision, and document analysis, are available for various business problems.
  - Amazon SageMaker AI offers fully managed infrastructure for building and training custom models.
  - AWS provides a range of advanced ML frameworks and infrastructure options for highly customized and specialized ML models.
```
---
## Future Improvement
* Web UI
* Chat Interface
* AWS Deployment
* User Upload PDFs
---




