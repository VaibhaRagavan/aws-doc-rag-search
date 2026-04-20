### Emedding the chuncked documnent
from sentence_transformers import SentenceTransformer
import numpy as np
from typing  import List


class Embedding:
    def __init__(self,model_name:str ="all-MiniLM-L6-v2"):
        self.model_name=model_name
        self.model=None
        self.device="cpu"
        self._load_model()
        print(f"embedding model loaded{model_name}")
    
    def _load_model(self):
        try:
            self.model=SentenceTransformer(self.model_name,device="cpu")
            print("Model loaded successfully")
        except Exception as e:
            print(f"Error loading model: {e}")
    
    def create_embedding(self,texts:List[str])->np.ndarray:
        if not self.model:
            raise ValueError("Model not loaded. Call _load_model first.")
        try:
            embedding=self.model.encode(texts,show_progress_bar=True,convert_to_numpy=True,device="cpu")
            print(f"Created embedding for {len(texts)} texts")
            print(f"embedding shape{embedding.shape}")
        except Exception as e:
            print(f"Error creating embedding: {e}")
        return embedding
