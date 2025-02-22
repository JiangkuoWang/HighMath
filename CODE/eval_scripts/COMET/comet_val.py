import json
import sys
from comet import load_from_checkpoint

json_file_path = sys.argv[1]
model_path = sys.argv[2]
output_file_path = sys.argv[3]
gpus = int(sys.argv[4])


with open(json_file_path, 'r', encoding='utf-8') as file:
    dataset = json.load(file)

data = []
for item in dataset['translations']:
    data.append({
        "src": item['source'],
        "mt": item['prediction'],
        "ref": item['reference']
    })

model = load_from_checkpoint(model_path)
model_output = model.predict(data, batch_size=8, gpus=gpus)


results = {
    "scores": model_output.scores, 
    "system_score": model_output.system_score  
}


with open(output_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(results, outfile, ensure_ascii=False, indent=4)

print(f"system_score == {model_output.system_score}")
print(f"saved in {output_file_path}")
