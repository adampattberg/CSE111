dis_rate = 0.1
tax = 0.06
subtotal = float(input("Please enter the subtotal: "))
from datetime import datetime
current_date_and_time = datetime.now()
weekday = current_date_and_time.weekday()
if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal * dis_rate, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount
sales_tax = round(subtotal * tax, 2)
print (f"Sales tax amount: {sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: {total:.2f}")