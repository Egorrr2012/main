import random

class Person:
    def __init__(self, name, health=100, mood=100, money=0.0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return (f"=== {self.name} ===\n"
                f"Здоров'я: {self.health}\n"
                f"Настрій: {self.mood}\n"
                f"Капітал: {self.money}")

    def change_state(self, health=0, mood=0, money=0):
        self.health += health
        self.mood += mood
        self.money += money

        if self.health < 0:
            raise Exception("Людина померла.")
        if self.mood < 0:
            raise Exception("Людина впала в депресію.")
        if self.money < 0:
            raise Exception("Людина збанкрутувала.")

    def do(self, action):
        if isinstance(action, Action):

            health = action.health if action.health is not None else 0
            mood = action.mood if action.mood is not None else 0
            money = action.money if action.money is not None else 0

            if isinstance(action, Work):
                money_increase = money
                if self.mood > 90:
                    money_increase *= 1.1
                self.change_state(health=health, mood=mood, money=money_increase)
            elif isinstance(action, Rest):
                mood_increase = mood
                if self.health < 40:
                    mood_increase *= 0.8
                self.change_state(health=health, mood=mood_increase, money=money)
            else:
                self.change_state(health=health, mood=mood, money=money)

class Action:
    def __init__(self, name, health=0, mood=0, money=0.0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

class Work(Action):
    pass

class Rest(Action):
    pass

people = [
    Person(name='Олег', health=100, mood=100, money=50),
    Person(name='Вікторія', health=80, mood=90, money=70),
    Person(name='Петро', health=120, mood=85, money=30)
]

actions = [
    Work(name='Піти на завод', health=-10, mood=-20, money=100),
    Rest(name='Сходити в парк', health=15, mood=30, money=-10),
    Action(name='Підти в лікарню', health=20, mood=-5, money=-20)
]

while people:
    for person in people[:]:
        try:
            action = random.choice(actions)
            print(f"{person.name} виконує дію: {action.name}")
            person.do(action)
            print(person)
        except Exception as e:
            print(f"{person.name} випав з гри: {e}")
            people.remove(person)

    if not people:
        print("Гра завершена. Дякую за гру!")
        break

