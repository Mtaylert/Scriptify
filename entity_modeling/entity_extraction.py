import torch
from torch.optim import Adam
from torch.utils.data import DataLoader

from entity_modeling.data_setup import TrainData
from entity_modeling.ner_model import BertNER, loss_fn


class NerModel(object):
    def __init__(self, epochs, learning_rate, train_batch_size):
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.train_batch_size = train_batch_size
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = BertNER(num_labels=3)

    def _get_optimizer_params(self, model, encoder_lr, decoder_lr, weight_decay=0.0):
        no_decay = ["bias", "LayerNorm.bias", "LayerNorm.weight"]
        optimizer_parameters = [
            {
                "params": [
                    p
                    for n, p in model.model.named_parameters()
                    if not any(nd in n for nd in no_decay)
                ],
                "lr": encoder_lr,
                "weight_decay": weight_decay,
            },
            {
                "params": [
                    p
                    for n, p in model.model.named_parameters()
                    if any(nd in n for nd in no_decay)
                ],
                "lr": encoder_lr,
                "weight_decay": 0.0,
            },
            {
                "params": [p for n, p in model.named_parameters() if "model" not in n],
                "lr": decoder_lr,
                "weight_decay": 0.0,
            },
        ]
        return optimizer_parameters

    def fit(self, annotated_json_filepath):
        train_dataset = TrainData(annotated_json_filepath)
        train_dataloader = DataLoader(
            train_dataset, shuffle=True, batch_size=self.train_batch_size
        )
        self.model.to(self.device)
        param_optimizer = list(self.model.named_parameters())
        no_decay = ["bias", "LayerNorm.bias", "LayerNorm.weight"]
        optimizer_parameters = [
            {
                "params": [
                    p for n, p in param_optimizer if not any(nd in n for nd in no_decay)
                ],
                "weight_decay": 0.001,
            },
            {
                "params": [
                    p for n, p in param_optimizer if any(nd in n for nd in no_decay)
                ],
                "weight_decay": 0.0,
            },
        ]
        optimizer = Adam(params=optimizer_parameters, lr=self.learning_rate)
        for epoch_num in range(self.epochs):
            self.model.train()
            for batch in train_dataloader:
                optimizer.zero_grad()
                b_input_ids = batch["input_ids"].to(self.device)
                b_attn_mask = batch["attention_mask"].to(self.device)
                b_token_type_ids = batch["token_type_ids"].to(self.device)
                b_tags = batch["target_tags"].to(self.device)
                logits = self.model(
                    input_id=b_input_ids,
                    attention_mask=b_attn_mask,
                    token_type_ids=b_token_type_ids,
                )
                loss = loss_fn(
                    output=logits, target=b_tags, mask=b_attn_mask, num_labels=3
                )
                print(f"Loss: {loss.item()}")
                loss.backward()
                optimizer.step()


ner = NerModel(epochs=2, learning_rate=0.001, train_batch_size=8)
fp = "/Users/home/workplace/Scriptify/test_data/entity_annotation/entity_labeling.json"
ner.fit(fp)
