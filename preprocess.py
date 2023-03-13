import pandas as pd

df = pd.read_csv("done.csv", usecols=['Horses'])
print(df)
df.replace('\/', '', regex=True, inplace=True)
df.replace('\+', ' ', regex=True, inplace=True)
df.replace('\d+$', '', regex=True, inplace=True)

restrict = ["mare", "stallion", "filly", "colt"]
patternDel = "|".join([i for i in restrict])
filter = df['Horses'].str.contains(patternDel)
df = df[~filter]
print(df)


df.to_csv("preprocessed.csv",  index=False)
