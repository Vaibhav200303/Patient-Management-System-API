from fastapi import FastAPI

from app.db import engine
from app.db_models import Base
from app.routers import patients





# Initialize FastAPI application
app = FastAPI(
    title="Patient Management System API",
    description="A REST API for creating, retrieving, updating, deleting, and sorting patient records.",
    version="1.0.0"
)


# Register application routers
app.include_router(patients.router)


# Health check endpoint
@app.get("/", tags=["Health"])
def read_root():
    return {
        "message": "Patient Management System API is running"
    }


# API information endpoint
@app.get("/about", tags=["Health"])
def read_about():
    return {
        "title": "Patient Management System API",
        "version": "1.0.0",
        "description": "A REST API for managing patient records."
    }