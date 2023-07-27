from fastapi import APIRouter

router = APIRouter()


@router.get("/data/", tags=["users"])
async def read_users():
    return {"message": "Data to be sent"}
