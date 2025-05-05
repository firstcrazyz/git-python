from fastapi import APIRouter, Depends
from app.api import  packingstock

api_router = APIRouter()


api_router.include_router(packingstock.router,
                          tags=["packingstock"])
