shortsword = {
            "name": "shortsword",
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

skeleton = {
    "name": "Skeleton",
    "xp": 50,
    "hp": 13,
    "armor class": 13,
    "speed": [30,30],
    "weapon": shortsword
}

ABILITIES_LIST = {
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0
}

skill_str = {
    "ability": "Strenght",
    "bonus": 0
}

skill_dex = {
    "ability": "Dexterity",
    "bonus": 0
}

skill_con = {
    "ability": "Constitution",
    "bonus": 0
}

skill_int = {
    "ability": "Intelligence",
    "bonus": 0
}

skill_wis = {
    "ability": "Wisdom",
    "bonus": 0
}

skill_cha = {
    "ability": "Charisma",
    "bonus": 0
}

skills_test = {
    "Acrobatics": skill_dex,
    "Animal Handling": skill_wis,
    "Arcana": skill_int,
    "Athletics": skill_str,
    "Deception": skill_cha,
    "History": skill_int,
    "Insight": skill_wis,
    "Intimidation": skill_cha,
    "Investigation": skill_int,
    "Medicine": skill_wis,
    "Nature": skill_int,
    "Perception": skill_wis,
    "Performance": skill_cha,
    "Persuasion": skill_cha,
    "Religion": skill_int,
    "Sleight of Hands": skill_dex,
    "Stealth": skill_dex,
    "Survival": skill_wis
}

test_char_complete = {
    "name": "Stranger",
    "level": 1,
    "xp": 0,
    "race": "Human",
    "class": "Fighter",
    "abilities": ABILITIES_LIST,
    "skills": skills_test,
    "hp": 0,
    "armor class": 0,
    "iniciative": 0,
    "speed": 0,
    "weapon": greatsword
}

############ Dwarf race info ##########
DWARF_PROFICIENCY = ["Battleaxe","Handaxe","Light hammer","Warhammer"]
DWARF_LANGUAGE = ["Dwarvish"]
DWARF_HILL_SUBRACE_ABILITY_BONUS={
        "Constitution": 2,
        "Wisdom":       1
}
DWARF_MONTAIN_SUBRACE_PROFICIENCY = ["Light armor","Medium armor"]
DWARF_MONTAIN_SUBRACE_ABILITY_BONUS={
        "Strength":     2,
        "Constitution": 2,
}
########### Elf race info
ELF_PROFICIENCY = ["Perception"]
ELF_LANGUAGE = ["Elvish"]
ELF_HIGH_SUBRACE_PROFICIENCY = ["Longsword","Shortsword","Shortbow","Longbow"]
ELF_HIGH_SUBRACE_ABILITY_BONUS = {
    "Dexterity":    2,
    "Intelligence": 1
}
ELF_WOOD_SUBRACE_PROFICIENCY = ["Longsword","Shortsword","Shortbow","Longbow"]
ELF_WOOD_SUBRACE_ABILITY_BONUS = {
    "Dexterity":    2,
    "Wisdom":       1
}
ELF_DROW_SUBRACE_PROFICIENCY = ["Rapiers","Shortswords","Hand crossbows"]
ELF_DROW_SUBRACE_ABILITY_BONUS = {
    "Dexterity":    2,
    "Charisma":     1
}
########### Halfling race info
HALFLING_LANGUAGE = ["Halfling"]
HALFLING_LIGHTFOOT_SUBRACE_ABILITY_BONUS={
    "Dexterity":    2,
    "Charisma":     1
}
HALFLING_STOUT_SUBRACE_ABILITY_BONUS={
    "Dexterity":    2,
    "Constitution": 1
}
########### Human race info
HUMAN_RACE_ABILITY_BONUS = {
    "Strength":     1,
    "Dexterity":    1,
    "Constitution": 1,
    "Intelligence": 1,
    "Wisdom":       1,
    "Charisma":     1
}
########### Dragonborn race info
DRAGONBORN_LANGUAGE = ["Draconic"]
DRAGONBORN_RACE_ABILITY_BONUS = {
    "Strength":     2,
    "Charisma":     1
}
########### Gnome race info
GNOME_LANGUAGE = ["Gnomish"]
GNOME_FOREST_SUBRACE_ABILITY_BONUS = {
    "Dexterity": 1,
    "Intelligence": 2
}
GNOME_ROCK_SUBRACE_ABILITY_BONUS = {
    "Constitution": 1,
    "Intelligence": 2
}
########### Half Elf info
HALF_ELF_RACE_ABILITY_BONUS = {
    "Charisma":     2
}
########### Half Orc info
HALF_ORC_RACE_ABILITY_BONUS = {
    "Strength":     2,
    "Constitution": 1
}
########### Tiefling
TIEFLING_RACE_ABILITY_BONUS = {
    "Intelligence": 1,
    "Charisma":     2
}

#RACES = {
#    "Hill Dwarf":,
#    "Montain Dwarf":,
#    "High Elf":,
#    "Wood Elf":,
#    "Drow Elf":,
#    "Lightfoot Halfling":,
#    "Stout Halfling":,
#    "Human":,
#    "Dragonborn":,
#    "Forest Gnome":,
#    "Rock Gnome":,
#    "Half-Elf":,
#    "Half-Orc":,
#    "Tiefling":
#}

class models:    
    def __init__(self):
        pass