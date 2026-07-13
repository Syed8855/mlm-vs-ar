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

        mask_token_index = (
            inputs["input_ids"] == self.tokenizer.mask_token_id
            ).nonzero(as_tuple=True)[1]
        
        mask_logits = outputs.logits[0,mask_token_index, :]

        probabilities = torch.softmax(mask_logits,dim=-1)

        predicted_id = torch.argmax(probabilities,dim=-1)

        prediction = self.tokenizer.decode(predicted_id).strip()

        confidence = probabilities[0,predicted_id].item()




        metrics.stop()

        return BenchmarkResult(
            model="bert-base-uncased",
            prediction=prediction,
            confidence=confidence,
            inference_time=metrics.elapsed_time()
        )
