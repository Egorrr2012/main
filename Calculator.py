def calculator():

    try:
        a = float(input("Введіть перше число (a): "))
        b = float(input("Введіть друге число (b): "))

        operation = input("Виберіть операцію (+, -, *, /): ")

        if operation == "+":
            result = a + b
            print(f"Результат: {a} + {b} = {result}")
        elif operation == "-":
            result = a - b
            print(f"Результат: {a} - {b} = {result}")
        elif operation == "*":
            result = a * b
            print(f"Результат: {a} * {b} = {result}")
        elif operation == "/":
            if b == 0:
                print("Помилка: Ділення на нуль.")
            else:
                result = a / b
                print(f"Результат: {a} / {b} = {result}")
        else:
            print("Некоректна операція. Виберіть одну з (+, -, *, /).")
    except ValueError:
        print("Помилка: Введіть коректні числа.")


calculator()
