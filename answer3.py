import pandas as pd
from collections import Counter

def extract_top3_chars(df):
    temp_df = df[df['date']>'13/11/2021']
    d = {}
    for sentence in temp_df['caption']:
        if type(sentence) == str:
            for char in sentence:
                if not char.isalnum() and char!=' ':
                    if char in d:
                        d[char]+=1
                    else:
                        d[char] =1
    k = Counter(d)
    top_3 = k.most_common(3)
    top3 = []
    for i in top_3:
        top3.append((i[0],i[1]))
    return top3

df = pd.read_csv("Captions.csv")
df['date'] = pd.to_datetime(df['date'])

print(extract_top3_chars(df))