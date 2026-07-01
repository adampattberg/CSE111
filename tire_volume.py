print ("\n")
w = int(input("Enter the width of the tire in mm (ex 205): "))
ar = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))
v = (3.14159 * w ** 2 * ar * (w * ar + 2540 * d)) / 10000000000
print ("\n")
print (f"The approximate volume is {v} liters.")
from datetime import datetime
current_date_and_time = datetime.now()
print(f"{current_date_and_time:%Y-%m-%d}")
with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date_and_time}, {w}, {ar}, {d}, {v}", file=volumes_file)