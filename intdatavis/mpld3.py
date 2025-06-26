import matplotlib.pyplot as plt
import mpld3

fig, ax = plt.subplots()
ax.plot(df['x'], df['y'], marker='o')
ax.set_title('Interactive Plot using mpld3')
mpld3.display()
