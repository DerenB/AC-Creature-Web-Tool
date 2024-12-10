from fastapi import APIRouter, Request

# Create Router
router = APIRouter()

# Get Data variable
from data.data_fish_north import data_fish_north


# TEST
@router.get("/fish")
async def read_fish():
    return {
        "data": data_fish_north
    }



