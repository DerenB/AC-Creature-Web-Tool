from pydantic import BaseModel

class Creature(BaseModel):
    id: int
    name: str
    price: int
    size: str
    speed: str
    month_start: int
    month_end: int
    time_start: int
    time_end: int