def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def user_inputs():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))  
    return num1, num2

def main():
    print("options.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.View previous calculations")
    print("0.Turn off the calculator")

    history = {}

    while True:
        choice = input("Enter choice(1,2,3,4,5,0): ")
        if choice in ('1', '2', '3', '4', '5', '0'):
            if choice == '0':
                # Loop condition -> False:
                print("The calculator's been turned off.")
                break
            else:
                if choice == '1':
                    num1, num2 = user_inputs()
                    key = str(num1) + " + " + str(num2)
                    value = add(num1, num2)
                    history[key] = value
                    print(num1, "+", num2, "=", value)

                elif choice == '2':
                    num1, num2 = user_inputs()
                    key = str(num1) + " - " + str(num2)
                    value = subtract(num1, num2)
                    history[key] = value
                    print(num1, "-", num2, "=", value)

                elif choice == '3':
                    num1, num2 = user_inputs()
                    key = str(num1) + " x " + str(num2)
                    value = multiply(num1, num2)
                    history[key] = value
                    print(num1, "*", num2, "=", value)

                elif choice == '4':
                    num1, num2 = user_inputs()
                    key = str(num1) + " / " + str(num2)
                    value = divide(num1, num2)
                    history[key] = value
                    print(num1, "/", num2, "=", value)

                elif choice == '5':
                    for (k, v) in history.items():
                        print(k, "=", v)
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()