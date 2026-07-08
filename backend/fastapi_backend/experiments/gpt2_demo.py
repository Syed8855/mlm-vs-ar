from transformers import pipeline

generator = pipeline(
    'text-generation',
    model ="gpt2"
)
result = generator(
    "machine learning is",
    max_new_tokens=20
)
print(result)