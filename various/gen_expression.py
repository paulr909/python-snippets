import sys

# Saves memory compared to list comprehension
print(sum((i * i for i in range(1, 1001))))


squares_generator = (i * i for i in range(5))

for i in squares_generator:
    print(i)

# Profiling performance
nums_squared_lc = [i**2 for i in range(10000)]
print("List comprehension size in bytes:", sys.getsizeof(nums_squared_lc))

nums_squared_gc = (i**2 for i in range(10000))
print("Generator expression size in bytes:", sys.getsizeof(nums_squared_gc))
