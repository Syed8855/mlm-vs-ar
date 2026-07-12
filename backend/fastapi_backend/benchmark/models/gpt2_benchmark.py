from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM
import torch 

from benchmark.models.base_benchmark import BaseBenchmark
from benchmark.metrics.metrics import MetricsCollector
from benchmark.schemas.benchmark_result import BenchmarkResult 

class GPT2Benchmark(BaseBenchmark):

    def __init__(self):

        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")

        self.model = AutoModelForCausalLM.from_pretrained("gpt2")

    def run(self,text:str):

        metrics = MetricsCollector()
        metrics.start()

        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        generated_ids = self.model.generate(**inputs, max_new_tokens=20)
        metrics.stop()
        generated_text = self.tokenizer.decode(generated_ids[0], skip_special_tokens=True)
        return BenchmarkResult(
            model="gpt2",
            prediction=generated_text,
            confidence=0.0, 
            inference_time=metrics.elapsed_time()
        )
              
