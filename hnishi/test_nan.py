import pandas as pd
import numpy as np

s = pd.Series([2,3,np.nan,7,"The Hobbit"])

s
s.isnull()
print (s)
print (s.isnull())

#https://chartio.com/resources/tutorials/how-to-check-if-any-value-is-nan-in-a-pandas-dataframe/

