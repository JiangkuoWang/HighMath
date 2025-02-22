import json
import random

input_file = ''
output_file = ''
num_samples = 20000
random_seed = 42 

random.seed(random_seed)

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

if num_samples > len(data):
    print(f"数据总量不足{num_samples}条，抽取所有数据。")
    num_samples = len(data)

sampled_data = random.sample(data, num_samples)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(sampled_data, f, ensure_ascii=False, indent=4)

print(f"已成功抽取{num_samples}条数据并写入'{output_file}'文件中。")
