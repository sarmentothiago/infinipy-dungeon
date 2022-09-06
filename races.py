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
        self.cantrip = []
        self.artisan_tools = []
    
    def set_race(self):
        pass

    def level_up(self):
        pass

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
        self.size =                 "Medium"
        self.speed =                25
        self.vision = {
            "Bright light":         60,
            "Dim light":            60,
            "Darkness":             60
        }
        self.advantage =            ["Poison"]
        self.resistance =           ["Poison"]
        self.proficiency +=         ["Battleaxe","Handaxe","Light hammer","Warhammer"]
        self.hp_bonus =         0
        self.artisan_tools += []

        if subrace == "Hill Dwarf":
            self.abilities_bonus =  {
                                        "Constitution": 2,
                                        "Wisdom":       1
                                    }
            self.hp_bonus =         1
        elif subrace == "Montain Dwarf":
            self.abilities_bonus =  {
                                        "Strength":     2,
                                        "Constitution": 2,
                                    }
            self.proficiency +=     ["Light armor","Medium armor"]

        self.language +=            ["Dwarvish"]

    def set_race(self,character,tools):
        character.sheet["abilities score bonus"] = self.abilities_bonus
        character.sheet["size"] = self.size
        character.sheet["speed"] = self.speed
        character.sheet["vision"] = self.vision
        character.sheet["advantage"] += self.advantage
        character.sheet["resistance"] += self.resistance
        character.sheet["proficiency"] += self.proficiency
        character.sheet["imunity"] += self.imunity
        character.sheet["language"] += self.language
        character.sheet["hp"] += self.hp_bonus
        character.sheet["artisan tool"] = tools

    def level_up(self,character):
        if character.sheet["race"] == "Hill Dwarf":
            character.sheet["hp"] += self.hp_bonus

class Elf(Race):
    def __init__(self,subrace):
        super().__init__()
        self.size = "Medium"
        self.speed = 30
        self.vision = {
            "Bright light":         60,
            "Dim light":            60,
            "Darkness":             60
        }
        self.proficiency += ["Perception"]
        self.advantage =            ["Charmed"]
        self.imunity +=             [["Sleep","Magic"]]
        self.language +=            ["Elvish"]
        
        if subrace == "High Elf":
            self.abilities_bonus =  {
                                        "Dexterity":    2,
                                        "Intelligence": 1
                                    }
            self.proficiency +=     ["Longsword","Shortsword","Shortbow","Longbow"]
        elif subrace == "Wood Elf":
            self.abilities_bonus =  {
                                        "Dexterity":    2,
                                        "Wisdom":       1
                                    }
            self.proficiency +=     ["Longsword","Shortsword","Shortbow","Longbow"]
        elif subrace == "Drow Elf":
            self.abilities_bonus =  {
                                        "Dexterity":    2,
                                        "Charisma":     1
                                    }
            self.proficiency +=     ["Rapiers","Shortswords","Hand crossbows"]

class Halfling(Race):
    def __init__(self,subrace):
        super().__init__()
        self.size = "Small"
        self.speed = 25
        self.advantage += ["Frightened"]
        self.hide = []

        if subrace == "Lightfoot Halfling":
            self.abilities_bonus =  models.HALFLING_LIGHTFOOT_SUBRACE_ABILITY_BONUS
            self.hide = ["Naturally Stealthy"]
        elif subrace == "Stout Halfling":
            self.abilities_bonus =  models.HALFLING_STOUT_SUBRACE_ABILITY_BONUS
            self.advantage +=       ["Poison"]
            self.resistance +=      ["Poison"]

        self.language +=            models.HALFLING_LANGUAGE

    def set_race(self,character):
        character.sheet["size"] = self.size
        character.sheet["speed"] = self.speed
        character.sheet["advantage"] += self.advantage
        character.sheet["Fail"]["Lucky"] = self.lucky
        character.sheet["Hide"] += self.hide
        character.sheet["abilities"] = self.abilities_bonus
        character.sheet["resistance"] += self.resistance
        character.sheet["language"] = self.language     
        
    def lucky(self,character):
        return character.sheet["Weapon"]["Dice"].attack_roll()

class Human(Race):
    def __init__(self):
        super().__init__()
        self.abilities_bonus =      models.HUMAN_RACE_ABILITY_BONUS
        self.size =                 "Medium"
        self.speed =                30
        self.vision = {
            "Bright light":         60,
            "Dim light":            30,
            "Darkness":             0
        }

    def set_race(self,character,new_language):
        character.sheet["abilities score bonus"] = self.abilities_bonus
        character.sheet["size"] = self.size
        character.sheet["speed"] = 30
        character.sheet["language"] += [new_language]

