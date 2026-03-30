num = int(input("Enter a number: "))
divisor = 2
while divisor * divisor < num:
    divisor += 1
if divisor * divisor == num:
    print(num, "is a perfect square.")
else:    print(num, "is not a perfect square.")


# better way to check perfect square
sqrt = int(num ** 0.5)
if sqrt * sqrt == num:
    print(num, "is a perfect square.")
else:
    print(num, "is not a perfect square.")