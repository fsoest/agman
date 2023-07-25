import json

with open('edgg_loas', 'r') as f:
    contents = json.loads(f.read())

print(contents)