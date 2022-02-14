import pandas as pd

df = pd.read_csv('Dummy medical dataset.csv')

df.to_json('data.json',orient='index')