amount = int(input("Enter the amount: "))
num_2000 = amount // 2000
amount = amount % 2000
num_500 = amount // 500
amount = amount % 500
nums_100 = amount // 100
amount = amount % 100
print("Number of 2000 notes:", num_2000)
print("Number of 500 notes:", num_500)
print("Number of 100 notes:", nums_100)
if amount > 0:
    print("full amount cannot be divided into 2000, 500 and 100 notes. Remaining amount:", amount)