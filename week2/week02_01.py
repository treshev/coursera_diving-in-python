import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()
key = args.key
value = args.value

key = 1
value = 2


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
json_from_file = {}

if os.path.isfile(storage_path) and os.path.getsize(storage_path) > 0:
    with open(storage_path, 'r') as f:
        json_from_file = json.load(f)

if value:
    with open(storage_path, 'w') as f:

        import pdb
        pdb.set_trace()

        key_value = json_from_file.get(key, [])
        json_from_file[key] = key_value
        key_value.append(value)
        json.dump(json_from_file, f)
else:
    key_value = json_from_file.get(key, None)
    if key_value:
        print(*json_from_file.get(key, None))
    else:
        print(None)