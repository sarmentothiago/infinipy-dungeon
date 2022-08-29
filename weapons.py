import tool

shortsword = {
            "name": "shortsword ",
            "dices": [6],
            "base damage": 2,
            "bonus damage": 0,
            "damage type": "piercing",
            "weight": 0,
            "attack range": 1.5
}

bare_hands = {
            "name": "bare hands",
            "dices": [1],
            "base damage": 0,
            "bonus damage": 0,
            "damage type": "bludgeoning",
            "weight": 0,
            "attack range": 1.5
            }

greatsword = {
            "name": "greatsword",
            "dices": [6,6],
            "base damage": 0,
            "bonus damage": 0,
            "damage type": "slashing",
            "weight": 4,
            "attack range": 1.5
            }

class Weapon:
    def __init__(self,equipment):
        self.name = equipment.get("name")
        self.base_damage = equipment.get("base damage")
        self.bonus = equipment.get("bonus damage")
        self.damage_dice = tool.Dice(equipment.get("dices"))
        self.range = equipment.get("attack range")
        
    def damage(self):
        self.damage_dice.roll()
        damage = self.base_damage + self.bonus + self.damage_dice.get_roll_result()
        return damage