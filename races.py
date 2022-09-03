class Race:
    HUMAN_RACE_ABILITY_BONUS = {
        "Strength":     1,
        "Dexterity":    1,
        "Constitution": 1,
        "Intelligence": 1,
        "Wisdom":       1,
        "Charisma":     1
    }

    DRAGONBORN_RACE_ABILITY_BONUS = {
        "Strength":     2,
        "Charisma":     1
    }

    GNOME_FOREST_SUBRACE_ABILITY_BONUS = {
        "Dexterity": 1,
        "Intelligence": 2
    }

    GNOME_ROCK_SUBRACE_ABILITY_BONUS = {
        "Constitution": 1,
        "Intelligence": 2
    }

    HALF_ELF_RACE_ABILITY_BONUS = {
        "Charisma":     2
    }

    HALF_ORC_RACE_ABILITY_BONUS = {
        "Strength":     2,
        "Constitution": 1
    }

    TIEFLING_RACE_ABILITY_BONUS = {
        "Intelligence": 1,
        "Charisma":     2
    }

    def __init__(self):
        self.abilities_bonus = {}
        self.skills_bonus = {}
        self.proficiency = []
        self.language = ["Common"]
    
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

class Dwarf(Race):
    def __init__(self,subrace):
        super().__init__()
        self.proficiency += self.DWARF_PROFICIENCY
        self.language += self.DWARF_LANGUAGE

        if subrace == "Hill Dwarf":
            self.abilities_bonus = self.DWARF_HILL_SUBRACE_ABILITY_BONUS
        elif subrace == "Montain Dwarf":
            self.abilities_bonus = self.DWARF_MONTAIN_SUBRACE_ABILITY_BONUS
            self.proficiency += 

class Elf(Race):
    def __init__(self,subrace):
        super().__init__()
        self.proficiency += ["Perception"]
        self.language += ["Elvish"]
        
        if subrace == "High Elf":
            self.abilities_bonus = self.ELF_HIGH_SUBRACE_ABILITY_BONUS
            self.proficiency += ["Longsword","Shortsword","Shortbow","Longbow"]
        elif subrace == "Wood Elf":
            self.abilities_bonus = self.ELF_WOOD_SUBRACE_ABILITY_BONUS
            self.proficiency += ["Longsword","Shortsword","Shortbow","Longbow"]
        elif subrace == "Drow Elf":
            self.abilities_bonus = self.ELF_DROW_SUBRACE_ABILITY_BONUS
            self.proficiency += ["Rapiers","Shortswords","Hand crossbows"]


class Halfling(Race):
    def __init__(self,subrace):
        super().__init__()
        self.proficiency += []
        self.language += ["Halfling"]

        if subrace == "Lightfoot Halfling":
            self.abilities_bonus = self.HALFLING_LIGHTFOOT_SUBRACE_ABILITY_BONUS
        elif subrace == "Stout Halfling":
            self.abilities_bonus = self.HALFLING_STOUT_SUBRACE_ABILITY_BONUS

class Human(Race):
    def __init__(self):
        super().__init__()
        self.abilities_bonus = self.HUMAN_RACE_ABILITY_BONUS

class Dragonborn(Race):
    def __init__(self,subrace):
        self.language += ["Draconic"]
        super().__init__()
        if subrace == "":
            self.abilities_bonus = self.GNOME_FOREST_SUBRACE_ABILITY_BONUS
        elif subrace == "":
            self.abilities_bonus = self.GNOME_ROCK_SUBRACE_ABILITY_BONUS
        self.abilities_bonus = self.DRAGONBORN_RACE_ABILITY_BONUS

class Gnome(Race):
    def __init__(self):
        self.language += ["Gnomish"]
        super().__init__()
        self.abilities_bonus = self.GNOME_ROCK_SUBRACE_ABILITY_BONUS

class HalfElf(Race):
    def __init__(self):
        super().__init__()
        self.abilities_bonus = self.HALF_ELF_RACE_ABILITY_BONUS

class HalfOrc(Race):
    def __init__(self):
        super().__init__()
        self.abilities_bonus = self.HALF_ORC_RACE_ABILITY_BONUS

class Tiefling(Race):
    def __init__(self):
        super().__init__()
        self.abilities_bonus = self.TIEFLING_RACE_ABILITY_BONUS