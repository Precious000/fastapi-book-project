from fastapi import APIRouter

from api.routes import books, stage2

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])
api_router.include_router(stage2.router, tags=["stage2"])
