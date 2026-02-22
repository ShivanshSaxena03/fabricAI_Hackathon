from typing import Optional

from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from db import Base, engine, get_db
from models import Fabric

from outfit_service import generate_outfit
from chat_service import chat_with_ai
from sql_service import generate_sql, execute_safe_query
from outfit_service import generate_outfit
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# INVENTORY
# -------------------------

@app.get("/inventory")
def get_inventory(db: Session = Depends(get_db)):

    fabrics = db.query(Fabric).all()

    return fabrics


@app.post("/inventory")
def add_inventory(data: dict, db: Session = Depends(get_db)):

    print("Received:", data)   # ADD THIS LINE

    fabric = Fabric(
        name=data.get("name"),
        quantity=data.get("quantity"),
        sustainability_score=data.get("sustainability_score")
    )

    db.add(fabric)
    db.commit()

    return {"message": "Fabric added"}

# -------------------------
# OUTFIT GENERATOR
# -------------------------


class OutfitRequest(BaseModel):

    fabric: str
    color: str
    occasion: str

    gender: Optional[str] = None
    body_type: Optional[str]  = None
    season: Optional[str]  = None
    style: Optional[str]  = None
    fit: Optional[str]  = None
    climate: Optional[str]  = None
    culture: Optional[str] = None


@app.post("/generate-outfit")
def create_outfit(request: OutfitRequest):

    print("Received:", request.dict())  # DEBUG

    result = generate_outfit(

        fabric=request.fabric,
        color=request.color,
        occasion=request.occasion,
        gender=request.gender,
        body_type=request.body_type,
        season=request.season,
        style=request.style,
        fit=request.fit,
        climate=request.climate,
        culture=request.culture

    )

    return result




# -------------------------
# CHAT
# -------------------------

@app.post("/chat")
def chat(data: dict):

    result = chat_with_ai(data["message"])

    return {"result": result}


# -------------------------
# SQL QUERY
# -------------------------

@app.post("/query")
def query(data: dict, db: Session = Depends(get_db)):

    sql = generate_sql(data["question"])

    result = execute_safe_query(db, sql)

    return {
        "sql": sql,
        "result": result
    }

app.mount("/", StaticFiles(directory=".", html=True), name="static")