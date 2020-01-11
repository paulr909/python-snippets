import sys
 
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("Please tell me your name: ")
    if name == '': name = 'Monty'
  
