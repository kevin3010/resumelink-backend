from pinecone import Pinecone
from .config import settings

class VectorStore:
    def __init__(self):
        self.pinecone = Pinecone(api_key=settings.PINECONE_API_KEY)

    async def upsert_job_embeddings(self, job_vectors):
        index = self.pinecone.Index(settings.PINECONE_INDEX_NAME_JOBS)
        return index.upsert(vectors=job_vectors, namespace='ns1')

    async def upsert_resume_embeddings(self, resume_vectors):
        index = self.pinecone.Index(settings.PINECONE_INDEX_NAME_RESUMES)
        return index.upsert(vectors=resume_vectors, namespace='ns1')

    async def query_jobs(self, resume_embedding , top_k=20):
        
        index = self.pinecone.Index(settings.PINECONE_INDEX_NAME_JOBS)
        return index.query(vector=resume_embedding, top_k=top_k, include_metadata=True, include_values=False, namespace='ns1')
    
vector_store = VectorStore()
    