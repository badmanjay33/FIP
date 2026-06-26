import pandas as pd

# Read the file
FILE_PATH = "data_files/goals.csv"
df = pd.read_csv(FILE_PATH, index_col="player_name")

print(df.head())
print(df.info())
print(df.describe().to_string())

print(df.mean(numeric_only=True))
print(df.median(numeric_only=True))
print(df.mode(numeric_only=True).to_string())
print(df.std(numeric_only=True))
print(df.corr(numeric_only=True).to_string())