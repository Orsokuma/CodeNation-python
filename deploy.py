# Activity 1
for i in range(13):
    print(f"{i}. Hello world")

num = 0
while num < 13:
    num += 1
    print(f"{num}. Hello world")

# Activity 2
import random
for i in range(6):
    rand_num = random.randint(1, 30)
    is_div = 'is' if rand_num % 7 == 0 else 'isn\'t'
    print(f"{rand_num} {is_div} divisible by 7")

# Activity 3
import random
cards = [
    'Diamond',
    'Spade',
    'Club',
    'Heart'
]
card = ''
cnt = 0
while card != 'Diamond':
    cnt += 1
    card = random.choice(cards)
    print(f"#{cnt} · Card suite: {card}")

# Activity 4
def multiplication_table(table):
    cnt = 0
    while cnt < 12:
        cnt += 1
        print(f"{cnt} x {table} = {cnt * table}")

table = input("Which multiplication table would you like?\n")
multiplication_table(int(table))

# Activity 5
def is_prime(n):
    import math
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

for i in range(1, 21):
    is_a_prime_number = 'IS' if is_prime(i) else 'is NOT'
    print(f"{i} {is_a_prime_number} a prime number")