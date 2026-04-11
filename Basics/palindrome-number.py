num = int(input("Enter a number: "))
i = 0
nom_str = str(num)
j = len(nom_str) - 1
while i < j:
    if nom_str[i] != nom_str[j]:
        print("Not a palindrome")
        break
    i += 1
    j -= 1
else:
    print("Palindrome")