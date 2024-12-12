from pydantic import BaseModel

class Bug(BaseModel):
    id: int
    name: str
    price: int
    location: str
    weather: str
    month_start: int
    month_end: int
    time_start: int
    time_end: int