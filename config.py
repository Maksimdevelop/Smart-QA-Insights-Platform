from pydantic import BaseModel

class Config(BaseModel):
    key: str
    llm_model: str