num = int(input("Enter a three-digit number: "))
firstdigit = num%10
num = num//10
flag = True
while num!= 0:
    if num%10 != firstdigit:
        flag = False
        break
    else:
        num = num//10

if flag:
    print("All digits are the same.")
else:    print("All digits are not the same.")


# better solution
num = int(input("Enter a three-digit number: "))
digits = set()
while num != 0:
    digits.add(num % 10)
    num = num // 10

if len(digits) == 1:
    print("All digits are the same.")
else:    print("All digits are not the same.")