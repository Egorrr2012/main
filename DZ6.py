result = []

def divider(a, b):
    if a < b:
        raise ValueError("'a' повинно бути більше або дорівнювати 'b'.")
    if b > 100:
        raise IndexError("'b' повинно бути меншим або дорівнювати 100.")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        a = int(key)
        b = data[key]

        res = divider(a, b)
        result.append(res)

    except Exception as e:
        print(f"Помилка: {type.__name__} для ключа={key}, значення={data[key]}: {e}")

print("Результат:", result)