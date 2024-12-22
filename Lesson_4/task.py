def get_valid_number(prompt):
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            print("Помилка: введене значення не є числом. Спробуйте ще раз.")

if __name__ == "__main__":
    result = get_valid_number("Введіть число: ")
    print(f"Ви ввели число: {result}")
