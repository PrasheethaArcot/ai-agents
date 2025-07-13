import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class SemanticSearchEngine:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.documents = []
        self.document_embeddings = None
    
    def add_documents(self, documents):
        self.documents.extend(documents)
        new_embeddings = self.model.encode(documents)
        if self.document_embeddings is None:
            self.document_embeddings = new_embeddings
        else:
            self.document_embeddings = np.vstack([self.document_embeddings, new_embeddings])
    
    def search(self, query, top_k=3):
        if not self.documents:
            return []
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.document_embeddings)[0]
        top_indices = np.argsort(similarities)[::-1][:top_k]
        results = []
        for idx in top_indices:
            results.append({
                'document': self.documents[idx],
                'similarity': similarities[idx],
                'index': idx
            })
        return results