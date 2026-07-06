from fastapi import APIRouter
from app.schemas.benchmark import PromptRequest
from app.services.benchmark_service import run_benchmark

router = APIRouter()
@router.post("/benchmark")
def benchmark(request: PromptRequest):
    return run_benchmark(request.prompt)