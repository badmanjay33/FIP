import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", palette="colorblind")
df = sns.load_dataset("tips")

fig, ax = plt.subplots(figsize=(7, 5))

sns.kdeplot(data=df, x="total_bill", y="tip",
            fill=True,
            cmap="Blues",       # color map for contours
            thresh=0.05,        # cut off very low density regions
            levels=10,          # number of contour levels
            ax=ax)

ax.set_title("2D KDE — Bill vs Tip")
ax.set_xlabel("Total Bill ($)")
ax.set_ylabel("Tip ($)")
plt.show()