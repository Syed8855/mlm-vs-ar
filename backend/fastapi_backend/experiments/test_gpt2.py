from benchmark.models.gpt2_benchmark import GPT2Benchmark

gpt2 = GPT2Benchmark()

result = gpt2.run("Machine learning is")

print(result)