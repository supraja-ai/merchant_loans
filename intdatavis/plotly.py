import plotly.express as px
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'x': list(range(10)),
    'y': [x**2 for x in range(10)]
})

# Create an interactive line chart
fig = px.line(df, x='x', y='y', title='Interactive Line Plot')
fig.show()
