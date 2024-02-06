first_number = float(input("Enter the first number: "))
action = input("Enter an action (+, -, *, /): ")
second_number = float(input("Enter the second number: "))
if action == "+":
    result = first_number + second_number
    print(f"The result is {result}")
elif action == "-":
    result = first_number - second_number
    print(f"The result is {result}")
elif action == "*":
    result = first_number * second_number
    print(f"The result is {result}")
elif action == "/" and second_number == 0:
    print("Division by zero!")
elif action == "/" and second_number != 0:
    result = first_number / second_number
    print(f"The result is {result}")
