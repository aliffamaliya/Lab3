#
# Aliffa g12460776
#

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r'c:\Users\User\Downloads\smoker.csv')

# Inspect structure
df.shape
df.info()

df.head()
df.tail()

# Inspect value
df.head()
df.tail()

# Visualize
df['smoker'].hist()
plt.show()

# Sum
df.sum()
df.sum(axis=1)