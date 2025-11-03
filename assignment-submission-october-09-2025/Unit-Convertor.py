# Unit Converter Program

def unit_converter():
    print("Welcome to the Unit Converter!")
    print("Supported conversions:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("Type 'exit' to quit.\n")

    while True:
        choice = input("Enter conversion number (1-6): ")
        if choice.lower() == 'exit':
            print("Goodbye!")
            break
        
        if choice not in ['1','2','3','4','5','6']:
            print("Invalid choice. Try again.\n")
            continue

        try:
            value = float(input("Enter value to convert: "))
        except ValueError:
            print("Invalid number. Try again.\n")
            continue

        if choice == '1':
            print(f"{value} km = {value * 0.621371:.2f} miles\n")
        elif choice == '2':
            print(f"{value} miles = {value / 0.621371:.2f} km\n")
        elif choice == '3':
            print(f"{value}°C = {(value * 9/5) + 32:.2f}°F\n")
        elif choice == '4':
            print(f"{value}°F = {(value - 32) * 5/9:.2f}°C\n")
        elif choice == '5':
            print(f"{value} kg = {value * 2.20462:.2f} lbs\n")
        elif choice == '6':
            print(f"{value} lbs = {value / 2.20462:.2f} kg\n")

# Run it
unit_converter()
