import torch
from torch import nn
from transformers import AutoModel


class BertNER(nn.Module):
    def __init__(self, num_labels=3):
        super(BertNER, self).__init__()
        self.bert = AutoModel.from_pretrained("bert-base-cased", return_dict=False)
        self.dropout = nn.Dropout(0.3)
        self.out = nn.Linear(768, num_labels)

    def forward(self, input_id, attention_mask, token_type_ids):
        o1, _ = self.bert(
            input_ids=input_id,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
        )
        dropout = self.dropout(o1)
        logits = self.out(dropout)
        return logits


def loss_fn(output, target, mask, num_labels):
    lfn = nn.CrossEntropyLoss()
    active_loss = mask.view(-1) == 1
    active_logits = output.view(-1, num_labels)
    active_labels = torch.where(
        active_loss, target.view(-1), torch.tensor(lfn.ignore_index).type_as(target)
    )
    loss = lfn(active_logits, active_labels)
    return loss
