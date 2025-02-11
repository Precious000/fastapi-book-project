from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter()

@router.get("/")

async def stage2():
    return {"message": "Stage2 endpoint is working!"}

@router.head("/")
async def stage2_head():
    return Response(headers={"X-Message": "Stage2 HEAD request"})




