import pickle
from pprint import pprint
import pandas as pd

with open('keywords.pkl', 'rb') as f:
    data = pickle.load(f)
df = pd.read_pickle('keywords.pkl')
pprint(df)