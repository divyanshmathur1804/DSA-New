# prime numbers after 3 can be expressed as 6n +- 1
#If a number num has a factor, it must appear in a pair:

# Example:

# 36 → (1×36), (2×18), (3×12), (4×9), (6×6)

# Notice:

# After √36 = 6, the pairs repeat

# 👉 So:

# If no number ≤ √num divides it
# Then no number > √num will either
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [2,3]
n= 1
while 6*n < 100:
    for candidate in [(6*n)-1, (6*n)+1]:
        if is_prime(candidate):
            prime_numbers.append(candidate)
    n += 1

print(prime_numbers)


