from transformers import AutoTokenizer
from transformers import AutoModelForMaskedLM
import torch

from benchmark.schemas.benchmark_result import BenchmarkResult
from benchmark.metrics.metrics import MetricsCollector

class BertBenchmark:

    def __init__(self):

        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.model = AutoModelForMaskedLM.from_pretrained(
            "bert-base-uncased")
    def run(self,text:str):
        metrics = MetricsCollector()

        metrics.start()

        inputs = self.tokenizer(text, return_tensors="pt")

        outputs = self.model(**inputs)

        metrics.stop()

        return BenchmarkResult(
            model="bert-base-uncased",
            prediction="TODO",
            confidence=0.0,
            inference_time=metrics.elapsed_time()
        )
