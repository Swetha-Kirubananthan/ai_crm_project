from fastapi import APIRouter, HTTPException
from schemas.match_schema import ProfileInput, MatchOutput
from db import persona_collection, profile_collection, match_collection
from rapidfuzz import fuzz
from datetime import datetime
from bson import ObjectId
from typing import List

router = APIRouter()


@router.post("/match_profile", response_model=MatchOutput)
def match_profile(data: ProfileInput):
    # Get the latest persona from MongoDB
    persona = persona_collection.find_one(sort=[("created_at", -1)])
    if not persona:
        raise HTTPException(status_code=404, detail="No persona found")

    # Calculate similarity scores using RapidFuzz
    score_product = fuzz.token_sort_ratio(data.product, persona["product"])
    score_region = fuzz.token_sort_ratio(data.region, persona["region"])
    score_industry = fuzz.token_sort_ratio("general", persona["target_industry"])  # dummy logic

    final_score = round((score_product * 0.5 + score_region * 0.3 + score_industry * 0.2), 2)

    # Save profile to DB
    profile_doc = {
        "company_name": data.company_name,
        "product": data.product,
        "region": data.region,
        "created_at": datetime.utcnow()
    }
    profile_id = profile_collection.insert_one(profile_doc).inserted_id

    # Save match result to DB
    match_doc = {
        "profile_id": profile_id,
        "matched_with_persona_id": str(persona["_id"]),
        "match_score": final_score,
        "timestamp": datetime.utcnow()
    }
    match_collection.insert_one(match_doc)

    return {
        "company_name": data.company_name,
        "match_score": final_score,
        "matched_with": str(persona["_id"])
    }


@router.get("/all_matches", response_model=List[MatchOutput])
def get_all_matches():
    results = []
    matches = match_collection.find().sort("timestamp", -1)

    for match in matches:
        profile = profile_collection.find_one({"_id": ObjectId(match["profile_id"])})
        if profile:
            results.append({
                "company_name": profile["company_name"],
                "match_score": match["match_score"],
                "matched_with": match["matched_with_persona_id"]
            })

    return results