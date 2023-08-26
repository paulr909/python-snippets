# dirty dishes in the sink
sink = ["bowl", "plate", "cup"]

for dish in list(sink):
    print(f"Putting {dish} in the dishwasher")
    sink.remove(dish)

# check that the sink is empty
print(sink)
