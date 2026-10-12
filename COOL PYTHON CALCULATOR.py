import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def floor_divide(a, b):
    return a // b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_menu():
    print("\nCOOL PYTHON CALCULATOR\n")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor division (//)")
    print("6. Modulus (%)")
    print("7. Exponentiation (**)")
    print("8. Square root")
    print("9. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "9":
            print("Thank you for using the calculator!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6", "7", "8"):
            print("Invalid choice. Please select a number from 1 to 9.")
            continue

        if choice == "8":
            number = get_number("Enter a number: ")
            if number < 0:
                print("Square root of a negative number is not supported.")
            else:
                print("Result:", math.sqrt(number))
            continue

        first = get_number("Enter the first number: ")
        second = get_number("Enter the second number: ")

        try:
            if choice == "1":
                result = add(first, second)
            elif choice == "2":
                result = subtract(first, second)
            elif choice == "3":
                result = multiply(first, second)
            elif choice == "4":
                result = divide(first, second)
            elif choice == "5":
                result = floor_divide(first, second)
            elif choice == "6":
                result = modulus(first, second)
            else:
                result = power(first, second)

            print("Result:", result)
        except ZeroDivisionError:
            print("Error: division by zero is not allowed.")
        except OverflowError:
            print("Error: the result is too large to calculate.")


if __name__ == "__main__":
    main()
