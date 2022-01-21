# """
# A very basic calculator, limited to the 4 common operations.

# Accepts 3 parameters

# operation:string [add, subtract, multiply, divide]
# num_1:int
# num_2:int

# return int
# """
# def basic_calc(operation, num_1, num_2):
#     match operation:
#         case "multiply":
#             return num_1 * num_2
#         case "add":
#             return num_1 + num_2
#         case "subtract":
#             return num_1 - num_2
#         case "divide":
#             if (num_1 == 0 or num_2 == 0):
#                 exit("Cannot divide by zero")
#             return num_1 / num_2
#         case _:
#             return "Select an operation: add, subtract, multiply, divide"

# # print(basic_calc("add", 5, 10))

# def get_customer_details(accnum):
#     return {
#         "name": "Bear Jordan",
#         "account_number": 89465191656,
#         "sort_code": 123813,
#         "cash": 0.01
#     }

# def has_the_cash(amount, accnum):
#     customer = get_customer_details(accnum)
#     return amount > customer['cash']

# def cash_withdrawal(amount, accnum):
#     if has_the_cash(amount, accnum):
#         print(f"Withdrawing £{amount} from account {accnum}")
#     else:
#         print("You don't have enough cash")

# # cash_withdrawal(100, 591261959)

# def take_order(size, type):
#     a_an = "an" if size[0].lower() in "aeiou" else "a"
#     print(f"You've ordered {a_an} {size} {type}")

# take_order("small", "espresso")
# take_order("medium", "cappuccino")
# take_order("large", "coffee")
# take_order("extra-large", "super caffeine deluxe")

# def convert_temp(to, temp):
#     if to == "f":
#         return temp / 5 * 9 + 32
#     elif to == "c":
#         return (temp - 32) * 5 / 9

# celcius = 0;
# fahrenheit = 42
# print(f"{celcius}C to F: {convert_temp('f', celcius)}")
# print(f"{fahrenheit}F to C: {convert_temp('c', fahrenheit)}")


