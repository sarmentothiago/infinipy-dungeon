import models

class Race:
    def __init__(self):
        self.abilities_bonus = {}
        self.skills_bonus = {}
        self.proficiency = []
        self.language = ["Common"]
        self.resistance = []
        self.advantage = []
        self.imunity = []
    
    def skill_check(self,skill):
        if self.skills_bonus.has_key(skill):
            score = self.skills_bonus.get(skill)
            return score
        else:
            return 0

    def ability_check(self,ability):
        if self.abilities_bonus.has_key(ability):
            score = self.abilities_bonus.get(ability)
            return score
        else:
            return 0

    def use_ability_modifier(self,ability):
        value = self.abilities_bonus[ability]
        return value

    def use_skill_modifier(self,skill):
        value = self.skills_bonus[skill]["bonus"]
        return value

    def level_up(self):
        pass

    def race_attack(self):
        pass

    def race_proficiency(self):
        pass

    def race_language(self):
        pass

class Dwarf(Race):
    def __init__(self,subrace):
        super().__init__()
        self.size =                 "Medium"
        self.speed =                25
        self.vision = {
            "Bright light":         60,
            "Dim light":            60,
            "Darkness":             60
        }
        self.advantage =            ["Poison"]
        self.resistance =           ["Poison"]
        self.proficiency +=         models.DWARF_PROFICIENCY

        if subrace == "Hill Dwarf":
            self.abilities_bonus =  models.DWARF_HILL_SUBRACE_ABILITY_BONUS
        elif subrace == "Montain Dwarf":
            self.proficiency +=     models.DWARF_MONTAIN_SUBRACE_PROFICIENCY
            self.abilities_bonus =  models.DWARF_MONTAIN_SUBRACE_ABILITY_BONUS
        
        self.language +=            models.DWARF_LANGUAGE

        def level_up(self,character):
            if character.sheet["race"] == "Hill Dwarf":
                character.sheet["hp"] += 1
            else:
                pass

class Elf(Race):
    def __init__(self,subrace):
        super().__init__()
        self.proficiency +=         models.ELF_PROFICIENCY
        self.language +=            models.ELF_LANGUAGE
        
        if subrace == "High Elf":
            self.proficiency +=     models.ELF_HIGH_SUBRACE_PROFICIENCY
            self.abilities_bonus =  models.ELF_HIGH_SUBRACE_ABILITY_BONUS
        elif subrace == "Wood Elf":
            self.proficiency +=     models.ELF_WOOD_SUBRACE_PROFICIENCY
            self.abilities_bonus =  models.ELF_WOOD_SUBRACE_ABILITY_BONUS
        elif subrace == "Drow Elf":
            self.proficiency +=     models.ELF_DROW_SUBRACE_PROFICIENCY
            self.abilities_bonus =  models.ELF_DROW_SUBRACE_ABILITY_BONUS


class Halfling(Race):
    def __init__(self,subrace):
        super().__init__()
        self.proficiency += []
        self.size = "Small"
        self.advantage += ["Frightened"]

        if subrace == "Lightfoot Halfling":
            self.abilities_bonus =  models.HALFLING_LIGHTFOOT_SUBRACE_ABILITY_BONUS
        elif subrace == "Stout Halfling":
            self.abilities_bonus =  models.HALFLING_STOUT_SUBRACE_ABILITY_BONUS
            self.advantage +=       ["Poison"]
            self.resistance +=      ["Poison"]

        self.language +=            models.HALFLING_LANGUAGE

class Human(Race):
    def __init__(self):
        super().__init__()
        self.abilities_bonus =      models.HUMAN_RACE_ABILITY_BONUS
        self.size =                 "Medium"
        self.speed =                30

    def race_language(self,choice):
        self.language +=            [choice]

class Dragonborn(Race):
    def __init__(self,color):
        self.language +=            models.DRAGONBORN_LANGUAGE
        super().__init__()
        self.abilities_bonus =      models.DRAGONBORN_RACE_ABILITY_BONUS

class Gnome(Race):
    def __init__(self,subrace):
        self.language +=            models.GNOME_LANGUAGE
        super().__init__()
        if subrace == "Forest Gnome":
            self.abilities_bonus =  models.GNOME_FOREST_SUBRACE_ABILITY_BONUS
        elif subrace == "Rock Gnome":
            self.abilities_bonus =  models.GNOME_ROCK_SUBRACE_ABILITY_BONUS

class HalfElf(Race):
    def __init__(self):
        super().__init__()
        self.abilities_bonus =      models.HALF_ELF_RACE_ABILITY_BONUS
        self.size =                 "Medium"
        self.speed =                30
        self.vision = {
            "Bright light":         60,
            "Dim light":            60,
            "Darkness":             60
        }
        self.advantage =            ["Charmed"]
        self.imunity +=             [["Sleep","Magic"]]
    
    def race_proficiency(self,choice):
        self.proficiency +=         [choice]

    def race_language(self,choice):
        self.language +=            [choice]

class HalfOrc(Race):
    def __init__(self):
        super().__init__()
        self.abilities_bonus =      models.HALF_ORC_RACE_ABILITY_BONUS
        self.size =                 "Medium"
        self.speed =                30
        self.vision = {
            "Bright light":         60,
            "Dim light":            60,
            "Darkness":             60
        }
        self.proficiency +=         ["Intimidation"]
        self.language +=            ["Orc"]

    def race_attack(self,roll):
        bonus_damage = 0
        if roll == 20:
            pass #TODO: receive roll, use weapon dice, return bonus damage
        return bonus_damage

class Tiefling(Race):
    def __init__(self):
        super().__init__()
        self.abilities_bonus =      models.TIEFLING_RACE_ABILITY_BONUS
        self.size =                 "Medium"
        self.speed =                30
        self.vision = {
            "Bright light":         60,
            "Dim light":            60,
            "Darkness":             60
        }
        self.resistance +=          ["Fire"]
        self.cantrip =              ["Thaummaturgy"]
        self.language +=            ["Infernal"]

    def level_up(self,character):
        if character.sheet["level"] ==      3:
            character.sheet["spells"] += ["Hellish rebuke"]
        elif character.sheet["level"] ==    5:
            character.sheet["spells"] += ["Darkness"]