from pydantic import BaseModel

class Token(BaseModel):
    id_token: str