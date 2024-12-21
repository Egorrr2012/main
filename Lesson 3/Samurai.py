from Lesson_2.character import Character


class Samurai(Character):

    def __init__(self, name, health, damage, defence):
        super().__init__(name, health, damage, defence)
        self.damage_multiplier = 1.0
        self.max_multiplier = 1.5
        self.increment = 0.1
        self.attack_count = 0

    def attack(self, other):
        effective_damage = self.damage * self.damage_multiplier
        other.take_damage(effective_damage)

        if self.damage_multiplier < self.max_multiplier:
            self.damage_multiplier += self.increment
            self.attack_count += 1

        if self.attack_count >= 5:
            self.damage_multiplier = 1.0
            self.attack_count = 0

        print(f"{self.name} атакує {other.name} завдаючи {effective_damage:.1f} шкоди.")
        print(f"Множник шкоди: {self.damage_multiplier:.1f}")