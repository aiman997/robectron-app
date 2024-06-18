from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True
