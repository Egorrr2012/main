from Lesson_2.character import Character


class Berserk(Character):
    #На скільки треба збільшити шкоду при низькому здоров'ї
    damage_multiplier = 1.5
    rage_limit = 50

    def __init__(self, name, health=100, damage=5, defence=0, damage_multiplier=1.5, rage_limit=50):
        Character.__init__(self, name, health, damage, defence)
        self.damage_multiplier = damage_multiplier
        self.rage_limit = rage_limit

    def attack(self, target):
        final_damage = self.damage * self.damage_multiplier \
            if self.health < self.rage_limit else self.damage
        return target.take_damage(final_damage)