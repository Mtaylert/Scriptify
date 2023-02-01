import json

import torch
from torch.utils.data import Dataset
from transformers import AutoTokenizer


class Config:
    LABEL_TO_ID = {"B-Name": 1, "I-Name": 2, "o": 0}
    ID_TO_LABEL = {1: "B-Name", 2: "I-Name", 0: "o"}
    MODEL = "bert-base-cased"
    MAX_LEN = 128
    TOKENIZER = AutoTokenizer.from_pretrained(MODEL, do_lower_case=True)


def datareader(filepath):
    flattened_data = {"text": [], "labels": []}
    with open(filepath, "r") as file:
        data = json.load(file)

    for record in data:
        for name in ["text", "labels"]:
            flattened_data[name].append(record[name])
    return flattened_data


class TrainData(Dataset):
    def __init__(self, annotated_json_filepath: json):
        data = datareader(annotated_json_filepath)
        self.text = data["text"]
        self.labels = data["labels"]
        self.tokenizer = AutoTokenizer.from_pretrained(Config.MODEL)

    def __len__(self):
        return len(self.text)

    def __getitem__(self, index):
        text = self.text[index]
        tags = [Config.LABEL_TO_ID[tag] for tag in self.labels[index]]

        ids = []
        target_tag = []

        for i, s in enumerate(text):
            inputs = Config.TOKENIZER.encode(s, add_special_tokens=False)
            input_len = len(inputs)
            ids.extend(inputs)
            target_tag.extend([tags[i]] * input_len)

        ids = ids[: Config.MAX_LEN - 2]
        target_tag = target_tag[: Config.MAX_LEN - 2]

        ids = [101] + ids + [102]
        target_tag = [0] + target_tag + [0]

        mask = [1] * len(ids)
        token_type_ids = [0] * len(ids)

        padding_len = Config.MAX_LEN - len(ids)

        ids = ids + ([0] * padding_len)
        mask = mask + ([0] * padding_len)
        token_type_ids = token_type_ids + ([0] * padding_len)
        target_tag = target_tag + ([0] * padding_len)

        return {
            "input_ids": torch.tensor(ids, dtype=torch.long),
            "attention_mask": torch.tensor(mask, dtype=torch.long),
            "token_type_ids": torch.tensor(token_type_ids, dtype=torch.long),
            "target_tags": torch.tensor(target_tag, dtype=torch.long),
        }


if __name__ == "__main__":
    fp = "/Users/home/workplace/Scriptify/test_data/entity_annotation/entity_labeling.json"
    td = TrainData(annotated_json_filepath=fp)
    for i in td:
        print(i["labels"])
