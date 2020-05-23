import os
os.chdir('C:\\Users\\<folder>\\Desktop\\<folder>\\datafiles')
import pandas as pd

df = pd.read_csv('titanic.csv')



#df = pd.read_csv('titanic.csv', index_col=0)
df.describe()
df.shape


df.head()