from fastapi import APIRouter, Request

# Create Router
router = APIRouter()


# TEST
@router.get("/fish")
async def read_fish():
    return {"Location": "Fish Page"}



