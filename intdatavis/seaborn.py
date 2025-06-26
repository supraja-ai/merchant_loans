import seaborn as sns

# Create a simple Seaborn scatter plot
tips = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data=tips)
import matplotlib.pyplot as plt

sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Seaborn Scatter Plot (Interactive in Notebook)")
plt.show()
