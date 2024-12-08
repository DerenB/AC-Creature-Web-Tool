from pydantic import BaseModel

class Fish(BaseModel):
    id: int
    name: str
    price: int
    location: str
    shadow_size: str
    month_start: int
    month_end: int
    time_start: int
    time_end: int