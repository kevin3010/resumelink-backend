from pinecone import Pinecone
from .config import settings

class Embeddings:
    def __init__(self):
        self.pinecone = Pinecone(api_key=settings.PINECONE_API_KEY)

    async def generate_embeddings(self, texts):
        embeddings = self.pinecone.inference.embed(
            "multilingual-e5-large",
            inputs = texts,
            parameters={"input_type": "passage"}
        )
        
        return embeddings
    
embedding_store = Embeddings()