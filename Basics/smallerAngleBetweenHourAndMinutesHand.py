hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))
if hour > 12 or minute > 60:
    print("Invalid input")
hour_angle = 30 * hour + 0.5 * minute
minute_angle = 6 * minute
angle = abs(hour_angle - minute_angle)
if angle > 180:
    angle = 360 - angle
print("The smaller angle between the hour and minute hand is: ", angle)