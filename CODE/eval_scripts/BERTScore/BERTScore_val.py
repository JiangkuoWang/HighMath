import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from bert_score import score
import json


with open("", 'r', encoding='utf-8') as f:
    data = json.load(f)

sources = [item['source'] for item in data['translations']]
references = [item['reference'] for item in data['translations']]
candidates = [item['prediction'] for item in data['translations']]


P, R, F1 = score(candidates, references, lang='other')

results = {
    "sentences": [],
    "average_scores": {
        "precision": torch.mean(P).item(),
        "recall": torch.mean(R).item(),
        "f1": torch.mean(F1).item()
    }
}

for i, (source, ref, gen, p, r, f) in enumerate(zip(sources, references, candidates, P, R, F1)):
    sentence_result = {
        "source": source,
        "reference": ref,
        "generated": gen,
        "scores": {
            "precision": p.item(),
            "recall": r.item(),
            "f1": f.item()
        }
    }
    results["sentences"].append(sentence_result)
    # print(f"Sentence {i+1}:")
    # print(f"Precision: {p:.4f}, Recall: {r:.4f}, F1: {f:.4f}")
    # print()

print(f"Average Precision: {results['average_scores']['precision']:.4f}")
print(f"Average Recall: {results['average_scores']['recall']:.4f}")
print(f"Average F1: {results['average_scores']['f1']:.4f}")

# 将结果保存到json文件中
with open("/BERTScore_results/ar22_BERTScore_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("saved")
