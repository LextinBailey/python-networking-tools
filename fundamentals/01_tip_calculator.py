while True:
    try:
        bill = float(input("Enter bill amount: "))

        if bill <= 0:
            print("Bill must be greater than 0.")
            continue

        break
    
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        tip_percent = float(input("Enter tip percentage (e.g. 15): "))

        if tip_percent < 0 or tip_percent > 100:
            print("Tip must be between 0 and 100.")
            continue

        break

    except ValueError:
        print("Invalid input. Please enter a number.")

def calculate_tip(bill, tip_percent):
    tip_decimal = tip_percent / 100
    tip_amount = bill * tip_decimal
    total = bill + tip_amount
    return tip_amount, total

tip_amount, total = calculate_tip(bill, tip_percent)

print(f"\nTip amount: ${tip_amount:.2f}")
print(f"Total bill: ${total:.2f}")

