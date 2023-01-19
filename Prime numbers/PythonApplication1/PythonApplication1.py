def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(2)) # True
print(is_prime(3)) # True
print(is_prime(4)) # False
