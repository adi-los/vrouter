from fastapi import APIRouter, Depends, HTTPException
from vrouter.src.domain.models.vrouter import config_Router
from vrouter.src.domain.service.vrouter_service import vrouter_service
import requests


router = APIRouter()

@router.post("/configure")
async def config_vrouter(request: config_Router, cluster_service=Depends(vrouter_service)):
    print(f"vrouter_service: {type(vrouter_service)}")
    result = vrouter_service.config_vrouter(request)
    return result
