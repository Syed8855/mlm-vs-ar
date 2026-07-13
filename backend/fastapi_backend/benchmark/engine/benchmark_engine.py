from benchmark.models.gpt2_benchmark import GPT2Benchmark
from benchmark.models.bert_benchmark import BertBenchmark

class BenchmarkEngine:

    def __init__(self):
        self.models ={
            "bert" : BertBenchmark(),
            "gpt2" : GPT2Benchmark()
        }
    def run(self,model:str,text:str):
        if model not in self.models:
            raise ValueError("Unsupported model")
        benchmark = self.models[model]
        return benchmark.run(text)
