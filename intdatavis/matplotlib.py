# In a Jupyter Notebook cell, run the magic command:
%matplotlib notebook
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'x': list(range(10)),
    'y': [x * 2 for x in range(10)]
})

fig, ax = plt.subplots()
ax.plot(df['x'], df['y'], marker='o')
ax.set_title("Interactive Plot (Jupyter Notebook)")
plt.show()
#