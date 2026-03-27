num = int(input("Enter a three-digit number: "))
digits = []
while num != 0:
    digits.append(num % 10)
    num //= 10

if(digits.index(max(digits)) == 1):
    print("The middle digit is the largest.")