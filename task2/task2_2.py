
number = int(input("Enter a four-digit number: "))

if 1000 <= number <= 9999:

    thousands_digit = number // 1000
    hundreds_digit = (number % 1000) // 100
    tens_digit = (number % 100) // 10
    ones_digit = number % 10

    print("TThe digit in the thousands position is:", thousands_digit)
    print("The number in the hundreds position is:", hundreds_digit)
    print("The digit in the tens position is:", tens_digit)
    print("The digit in the position of units is:", ones_digit)
else:
    print("Please enter a valid four-digit number.")
