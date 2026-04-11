num = int(input("Enter a number: "))
sum_num = 0
temp = num
while temp >0:
    digit = temp % 10
    sum_num += digit ** 3
    temp //= 10
if num == sum_num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")