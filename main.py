from fastapi import FastAPI
from routes import persona, match

app = FastAPI()

app.include_router(persona.router)
app.include_router(match.router)