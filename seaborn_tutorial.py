import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
df = sns.load_dataset("tips")

fig, ax = plt.subplots(figsize=(7, 5))

corr = df.select_dtypes(include="number").corr()  # compute correlation matrix

sns.heatmap(corr,
            annot=True,          # show numbers inside cells
            fmt=".2f",           # 2 decimal places
            cmap="coolwarm",     # red = positive, blue = negative
            center=0,            # center colormap at 0
            linewidths=0.5,     # grid lines between cells)
            ax=ax)

ax.set_title("Correlation matrix — tips dataset")
plt.show()