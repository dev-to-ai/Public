# Lists
my_list = [1, "a", 3.5, True, [100, 3, 3, "apple"]]
print(my_list)

fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple
print(fruits[-1])   # cherry

fruits[1] = "orange"
fruits.append("mango")

# Slicing
print(fruits[1:3]) # list[start : end], start → index to begin (included), end → index to stop (excluded): ['orange', 'cherry']
print(fruits[:3]) # First 3 fruits: ['apple', 'orange', 'cherry']
print(fruits[2:]) # From index 2 to end: ['cherry', 'mango']
print(fruits[-2:]) # Last 2 fruits: ['cherry', 'mango']

fruits.remove("apple")
fruits.insert(1, "peach")
fruits.pop(2)
print(fruits)  # ['orange', 'peach', 'mango']

print(len(fruits)) # 3

fruits.reverse()
print(fruits) # ['mango', 'peach', 'orange']

fruits.sort()
print(fruits) # ['mango', 'orange', 'peach']

# Show all items
for item in fruits:
    print(item)

fruits.clear()
print(fruits) # []

# A nested list is a list that contains other lists.
fruits = [
    ["apple", "banana"],
    ["mango", "orange"],
    ["cherry", "grape"]
]
print(fruits[0])      # ['apple', 'banana']
print(fruits[0][1])   # banana
print(fruits[2][0])   # cherry

# List comprehension creates a new list from an existing list in one line.
fruits = ["apple", "banana", "cherry"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)

fruits = ["apple", "banana", "cherry", "mango"]
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print(long_fruits)