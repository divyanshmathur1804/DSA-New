def is_prime(n):
    if n < 2:
        return False
    if n%2 == 0:
        return False
    for i in (2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    
    return True

num = int(input("Enter a number: "))
if num == 2: print("is prime")
else: print(is_prime(num))

