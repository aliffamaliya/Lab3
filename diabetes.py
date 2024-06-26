#
# Aliffa Maliya G12460776
# Pandas Practice
#

import pandas as pd
import matlptlib.pyplot as plt

# Load data
df = pd.read_csv("diabetes.csv")

# Inspect structure
#df.shaped.info()

# Inspect value
#df.head() 
#df.tail()

# Add missing values
df2 = df.copy()
df2.loc[2:5, "Pregnancies"] = None
print(df2.head(10))

# Remove rows with missing values
df3 = df2.copy()
df3 = df3.dropna()
df3.shape

# By group
df.groupby('Outcome').mean()
df.groupby(['Pregnancies'],'Outcome').mean()
df.groupby(['Pregnancies'],'Outcome').value_counts()
df.groupby(['Pregnancies'],'Outcome').value_counts(normalize=True)

df[['BMI', 'Glucose']].plot.line()
plt.title('Aliffa')
plt.show()
