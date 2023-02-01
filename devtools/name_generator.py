import names
import json
stored = []

for i in range(20):
    naming = names.get_full_name()
    first = naming.split()[0]
    last =naming.split()[1]
    out = {"text": str(naming), 'labels':["B-Name","I-Name"]}
    stored.append(out)

with open('/Users/home/workplace/Scriptify/test_data/entity_annotation/generative_names.json', 'w') as f:
     f.write(json.dumps(stored, indent=4))