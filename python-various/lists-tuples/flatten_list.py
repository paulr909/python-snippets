dishwasher = [
    ["bowl", "cup", "plate", "cup"],
    [
        "knife",
        "fork",
        "spoon",
        "fork",
        "spoon",
        "knife",
        "fork",
        "spoon",
        "knife",
    ],
    ["plate", "bowl", "cup", "plate", "bowl", "plate", "cup"],
]

flatten_list = [item for sub_list in dishwasher for item in sub_list]

print(flatten_list)

# print(sorted(flatten_list, reverse=True))
