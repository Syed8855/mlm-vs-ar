from benchmark.models.bert_benchmark import BertBenchmark

bert = BertBenchmark()

result = bert.run("Machine learning is [MASK].")

print(result)
