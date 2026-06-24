from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Disaster Response AI API")

class SOSMessage(BaseModel):
    text: str
    latitude: float
    longitude: float

@app.post("/api/v1/analyze-sos")
async def analyze_sos(message: SOSMessage):
    # Placeholder for NLP detection logic
    keywords = ["help", "flood", "fire", "earthquake", "trapped"]
    urgency = "HIGH" if any(k in message.text.lower() for k in keywords) else "LOW"
    
    return {
        "status": "processed",
        "urgency_level": urgency,
        "coordinates": {"lat": message.latitude, "lng": message.longitude},
        "dispatch_recommended": urgency == "HIGH"
    }

@app.get("/health")
async def health_check():
    return {"status": "operational", "systems": ["nlp_engine", "geo_router"]}
