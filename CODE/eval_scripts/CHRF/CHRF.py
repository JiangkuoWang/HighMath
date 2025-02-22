from sacrebleu.metrics import CHRF, TER
import json

with open("", 'r', encoding='utf-8') as f:
    data = json.load(f)

sources = [item['source'] for item in data['translations']]
references = [item['reference'] for item in data['translations']]
candidates = [item['prediction'] for item in data['translations']]

ter = TER()
chrf = CHRF()

ter_score = ter.corpus_score(candidates,references)
chrf_score = chrf.corpus_score(candidates,references)

print(ter_score)
print(chrf_score)