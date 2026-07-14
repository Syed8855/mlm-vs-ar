"""backend/fastapi_backend/app/services/benchmark_service.py"""
def run_benchmark(prompt:str):
    return {
        "received_prompt": prompt,
        "status": "benchmark Started"
    }