import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

# Importing the csv file and displaying first five rows 
ranking = pd.read_csv("Screentime - App Ranking.csv")
ranking.head()

# Counting the numbers of times the app appears in Rank 1
ranking["Rank 1"].value_counts()

# Plot to display Rank 1 column 
px.bar(
    x=ranking['Rank 1'].value_counts().index,
    y=ranking['Rank 1'].value_counts().values,
    title='Number Of Apps in Rank 1'
)

# Counting the numbers of times the app appears in Rank 2
ranking["Rank 2"].value_counts()

# Plot to display Rank 2 column 
px.bar(
    x=ranking['Rank 2'].value_counts().index,
    y=ranking['Rank 2'].value_counts().values,
    title='Number Of Apps in Rank 2'
)

# Counting the numbers of times the app appears in Rank 3
ranking["Rank 3"].value_counts()

# Plot to display Rank 3 column
px.bar(
    x=ranking['Rank 3'].value_counts().index,
    y=ranking['Rank 3'].value_counts().values,
    title='Number Of Apps in Rank 3'
)

# Converting categorical data into dummy variable for the purpose of data manipulation
df = pd.get_dummies(data=ranking, columns=['Rank 1', 'Rank 2', 'Rank 3'])
df.sample()
np.shape(df)

# To get unique values of the each column 
rank1 = set(ranking['Rank 1'])
rank2 = set(ranking['Rank 2'])
rank3 = set(ranking['Rank 3']) 
app_list = rank1.union(rank2).union(rank3)
app_list

# To display the values of columns as columns
col = []
for i in app_list:
    for name in df.columns:
        if i in name:
            col.append(name)
    ranking[i] = df[col].sum(axis=1)
    col = []
ranking.head(5)

# To drop irrelevant columns from the table
ranking.drop(['Rank 1', 'Rank 2', 'Rank 3'], axis=1, inplace=True)
ranking.columns
ranking.head(5)

# •	To display the number of times app appears in data in the form of dictionary and sort it accordingly
dic = {}
g = ranking.drop(['Date '], axis=1)
for i in g.columns:
    a = g[i].sum()
    dic[i] = a
print(dic)
df = pd.DataFrame.from_dict(dic, orient='index')
df.index.rename('App', inplace=True)
df.rename(columns={0: 'sum'}, inplace=True)
df = df.sort_values('sum', ascending=False)
df.reset_index(inplace=True)
df

# Finally displaying the final data in the form of pie chart
px.pie(names=df.App, values=df['sum'])