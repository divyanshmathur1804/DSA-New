hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
if hours < 12:
    print("Time is in AM.")
elif hours == 12 and minutes == 0:
    print("Time is in PM.")
else:    print("Time is in PM.")