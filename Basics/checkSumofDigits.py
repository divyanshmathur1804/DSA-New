num = int(input("Enter a three-digit number: "))
digits = [int(d) for d in str(num)]
if(digits[0] + digits[2] == digits[1]):
    print("The sum of the first and last digit is equal to the middle digit.")
else:
    print("The sum of the first and last digit is not equal to the middle digit.")