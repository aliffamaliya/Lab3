#
# Aliffa g12460776
#

import pandas as pd

# Load data
df = pd.read_csv('c:\Users\User\Downloads\smoker.csv')

# Inspect value
df.head()
df.tail()

# Visualize
df['smoker'].hist()
plt.show