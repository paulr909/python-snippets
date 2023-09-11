tree = {
    "a": "Value of a",
    "b": {"b1": "Value of b1", "b2": "Value of b2"},
    "c": {
        "c1": "Value of c1",
        "c2": {
            "c21": "Value of c21",
            "c22": "Value of c22",
        },
    },
}


def print_tree(tree, prefix=""):
    for key, value in tree.items():
        line = f"{prefix}+-- {key}"
        if isinstance(value, dict):
            print(line)
            print_tree(
                value,
                prefix=prefix + "|   ",
            )
        else:
            print(f"{line}: {value}")


print_tree(tree)
