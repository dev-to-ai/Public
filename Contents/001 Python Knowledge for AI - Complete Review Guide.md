# 001 Python Knowledge for AI – Complete Review Guide

A complete, AI-focused Python review syllabus designed specifically for ML, Deep Learning, RAG, and production AI systems — not generic Python.

This is what senior AI engineers actually know.

---

## 1. Python Data Structures (Used Constantly in AI)

### 1.1 Lists

A list is a built-in data structure used to store multiple items in a single variable.

**Lists are:**
- Ordered (index starts at `0`)
- Mutable (items can be changed)
- Able to contain different data types
- Able to contain nested lists
- Written using square brackets `[]`
- Allow duplicate values
- Items are separated by commas

**List comprehension** can be used to create a new list from an existing list in a single line.

All code examples are in `001.1Lists.py`.

---

#### AI Rule

> Lists are temporary. Convert to NumPy or Torch as soon as possible.

---

### 1.2 Tuples

A tuple is:
- An ordered collection of values
- Immutable (cannot be changed after creation)
- Often used to represent a record (a fixed set of related values)

Think of a tuple like a **sealed box**: once you put items in and seal it, you can’t change them.

**Use tuples when:**
- Data should not change
- You want safety and clarity
- Representing records or coordinates
- Returning multiple values from functions
- Using data as dictionary keys

#### Key Takeaways

- Tuples are immutable, ordered collections
- Best for fixed, structured data
- Support unpacking, slicing, and indexing
- Safer than lists for records
- Ideal for function returns and dictionary keys

All code examples are in `001.2Tuples.py`.

### 1.3 Dictionaries
A dictionary is a data structure that stores data as key–value pairs.
Keys → identifiers (usually strings, numbers, tuples)
Values → any data type (numbers, lists, models, tensors, etc.)
Access is O(1) on average → very fast lookup

Why Dictionaries Are Core to AI Systems

AI systems constantly need to:
Map inputs → outputs
Store features → values
Track parameters → weights
Count tokens → frequencies
Cache results → predictions
Dictionaries do all of this efficiently.