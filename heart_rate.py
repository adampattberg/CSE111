"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

print ("\n")
age = int(input("What is your age? "))
maxheartrate = 220 - age
maxworkingrate = maxheartrate * 0.85
minworkingrate = maxheartrate * 0.65
print ("\n")
print (f"When you exercise to strengthen your heart, you should keep your heart rate between {minworkingrate} and {maxworkingrate} beats per minute.")
print ("\n")