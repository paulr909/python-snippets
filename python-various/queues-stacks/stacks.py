""" A stack of bills to pay """

# create a list to use as the stack
stack = list()

# add some bills to the stack
stack.append("bill1")
stack.append("bill2")

# remove the top bill to pay it
print(stack.pop())

# add two more bills to the stack
stack.append("bill3")
stack.append("bill4")

# remove bills from top to bottom
print(stack.pop())
print(stack.pop())
print(stack.pop())
# stack.pop()  # causes Index error exception
