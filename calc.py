"""
A very basic calculator, limited to the 4 common operations.

Accepts 3 parameters

operation:string [add, subtract, multiply, divide]
num_1:int
num_2:int

return int
"""
def basic_calc(operation, num_1, num_2):
    match operation:
        case "multiply":
            return num_1 * num_2
        case "add":
            return num_1 + num_2
        case "subtract":
            return num_1 - num_2
        case "divide":
            if (num_1 == 0 or num_2 == 0):
                exit("Cannot divide by zero")
            return num_1 / num_2
        case _:
            return "Select an operation: add, subtract, multiply, divide"

print(basic_calc("add", 5, 10)) # 15
print(basic_calc("subtract", 5, 10)) # -5
print(basic_calc("multiply", 5, 10)) # 50
print(basic_calc("divide", 5, 10)) # 0.5