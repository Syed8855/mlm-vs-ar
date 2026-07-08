from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="bert-base-uncased"
)
result = fill_mask(
    "Machine learning is [MASK]."
)

print(result)