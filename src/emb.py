import torch
import torch.nn as nn
import torch.optim as optim

vocab = ['cat','dog','banana','apple']
stoi = {word: i for i, word in enumerate(vocab)}
sentence = ['cat', 'banana']
inputs = torch.tensor([stoi[word] for word in sentence], dtype=torch.long)

print(f'Input tensor: {inputs}')
emb_dim = 8
embedding = nn.Embedding(num_embeddings=len(vocab), embedding_dim=emb_dim)

outputs = embedding(inputs)
print(f'Embedded Outputs: {outputs}')