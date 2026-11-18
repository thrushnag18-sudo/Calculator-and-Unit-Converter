#Addition function
def add(a, b):
    return a + b

# Subtraction function
def subtract(a, b):
    return a - b

# Multiplication function
def multiply(a, b):
    return a * b

# Division function
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
conversion_factors = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462
}
#Input validation
def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
#calculator menu
def calculator():
    print("===== CALCULATOR ====")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice = input("Enter your choice (1-4): ")

    num1 = read_number("Enter first number: ")
    num2 = read_number("Enter second number: ")    
    if choice == "1":
            print("Result:",add(num1,num2))
    elif choice == "2":
            print("Result:", subtract(num1,num2))
    elif choice == "3":
            print("Result:", multiply(num1,num2))
    elif choice == "4":
                print("Result:",divide(num1,num2))
                        
                
    else:
            print("Invalid choice") 
def km_to_metres(value):
    return value * 1000

def metres_to_km(value):
    return value / 1000

def celsius_to_fahrenheit(value):
    return (value * 9/5) + 32

def fahrenheit_to_celsius(value):
    return (value - 32) * 5/9

def km_to_miles(value):
    return value * conversion_factors["km_to_miles"]

def kg_to_pounds(value):
    return value * conversion_factors["kg_to_pounds"]
def unit_converter():
        print("\n===== UNIT CONVERTER =====")
        print("1. Kilometres to Metres")
        print("2. Metres to Kilometres")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. Kilometres to Miles")
        print("6.Kilograms to pounds")

        unit_choice = input("Enter your choice (1-6): ")
        value = read_number("Enter the value: ")

        if unit_choice == "1":
                        print("Result:", km_to_metres(value))
        elif unit_choice == "2":
                        print("Result:", metres_to_km(value))
        elif unit_choice == "3":
                        print("Result:",celsius_to_fahrenheit(value))
        elif unit_choice == "4":
                        print("Result:", fahrenheit_to_celsius(value))
        elif unit_choice == "5":
                       print("Result:", km_to_miles(value))
        elif unit_choice == "6":
                        print("Result:", kg_to_pounds(value))
        else: 
                print("Invalid choice") 
def currency_converter():
    amount = read_number("Enter amount in USD: ")
    rate = read_number("Enter USD to INR rate: ")
    print("Result in INR:", round(amount * rate, 2))
def main():
        while True:
                print("\n==== MAIN MENU ====")
                print("1. Calculator")
                print("2. Unit Converter")
                print("3. Currency Converter")
                print("4. Exit")

                choice = input("Enter your choice (1-4): ")

                if choice == "1":
                   calculator()
                elif choice == "2":
                   unit_converter()
                elif choice == "3":
                   currency_converter()
                elif choice == "4":
                    print("Thank you for using our program!")
                    break
                else:
                        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()