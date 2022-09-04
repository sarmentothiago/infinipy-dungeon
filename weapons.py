import tool

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