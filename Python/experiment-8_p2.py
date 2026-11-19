import pandas as pd
import matplotlib.pyplot as plt
# Create DataFrame

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Math": [85, 72, 91, 64, 78],
    "Science": [88, 65, 82, 90, 71],
    "English": [76, 80, 68, 74, 95],
}
df = pd.DataFrame(data)


# Analysis
df["Total"] = df[["Math","Science","English"]].sum(axis=1)
df["Average"] = df["Total"] / 3
print(df)
print("\nClass Average:")
print(df[["Math","Science","English"]].mean())



# Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 5))



# Bar chart
df.plot(x="Name", y=["Math","Science","English"],
        kind="bar", ax=axes[0], title="Subject-wise Marks")
axes[0].set_ylabel("Marks")




# Pie chart – average marks distribution
avg = df[["Math","Science","English"]].mean()
axes[1].pie(avg, labels=avg.index, autopct="%1.1f%%")
axes[1].set_title("Average Marks Distribution")
plt.tight_layout()
plt.savefig("analysis.png")
plt.show()


print("Name: Shreyansh Singh")
print("Prn No. 26013010907")