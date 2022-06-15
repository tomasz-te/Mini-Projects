import plotly
import plotly.express as px
import pandas as pd

df = pd.read_csv('segmented_customers.csv')
print(df.columns)
df['Cluster'] = df['Cluster'].astype(str)
df['Cluster'].replace({'0': 'Families', '1': 'Young superstars', '2': 'One-kid savers', '3': 'Mature supporters'}, inplace=True)
df['size'] = df['Children'] + 1
features = ['Income', 'Age', 'Children', 'Spent']

fig = px.scatter_3d(df, x='Age', y='Income', z='Spent', color_discrete_sequence=px.colors.qualitative.Plotly,
                    color='Cluster', size='size', opacity=1, title='Four segments of customers. Size of the mark corresponds to the number of children.',
                    hover_data=['Income', 'Age', 'Children', 'Spent'])
plotly.offline.plot(fig)