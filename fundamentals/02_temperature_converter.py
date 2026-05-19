while True:
    try:
        temp = float(input("Enter temperature value: "))
        
        break

    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    unit = input("Enter unit (C, F, K): ").lower()

    if unit in ["c", "f", "k"]:
        break
    
    else:
        print("Invalid unit. Please enter C, F, or K.")

def convert_temperature(temp, unit):
    if unit == "c":
        c = temp
        f = (temp * 9/5) + 32
        k = temp + 273.15

    elif unit == "f":
        c = (temp - 32) * 5/9
        f = temp
        k = c + 273.15

    elif unit == "k":
        c = temp - 273.15
        f = (c * 9/5) + 32
        k = temp

    return c, f, k

c, f, k = convert_temperature(temp, unit)

print(f"\nConverted Temperatures:")
print(f"Celsius: {c:.2f}°C")
print(f"Fahrenheit: {f:.2f}°F")
print(f"Kelvin: {k:.2f}K")