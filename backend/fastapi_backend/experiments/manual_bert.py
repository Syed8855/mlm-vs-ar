from transformers import AutoTokenizer
from transformers import AutoModelForMaskedLM
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

model = AutoModelForMaskedLM.from_pretrained(
    "bert-base-uncased"
)

text = "Machine learning is [MASK]."

inputs = tokenizer(
    text,
    return_tensors ="pt"
)
print(inputs)
outputs = model(**inputs)
print(outputs.logits.shape)
