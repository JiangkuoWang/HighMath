import json
import torch
import sys
from bleurt_pytorch import BleurtConfig, BleurtForSequenceClassification, BleurtTokenizer


def main(data_file, checkpoint, output_file):
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    references = [item['reference'] for item in data['translations']]
    candidates = [item['prediction'] for item in data['translations']]

    config = BleurtConfig.from_pretrained(checkpoint)
    model = BleurtForSequenceClassification.from_pretrained(checkpoint)
    tokenizer = BleurtTokenizer.from_pretrained(checkpoint)

    if torch.cuda.device_count() > 1:
        print(f"Using {torch.cuda.device_count()} GPUs!")
        model = torch.nn.DataParallel(model)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    model.eval()
    with torch.no_grad():
        inputs = tokenizer(references, candidates, padding="max_length", return_tensors='pt',truncation=True,max_length=512)
        res = model(**inputs).logits.flatten().tolist()
    print(res)

    average_score = sum(res) / len(res)

    results = []
    for reference, candidate, score in zip(references, candidates, res):
        result = {
            "reference": reference,
            "candidate": candidate,
            "bleurt_score": score
        }
        results.append(result)

    results.append({"average_bleurt_score": average_score})

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print(f"results have been saved in {output_file}.")
    print(f"Average BLEURT Score: {average_score:.4f}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python evaluate_bleurt.py <data_file> <checkpoint> <output_file>")
        sys.exit(1)
    
    data_file = sys.argv[1]
    checkpoint = sys.argv[2]
    output_file = sys.argv[3]
    
    main(data_file, checkpoint, output_file)
