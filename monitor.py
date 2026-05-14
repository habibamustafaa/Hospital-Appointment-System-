from fastapi import APIRouter
import time

router = APIRouter()

# simple in-memory request counter
request_count = {
    "total_requests": 0
}


# increase request count for each endpoint
def increment_request():
    request_count["total_requests"] += 1


# metrics endpoint
@router.get("/metrics")
def get_metrics():
    return {
        "total_requests": request_count["total_requests"],
        "status": "running"
    }


#system health check endpoint
@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "time": time.time()
    }