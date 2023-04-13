import json

def read_items(file: str = 'items.json', mode: str = 'r' ):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except Exception as e:
        write_items([], file)
    

def write_items(newData: dict, file: str = 'items.json', mode: str = 'w' ):
    with open(file, 'w') as f:
        json.dump(newData, f)
        print(f'JSON file {file} updated')

