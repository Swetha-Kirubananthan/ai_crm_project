from pydantic import BaseModel

class ProfileInput(BaseModel):
    company_name: str
    product: str
    region: str

class MatchOutput(BaseModel):
    company_name: str
    match_score: float
    matched_with: str