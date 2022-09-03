import weapons
import tool
import os
import races
import classes

class Player:

    CHARACTER_XP_LEVEL_UP = [0, 300, 900, 2_700,                    #lvl 1 2 3 4
                            6_500, 14_000, 23_000, 34_000,          #lvl 5 6 7 8
                            48_000, 64_000, 85_000, 100_000,        #lvl 9 10 11 12
                            120_000, 140_000, 165_000, 195_000,     #lvl 13 14 15 16
                            225_000, 265_000, 305_000, 355_000]     #lvl 17 18 19 20

    ABILITY_MODIFIERS = [-5, -4, -4, -3, -3,    #lvl 1 2 3 4 5 
                        -2, -2, -1, -1, 0,      #lvl 6 7 8 9 10
                        0, 1, 1, 2, 2,          #lvl 11 12 13 14 15
                        3, 3, 4, 4, 5,          #lvl 16 17 18 19 20
                        5, 6, 6, 7, 7,          #lvl 21 22 23 24 25
                        8, 8, 9, 9, 10]         #lvl 26 27 28 29 30

    RACES = ["Hill Dwarf","Montain Dwarf","High Elf",
            "Wood Elf","Drow Elf","Lightfoot Halfling","Stout Halfling"
            "Human","Dragonborn","Forest Gnome","Rock Gnome",
            "Half-Elf","Half-Orc","Tiefling"]

    ABILITIES = ["Strength","Dexterity",
                "Constitution","Intelligence",
                "Wisdom","Charisma"]

    SKILLS = ["Acrobatics","Animal Handling","Arcana",
            "Athletics","Deception","History",
            "Insight","Intimidation","Investigation",
            "Medicine","Nature","Perception",
            "Performance","Persuasion","Religion",
            "Sleight of Hands","Stealth","Survival"]

    NUMBER_OF_ABILITIES = 6
    NUMBER_OF_SKILLS = 18

    def __init__(self,sheet):
        self.sheet = sheet
        self.set_race()

    def set_race(self):
        if self.sheet["race"] == ("Hill Dwarf" or "Montain Dwarf"):
            subrace = self.sheet["race"]
            self.race = classes.Dwarf(subrace)

        elif self.sheet["race"] == ("High Elf" or "Wood Elf" or "Drow Elf"):
            subrace = self.sheet["race"]
            self.race = classes.Dwarf(subrace)

        elif self.sheet["race"] == ("Lightfoot Halfling" or "Stout Halfling"):
            subrace = self.sheet["race"]
            self.race = classes.Halfling(subrace)

        elif self.sheet["race"] == "Human":
            self.race = classes.Human()

        elif self.sheet["race"] == "Dragonborn":
            self.race = classes.Dragonborn()

        elif self.sheet["race"] == ("Forest Gnome" or "Rock Gnome"):
            self.race = classes.Gnome(subrace)

        elif self.sheet["race"] == "Half-Elf":
            self.race = classes.HalfElf()

        elif self.sheet["race"] == "Half-Orc":
            self.race = classes.HalfOrc()

        elif self.sheet["race"] == "Tiefling":
            self.race = classes.Tiefling()

    def skill_check(self,skill):
        race_bonus_score = self.race.skill_bonus.get(skill)
        bonus_score = self.use_skill_modifier(skill)
        return bonus_score + race_bonus_score

    def saving_throws(self,ability):
        race_bonus_score = self.race.abilities_bonus.get(ability)
        bonus_score = self.use_ability_modifier(ability)
        return bonus_score + race_bonus_score

    def update_ability(self,ability,value): #Update abilities
        self.sheet["abilities"][ability] = value
        return self.sheet["abilities"][ability]

    def use_ability_modifier(self,ability): #return ability modifier
        value = self.sheet["abilities"][ability] -1 #because array starts in 0 and level in 1
        return self.ABILITY_MODIFIERS[value]

    def use_skill_modifier(self,skill): #return ability modifier
        ability = self.sheet["skills"][skill]["ability"]
        value = self.use_ability_modifier(ability)
        return value