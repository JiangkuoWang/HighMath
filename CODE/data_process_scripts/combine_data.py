import json
import random

def read_json_file(file_name, num_entries):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data[:num_entries]

def main():

    files_and_entries = {

    }
    
    output_file = ''
    random.seed(55)
    all_entries = []
    
    for file_name, num_entries in files_and_entries.items():
        entries = read_json_file(file_name, num_entries)
        for entry in entries:
            translated_response = entry.get('translated_response','')
            translated_query = entry.get('translated_query',"")
            if (translated_query==""):
                translated_response = entry.get('response','')
                translated_query = entry.get('query',"")
            all_entries.append({
                'query': translated_query,
                'response': translated_response,
            })
    
    random.shuffle(all_entries)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_entries, f, ensure_ascii=False, indent=4)
    
    print(f'Shuffled data saved to {output_file}')

if __name__ == '__main__':
    main()
