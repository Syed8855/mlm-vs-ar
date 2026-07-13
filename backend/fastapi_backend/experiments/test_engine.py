from benchmark.engine.benchmark_engine import BenchmarkEngine

engine = BenchmarkEngine()

bert_result = engine.run(
    "bert",
    "Machine learning is [MASK]."
)

print(bert_result)

print()

gpt2_result = engine.run(
    "gpt2",
    "Machine Learning is")

print(gpt2_result)