def calculator():
    print("Welcome to the Python Calculator!")
    print("You can perform +, -, *, /, //, %, ** operations.")
    print("Type 'exit' anytime to quit.\n")

    while True:
        num1 = input("Enter first number: ")
        if num1.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            num1 = float(num1)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        operator = input("Enter operator (+, -, *, /, //, %, **): ")
        if operator.lower() == 'exit':
            print("Goodbye!")
            break

        num2 = input("Enter second number: ")
        if num2.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            elif operator == '//':
                result = num1 // num2
            elif operator == '%':
                result = num1 % num2
            elif operator == '**':
                result = num1 ** num2
            else:
                print("Invalid operator. Try again.")
                continue

            print(f"Result: {result}\n")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.\n")

calculator()
