"""Basic examples of Python collections."""
"""
# List: ordered and changeable
fruits = ["apple", "banana", "mango"]
print("Original list:", fruits)
print("First item:", fruits[0])          
print("Last item:", fruits[-1])
print("First two items:", fruits[0:2])   

fruits.append("orange")                
print("After append:", fruits)

removed_fruit = fruits.pop()             
print("Popped item:", removed_fruit)
print("After pop:", fruits)

fruits[1] = "grapes"                    
print("After changing a value:", fruits)
"""
colors = ("red", "green", "blue", "green")
print("\nTuple:", colors)
print("Tuple length:", len(colors))
print("Number of times green appears:", colors.count("green"))
print("Index of blue:", colors.index("blue"))
print("Is red in the tuple?", "red" in colors)

color1, color2, color3, color4 = colors
print("Unpacked values:", color1, color2, color3, color4)

# Tuples cannot be changed directly, but a new tuple can be created.
new_colors = colors + ("yellow",)
print("Tuple after adding an item:", new_colors)
"""
# Set: unordered collection of unique items
numbers = {1, 2, 3, 3}
print("\nSet (duplicates are removed):", numbers)
numbers.add(4)
print("Set after adding 4:", numbers)
numbers.remove(2)
print("Set after removing 2:", numbers)
print("Is 3 in the set?", 3 in numbers)

other_numbers = {3, 4, 5, 6}
print("Union:", numbers | other_numbers)
print("Intersection:", numbers & other_numbers)
print("Difference:", numbers - other_numbers)

# Dictionary: key-value pairs
student = {"name": "Shreyansh", "age": 20, "course": "Python"}
print("\nDictionary:", student)
print("Student name:", student["name"])
student["age"] = 21                    # Change a value
student["city"] = "Delhi"              # Add a new key-value pair
print("Dictionary after changes:", student)

print("\nDictionary keys:")
for key in student:
    print(key)

print("\nDictionary values:")
for value in student.values():
    print(value)

print("\nDictionary keys and values:")
for key, value in student.items():
    print(key, ":", value)

print("\nUsing get():", student.get("course"))
print("Is 'name' a key?", "name" in student)

student.pop("city")
print("After removing city:", student)
"""
print("\nname: shreyansh singh")
print("prn no.: 26013010907")
