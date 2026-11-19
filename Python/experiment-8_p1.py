import numpy as np
scores = np.array([85, 72, 91, 64, 78, 88, 95, 70, 55, 82])
print("Scores:", scores)
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Std Dev:", np.std(scores))
print("Min:", np.min(scores), " Max:", np.max(scores))
print("Variance:", np.var(scores))
# Sort and percentile
print("Sorted:", np.sort(scores))
print("75th Percentile:", np.percentile(scores, 75))

print("Name: Shreyansh Singh")
print("Prn No. 26013010907")