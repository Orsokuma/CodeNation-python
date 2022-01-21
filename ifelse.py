# Activity 1 and 1.5?
age = 31
country = "UK"
if age >= 18 and country.lower() == "uk":
    print("You're old enough")
elif age >= 18 and country.lower() != "uk":
    print("Unknown location")
else:
    print("Got any ID? No? Your problem")

# Challenge 1
password = "totallySecurePassword123!"
if len(password) >= 8:
    print(password)
else:
    exit("Password too short")

# Challenge 2
num = 10
if num % 3 == 0 or num % 5 == 0:
    print("This number is divisible by 3 or 5")
else:
    print("This number is not divisible by 3 or 5")


# Challenge 3
num = 6
if num % 3 == 0 and num % 7 == 0:
    print("fizz buzz")
elif num % 7 == 0:
    print("buzz")
elif num % 3 == 0:
    print("fizz")
else:
    print(num)

# Challenge 4
word = "asda"
first = word[0]
last = word[-1];
if first.lower() == last.lower():
    print(True)
else:
    print(False)

# Challenge 5
time = 5
place_of_work = "KumaDesk"
town_of_home = "Cybercity"

if time >= 6 and time <= 16:
    print("I'm in", place_of_work)
elif time > 16 and time <= 20:
    print("I'm in", town_of_home)
else:
    print("I'm nowhere")

# Challenge 6
num1 = 1
num2 = 3
added = num1 + num2
if added % 2 == 0:
    print(f"The sum of {num1} and {num2} ({added}) is even")
else:
    print(f"The sum of {num1} and {num2} ({added}) is odd")

# Challenge 7
num = 1001001
if str(num) == str(num)[::-1]:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")

# Challenge 8
str = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"
last_vowel = [letter for letter in str if letter in "aeiou"][-1]
print(last_vowel, ":", str.rfind(last_vowel))
