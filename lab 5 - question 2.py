#James adebayo
#Lab 5
#Question 2

print("vending machine menu booting...")
def main():
    item ={
        1: ("chip", 2.49),
        2: ("cookies", 4.58),
        3: ("chocolate bar", 3.89),
        4: ("water", 1.99),
        5: ("pop", 2.25),
    }

    subtotal = menu(item)

    tax_amount = tax_calculation(subtotal)
    total_after_tax = subtotal + tax_amount
    print(f"Tax: ${tax_amount:.2f}")
    print(f"Total after tax: ${total_after_tax:.2f}")

def menu(item):
    subtotal = 0
    selection = 0

    while selection != 6:
        print("\nPlease select from the option below")
        for key, value in item.items():
            print(f"{key}) {value[0]} - ${value[1]:.2f}")
        print("6) Exit and pay")
        print(f"current total: ${subtotal:.2f}")

        try:
            selection = int(input("Enter option number: "))

            if selection == 6:
                print("VEND: Exiting menu ...")
                break
            elif selection in item:
                item_name, item_price = item[selection]
                print(f"you have selected {item_name}\n")
                subtotal += item_price
            else:
                print("ERROR: Invalid selection")
        except ValueError:
            print("ERROR: Invalid selection")

    return subtotal

def tax_calculation(price):
    tax_rate = 0.1
    return price * tax_rate

if __name__ == "__main__":
    main()