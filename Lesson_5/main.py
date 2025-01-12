import requests

def get_cat_facts():
    lang = input("Введіть мову (ukr, eng): ")
    while lang not in ['ukr', 'eng']:
        print("Такої мови немає. Виберіть 'ukr' або 'eng'.")
        lang = input("Введіть мову (ukr, eng): ")

    try:
        count = int(input("Введіть кількість фактів: "))
        if count <= 0:
            raise ValueError("Кількість фактів має бути більше нуля.")
    except ValueError as e:
        print(f"Помилка: {e}. Будь ласка, введіть правильне число.")
        return

    url = "https://meowfacts.herokuapp.com/"

    response = requests.get(url=url, params={
        'lang': lang,
        'count': count
    })

    if response.ok:
        as_json = response.json()
        facts = as_json['data']

        print(f'Рандомні факти про котів ({lang}):')
        for fact in facts:
            print(f' - {fact}')
    else:
        print(f'Помилка запиту: {response.status_code}')

if __name__ == "__main__":
    get_cat_facts()

