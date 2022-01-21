def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


for i in range(1, 21):
    is_a_prime_number = 'IS' if is_prime(i) else 'is NOT'
    print(f"{i} {is_a_prime_number} a prime number")