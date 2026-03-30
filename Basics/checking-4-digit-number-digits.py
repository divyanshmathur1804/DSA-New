num = int(input("Enter a four-digit number: "))
digits = [int(d) for d in str(num)] # Convert the number to a list of its digits by converting it to a string and then back to integers
if (digits[0] == digits[len(digits) - 1]):
    print("The first and last digits are the same.")
else:    print("The first and last digits are different.")