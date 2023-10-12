data = [6, 5, 3, 7, 2, 4, 1]

print(sorted(data))

animals_list = ["cat", "dog", "cheetah", "rhino", "bear"]

print(sorted(animals_list, reverse=True))

animals = [
    {"type": "penguin", "name": "Stephanie", "age": 8},
    {"type": "elephant", "name": "Devon", "age": 3},
    {"type": "puma", "name": "Moe", "age": 5},
]

print(sorted(animals, key=lambda animal: animal["age"]))


def reverse_str(s: str) -> str:
    return s[::-1]


print(reverse_str("Paul"))
