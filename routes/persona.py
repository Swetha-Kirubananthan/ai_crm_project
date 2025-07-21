from fastapi import APIRouter, HTTPException
from schemas.persona_schema import PersonaInput, PersonaOutput
from db import persona_collection
from datetime import datetime
from typing import List

router = APIRouter()


@router.post("/generate_persona", response_model=PersonaOutput)
def generate_persona(data: PersonaInput):
    # Dummy persona logic
    persona = {
        "product": data.product,
        "region": data.region,
        "target_industry": "general",  # dummy value
        "created_at": datetime.utcnow()
    }
    inserted_id = persona_collection.insert_one(persona).inserted_id

    return {
        "product": persona["product"],
        "region": persona["region"],
        "target_industry": persona["target_industry"]
    }


@router.get("/latest_persona", response_model=PersonaOutput)
def get_latest_persona():
    latest_persona = persona_collection.find_one(sort=[("created_at", -1)])
    if not latest_persona:
        raise HTTPException(status_code=404, detail="No persona found")

    return {
        "product": latest_persona["product"],
        "region": latest_persona["region"],
        "target_industry": latest_persona["target_industry"]
    }


@router.get("/all_personas", response_model=List[PersonaOutput])
def get_all_personas():
    personas = persona_collection.find().sort("created_at", -1)
    result = []

    for p in personas:
        result.append({
            "product": p["product"],
            "region": p["region"],
            "target_industry": p["target_industry"]
        })

    return result