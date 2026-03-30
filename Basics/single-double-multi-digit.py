num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]
if len(digits) == 1:
    print("The number is a single-digit number.")
elif len(digits) == 2:
    print("The number is a double-digit number.")
else:
    print("The number is a multi-digit number.")