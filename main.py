from preprocessor import preprocess

with open("chat/chat.txt", "r", encoding="utf-8") as f:
    data = f.read()

df = preprocess(data)

print(df.head())
print(df.shape)