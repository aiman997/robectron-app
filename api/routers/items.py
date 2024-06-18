from fastapi import APIRouter, HTTPException
from api import models, schemas, crud
from api.database import SessionLocal

router = APIRouter()

@router.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int):
    db = SessionLocal()
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
