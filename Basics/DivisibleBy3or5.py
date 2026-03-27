num = int(input("Enter a number: "))
sum = 0
if num%10 == 0 or num%10 == 5:
    print("The number is divisible by 5")
while num != 0:
    sum += num%10
    num = num//10
if sum%3 == 0:
    print("The number is divisible by 3")
