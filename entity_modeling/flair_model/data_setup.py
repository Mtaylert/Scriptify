
import json




def flair_setup(fp):
    with open(fp, 'r') as file:
        data = json.load(file)
    
    output = {"text": [], "annotation": []}
    for rec in data:
        text = rec['text']
        labels = rec['labels']
        print(text)
        print(labels)
    print()


fp = "/Users/home/workplace/Scriptify/test_data/entity_annotation/entity_labeling.json"
flair_setup(fp=fp)