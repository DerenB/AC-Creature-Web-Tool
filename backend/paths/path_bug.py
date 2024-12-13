from fastapi import APIRouter, Request

# Create Router
router = APIRouter()

# Get Data variable
from data.data_bug_north import data_bug_north


# TEST
@router.get("/bug")
async def read_bug():
    return {
        "data": data_bug_north
    }



