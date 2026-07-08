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

mask_token_index = torch.where(inputs["input_ids"] == tokenizer.mask_token_id)[1]

mask_logits = outputs.logits[
    0,mask_token_index, :]

probabilities = torch.softmax(mask_logits,dim=-1)

predicted_token_id = torch.argmax(probabilities,dim=-1)

predicted_word = tokenizer.decode(predicted_token_id)

print(predicted_word)

