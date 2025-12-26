# A dictionary is a data structure that stores data as key–value pairs.
person = {
    "name": "Alice",
    "age": 25,
    "role": "data scientist"
}
print(person)
# Feature Representation (Machine Learning)
# Access a feature
print(person["role"]) # data scientist

# Token Frequency (NLP Core Concept)
# Natural Language Processing relies heavily on dictionaries.
sentence = "AI is transforming AI systems"
words = sentence.split()
word_count = {} # Initialize an empty dictionary
for word in words:
    # word_count.get(word, 0) returns the current count for word if it exists in the dictionary, otherwise it returns 0. Then we add 1 to it and store it back in word_count[word].
    word_count[word] = word_count.get(word, 0) + 1
print(word_count) # {'AI': 2, 'is': 1, 'transforming': 1, 'systems': 1}

# Model Parameters & Weights
# Neural networks store parameters in dictionaries.
model_params = {
    "W1": [[0.2, 0.5], [0.1, 0.9]],
    "b1": [0.1, 0.2],
    "W2": [[0.3], [0.8]],
    "b2": [0.05]
}
print(model_params["W1"]) # [[0.2, 0.5], [0.1, 0.9]]

# Label Encoding (Supervised Learning)
# AI models require numeric labels.
label_map = {
    "cat": 0,
    "dog": 1,
    "bird": 2
}
print(label_map["dog"]) # 1

# Reverse mapping (for predictions)
# Creates a reverse mapping to convert predictions back to labels
# This converts model prediction (1) back to human-readable label ("dog")
# { } - Creates a new dictionary
# v: k - Key-value pair where v becomes the key and k becomes the value
# for k, v in label_map.items() - Loops through each key-value pair in the original dictionary
reverse_label_map = {v: k for k, v in label_map.items()}
print(reverse_label_map)
print(reverse_label_map[1]) # dog

# Caching Predictions (Performance Optimization)
# AI systems cache expensive computations.
# Empty dictionary to store cached results
prediction_cache = {}
def predict(input_data):
    # Step 1: Check if we already computed this
    # input_data must be hashable (so it can be a dictionary key). 
    # Lists are NOT hashable - weneed to convert to a tuple
    key = tuple(input_data)  # Convert list to tuple
    if key in prediction_cache:
        return prediction_cache[key] # Return cached result

    # Step 2: If not cached, compute the expensive operation
    result = sum(key)  # This could be any slow/complex calculation
    # Step 3: Store result in cache for future use
    prediction_cache[key] = result
    # Step 4: Return the result
    return result

# Computes only once, reuses result
# Without caching: Each request repeats the expensive operation
# With caching: First request does the work, subsequent requests are instant!
predict([1,2,3])  # Calculates, stores result
predict([1,2,3])  # Returns cached result
print(predict([1,2,3]))  # Returns cached result - 6

# Dictionary comprehensions are a concise and Pythonic way to create dictionaries in a single line of code, similar to list comprehensions but for dictionaries.
squares = {x: x**2 for x in range(5)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

prices = {"apple": 1.0, "banana": 0.5, "orange": 0.8}

# Apply 10% discount
discounted = {fruit: price*0.9 for fruit, price in prices.items()} # {"apple": 0.9, "banana": 0.45, "orange": 0.72}
print(discounted)

# Multiple Conditions
squares = {x: x**2 for x in range(10) if x % 2 == 0 if x > 2} 
print(squares) # {4: 16, 6: 36, 8: 64}

# ASCII codes
ascii_codes = {chr(i): i for i in range(65, 91)}  # A-Z
print(ascii_codes) # {"A": 65, "B": 66, ..., "Z": 90}

# From Two Lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
person = {keys[i]: values[i] for i in range(len(keys))}
print(person) # {"name": "Alice", "age": 25, "city": "New York"}

# Better way with zip():
person = {k: v for k, v in zip(keys, values)}
print(person) # {"name": "Alice", "age": 25, "city": "New York"}

# Create a multiplication table
multiplication_table = {
    i: {j: i*j for j in range(1, 4)} 
    for i in range(1, 4)
}
print(multiplication_table)
# Result: {1: {1: 1, 2: 2, 3: 3}, 
#          2: {1: 2, 2: 4, 3: 6}, 
#          3: {1: 3, 2: 6, 3: 9}}