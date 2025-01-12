def perform_operation():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    match operation:
        case "add":
            print("Result :", num1 + num2)
        case "subtract":
            print("Result :", num1 - num2)
        case "multiply":
            print("Result :", num1 * num2)
        case "divide":
            if num2 == int("0"):
                print("Cannot divide by zero.")
            else:
                print("Reslt :", num1 / num2)
perform_operation()