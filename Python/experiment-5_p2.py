import re

text = "Python is great. Python is easy. I love Python!"


words = re.findall(r"\b[a-zA-Z]+\b", text)
print("Words:", words)


freq = {}

for w in words:
    freq[w.lower()] = freq.get(w.lower(), 0) + 1
    print("Frequency:", freq)

new_text = re.sub(r"Python", "Java", text)
print("After replace:", new_text)

print("\nname: shreyansh singh")
print("prn no.: 26013010907")