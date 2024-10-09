import numpy as np
import pandas as pd

dict1 = {
    'name' : ['mikey', 'rohan', 'skillf', 'shubh'],
    'marks' : [92, 34, 24, 17],
    'city' : ['janakpur', 'rampur', 'barelly', 'antartica']
}

df = pd.DataFrame(dict1)
# df.to_csv('./friends_index_false.csv', index=False)

# print(df.head(2))
# print(df.tail(2))

# print(df.describe())

# df = pd.read_csv('./data-sets/test.csv')
df.index = ['first', 'second', 'third', 'forth']
print(df)