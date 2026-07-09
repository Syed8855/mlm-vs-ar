from dataclasses import dataclass

@dataclass
class BenchmarkResult:
    model:str
    prediction:str
    confidence:float
    inference_time:float