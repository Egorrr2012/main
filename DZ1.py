def determine_grade(score):
    if score < 0 or score > 100:
        return "Некоректний бал. Введіть число від 0 до 100."
    elif score < 50:
        return "Незадовільно"
    elif score < 70:
        return "Задовільно"
    elif score < 90:
        return "Добре"
    else:
        return "Відмінно"

try:
    score = int(input("Введіть кількість балів (0-100): "))
    grade = determine_grade(score)
    print(f"Оцінка: {grade}")
except ValueError:
    print("Введіть ціле число від 0 до 100.")