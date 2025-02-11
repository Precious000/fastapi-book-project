from fastapi import APIRouter

router = APIRouter()

@router.get("/stage2")
async def stage2_endpoint():
    return {"message": "Stage2 endpoint is working!"}


