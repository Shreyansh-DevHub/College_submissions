with open("students.txt", "w") as f:
    f.write("101,Alice,85\n")
    f.write("102,Bob,72\n")
    f.write("103,Charlie,91\n")
print("Records written.")
# Reading from file
print("\nStudent Records:")
with open("students.txt", "r") as f:
    for line in f:
        roll, name, marks = line.strip().split(",")
        print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