class Dragonborn(Race):
    DRAGON_COLORS = {
#       Dragon                      Damage type     Breath weapon 
        "Black":                    ["Acid",        ["Line", "Dexterity"]   ],
        "Blue":                     ["Lightning",   ["Line", "Dexterity"]   ],
        "Brass":                    ["Fire",        ["Line", "Dexterity"]   ],
        "Bronze":                   ["Lightning",   ["Line", "Dexterity"]   ],
        "Copper":                   ["Acid",        ["Line", "Dexterity"]   ],
        "Gold":                     ["Fire",        ["Cone", "Dexterity"]   ],
        "Green":                    ["Poison",      ["Cone", "Constitution"]],
        "Red":                      ["Fire",        ["Cone", "Dexterity"]   ],
        "Silver":                   ["Cold",        ["Cone", "Constitution"]],
        "White":                    ["Cold",        ["Cone", "Constitution"]]
    }
    def __init__(self,color):
        super().__init__()
        self.abilities_bonus =      models.DRAGONBORN_RACE_ABILITY_BONUS
        self.size =                 "Medium"
        self.speed =                30
        self.vision = {
            "Bright light":         60,
            "Dim light":            30,
            "Darkness":             15
        }
        self.language +=            models.DRAGONBORN_LANGUAGE
        self.color =                color

    def set_race(self,character,color):
        character.sheet["abilities score bonus"] = self.abilities_bonus
        character.sheet["size"] = self.size
        character.sheet["speed"] = self.speed
        character.sheet["language"] += self.language
        character.sheet["resistance"] += self.DRAGON_COLORS[color][0]

    def set_weapon(self,color,character):
        self.DRAGON_COLORS[color]
        character.sheet["Weapon"]["Dragon Breath"] = None #TODO: make a new weapon class

    def level_up(self,character):
        if character["level"] == 6:
            character.sheet["Weapon"]["Dragon Breath"]["Dices"] = [6,6,6]
        elif character["level"] == 11:
            character.sheet["Weapon"]["Dragon Breath"]["Dices"] = [6,6,6,6]
        elif character["level"] == 16:
            character.sheet["Weapon"]["Dragon Breath"]["Dices"] = [6,6,6,6,6]

class Gnome(Race):
    def __init__(self,subrace):
        super().__init__()
        self.size = "Small"
        self.speed = 25
        self.vision = {
            "Bright light":         60,
            "Dim light":            60,
            "Darkness":             60
        }
        self.advantage +=           [["Saving throws","Intelligence","Magic"],
                                    ["Saving throws","Wisdom","Magic"],
                                    ["Saving throws","Charisma","Magic"]]
        
        if subrace == "Forest Gnome":
            self.abilities_bonus =  models.GNOME_FOREST_SUBRACE_ABILITY_BONUS
            self.cantrip += ["Minor Ilusion"]
            self.language += ["Simple", "Animal Communication"]
        elif subrace == "Rock Gnome":
            self.abilities_bonus =  models.GNOME_ROCK_SUBRACE_ABILITY_BONUS
            self.artisan_tools += ["Tinker's Tools"]
        self.language +=            models.GNOME_LANGUAGE

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
    
    def set_race(self,character,proficiency):
        character.sheet["abilities score bonus"] = self.abilities_bonus
        character.sheet["size"] = self.size
        character.sheet["speed"] = self.speed
        character.sheet["vision"] = self.vision
        character.sheet["advantage"] += self.advantage
        character.sheet["imunity"] += self.imunity
        character.sheet["language"] += self.language
        character.sheet["proficiency"] += proficiency

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

    def set_race(self,character):
        character.sheet["abilities score bonus"] = self.abilities_bonus
        character.sheet["size"] = self.size
        character.sheet["speed"] = self.speed
        character.sheet["vision"] = self.vision
        character.sheet["proficiency"] += self.proficiency
        character.sheet["language"] += self.language

    def set_action(self,character):
        character.sheet["Critical"]["Savage attack"] =  self.savage_attack
    
    def savage_attack(self,character):
        return character.sheet["Weapon"]["Dice"].damage_roll()

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

    def set_race(self,character):
        character.sheet["abilities score bonus"] = self.abilities_bonus
        character.sheet["size"] = self.size
        character.sheet["speed"] = self.speed
        character.sheet["vision"] = self.vision
        character.sheet["resistance"] += self.resistance
        character.sheet["cantrip"] += self.cantrip
        character.sheet["language"] += self.language

    def level_up(self,character):
        if character.sheet["level"] ==      3:
            character.sheet["spells"] += ["Hellish rebuke"]
        elif character.sheet["level"] ==    5:
            character.sheet["spells"] += ["Darkness"]