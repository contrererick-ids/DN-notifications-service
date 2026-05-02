import os
from fastapi import FastAPI
from app.routes import notificaciones
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Notifications Service")

app.include_router(notificaciones.router)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "notifications-service",
        "environment": os.getenv("ENVIRONMENT", "local"),
    }
