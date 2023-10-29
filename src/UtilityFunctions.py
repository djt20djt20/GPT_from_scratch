def encode(word,all_chars):
  stoi = {ch:i for i, ch in enumerate(all_chars)}
  return [stoi[letter] for letter in word]

def decode(integers, all_chars):
  itos = {i:ch for i, ch in enumerate(all_chars)}
  return ''.join([itos[i] for i in integers])