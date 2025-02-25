def calculator():
    while True:  
        print("\nSimple Calculator")
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")  

        try:
            choice = int(input("Enter your choice (1/2/3/4/5): "))
            
            if choice == 5:  
                print("Exiting the calculator. Goodbye!")
                break 

            if choice not in [1, 2, 3, 4]:  
                print("Invalid input! Try again (1/2/3/4/5).")
                continue  

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            match choice:
                case 1:
                    print(f"Result: {num1} + {num2} = {num1 + num2}")
                case 2:
                    print(f"Result: {num1} - {num2} = {num1 - num2}")
                case 3:
                    print(f"Result: {num1} * {num2} = {num1 * num2}")
                case 4:
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                    else:
                        print(f"Result: {num1} / {num2} = {num1 / num2}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

calculator()
