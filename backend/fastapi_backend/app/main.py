from fastapi import FastAPI
from app.schemas.benchmark import PromptRequest
from app.routers import benchmark
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("loading application resources")

    yield

    print("cleaning up application resources")

app = FastAPI(lifespan=lifespan)

app.include_router(benchmark.router)


@app.get("/")
def home():
    return {
        "message" : "Welcome to MLM vs AR Benchmark"
    }
