n = int(input("enter a number"))
series = [0,1]
x = 0
y = 1
for i in range(2,n):
    z = x+y
    series.append(z)
    x = y
    y = z
print(series)
sum_num = sum(series)
print("sum of the series is",sum_num)