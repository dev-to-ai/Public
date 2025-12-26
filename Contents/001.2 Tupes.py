#Tuples
point = (3,5)
# point[0] = 10   # TypeError - 
person = ("Alice", 30, 5.6)
single = (10,)   # comma is required
not_a_tuple = (10)  # this is just an integer
print(not_a_tuple)

# Tuples often represent fixed data structures
employee = ("E123", "John", "Engineering", 75000)

colors = ("red", "green", "blue")
print(colors[0])   # red
print(colors[-1])  # blue

numbers = (1, 2, 3, 4, 5)
print(numbers[1:4])  # (2, 3, 4)

point = (3, 5)
x, y = point
print(x)  # 3
print(y)  # 5

# Swapping variables
a = 10
b = 20
a, b = b, a
print(a, b)  # 20 10

# Tuples as Function Returns
def get_min_max(numbers):
    return min(numbers), max(numbers)
result = get_min_max([4, 1, 9, 2])
print(result)  # (1, 9)

# Truples can be dictionary keys because they are immutable.
# Lists cannot be dictionary keys because they are mutable.
locations = {
    (0, 0): "Origin",
    (1, 2): "Point A"
}

# Truple functions
nums = (1, 2, 2, 3)
print(nums.count(2))  # 2
print(nums.index(3))  # 3

# Nested tuples
matrix = (
    (1, 2, 3),
    (4, 5, 6)
)
print(matrix[1][2])  # 6

# Real-World Example
student = ("S101", "Emma", "Physics", 3.8)
id, name, major, gpa = student
print(major)

location = (37.7749, -122.4194)  # latitude, longitude





