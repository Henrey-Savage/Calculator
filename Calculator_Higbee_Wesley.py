#Wesley Higbee
#CS480 Lab3
#10/29/2018
import math

def hasNum(s):
    return any(i.isdigit() for i in s)

variable = input("What mathematical function would you like me to calculate?")
    
if hasNum(input):
    output = eval(variable)
else:
    print("Your input had no digits, let's use digits.")
print(output)

