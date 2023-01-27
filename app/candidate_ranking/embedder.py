import torch
from sentence_transformers import SentenceTransformer
import numpy as np
import os
from typing import List

class TextEmbedder:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.retriever = SentenceTransformer('flax-sentence-embeddings/all_datasets_v3_mpnet-base', device = self.device)
    def single_embed(self, input_text: str):
        embedding = np.array(self.retriever.encode(input_text))
        return embedding
    def batch_embed(self, input_text_list: List):
        embeddings = self.retriever.encode(input_text_list).to_list()
        return embeddings



if __name__ == '__main__':
    jd_path = "/Users/home/workplace/Scriptify/test_data/test_jds/"
    saved_embeds = {}
    for idx, file in enumerate(os.listdir(jd_path)):
        with open(jd_path+file, 'r') as file:
            jd_text = file.read()
        embed = TextEmbedder().embed(input_text=jd_path+jd_text)
        saved_embeds[idx] = embed
    
