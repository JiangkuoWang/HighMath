import json

file_path = ''
new_file_path = ''


new_data = []


with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        json_str = ''.join(lines[i:i+3])
        item = json.loads(json_str)
        translated_query = item.get("translated_query", "")
        if "Question:" in translated_query and "Response:" in translated_query:
            question = translated_query.split("Question:")[1].split("Response:")[0].strip()
            response = translated_query.split("Response:")[1].strip()
            new_data.append({"question": question, "response": response})
        else:
            new_data.append(item)

with open(new_file_path, 'w', encoding='utf-8') as file:
    json.dump(new_data, file, ensure_ascii=False, indent=4)

print("saved in", new_file_path)