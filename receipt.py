import csv
from datetime import datetime

def read_products(filename):
    products_dict = {}

    with open(filename, "rt", newline="") as products_file:
        reader = csv.reader(products_file)

        next(reader)  # Skip the header row

        for row in reader:
            product_number = row[0]
            products_dict[product_number] = row

    return products_dict

def process_request(filename, products_dict):
    subtotal = 0
    total_items = 0

    with open(filename, "rt", newline="") as request_file:
        reader = csv.reader(request_file)

        next(reader)

        for row in reader:
            product_number = row[0]
            quantity = int(row[1])

            product = products_dict[product_number]

            name = product[1]
            price = float(product[2])

            print(f"{name}: {quantity} @ ${price:.2f}")

            total_items += quantity
            subtotal += quantity * price

    return total_items, subtotal

def main():
    try:
        products_dict = read_products("products.csv")

        print("Inkom Emporium")
        print("-" * 30)

        total_items, subtotal = process_request("request.csv", products_dict)

        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        print()
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")

        print()
        print("Thank you for shopping at the Inkom Emporium.")

        current_date = datetime.now()
        print(current_date.strftime("%a %b %d %I:%M:%S %p %Y"))

    except FileNotFoundError:
        print("Error: One of the data files could not be found.")

    except KeyError as error:
        print(f"Error: unknown product ID {error.args[0]}.")

if __name__ == "__main__":
    main()