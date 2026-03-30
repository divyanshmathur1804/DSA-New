num = int(input("Enter a digit (0-9): "))
num_dict = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

print(num_dict.get(num, "Invalid input! Please enter a digit between 0 and 9."))