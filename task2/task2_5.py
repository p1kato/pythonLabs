try:

    num1 = float(input("Please type the first number: "))
    num2 = float(input("Please type the second number: "))

    operation = input("Please choose the operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':

        if num2 == 0:
            print("Error: Division by zero")
        else:
            result = num1 / num2
    else:
        print("Invalid operation choice")

    if 'result' in locals():
        print(f"{num1} {operation} {num2} = {result:.3f}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
except Exception as e:
    print(f"An error occurred: {e}")
