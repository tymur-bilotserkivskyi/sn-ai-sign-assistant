from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def get_health():
    """
    health check endpoint
    """
    heals_info = {
        "status": "ok"
    }
    return heals_info