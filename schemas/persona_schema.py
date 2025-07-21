from pydantic import BaseModel

class PersonaInput(BaseModel):
    website_url: str
    product: str
    region: str

class PersonaOutput(BaseModel):
    product: str
    region: str
    target_industry: str