from fastapi import APIRouter, Request

# Create Router
router = APIRouter()

# Get Data variable
from data.data_fish_north import data_fish_north
from data.data_fish_south import data_fish_south
from data.data_bug_north import data_bug_north
from data.data_bug_south import data_bug_south
from data.data_creature_north import data_creature_north
from data.data_creature_south import data_creature_south

@router.get("/")
async def read_available():
    return {
        "data": "current"
    }