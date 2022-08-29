from turtle import position
import weapons
import tool
import os

skeleton = {
    "name": "Skeleton",
    "xp": 50,
    "hp": 13,
    "armor class": 13,
    "speed": [30,30],
    "weapon": weapons.shortsword
}

test_char = {
    "name": "Stranger",
    "level": 1,
    "xp": 0,
    "hp": 20,
    "armor class": 15,
    "speed": [30,30],
    "weapon": weapons.greatsword
}

char_xp = [0,300, 900, 2_700,
        6_500, 14_000, 23_000, 34_000,
        48_000, 64_000, 85_000, 100_000,
        120_000, 140_000, 165_000, 195_000,
        225_000, 265_000, 305_000, 355_000]

class Character:
    def __init__(self,sheet,position=[0,0]):
        self.name = sheet.get("name")
        self.hp = sheet.get("hp")
        self.armor = sheet.get("armor class")
        self.damage = 1
        self.weapon = weapons.Weapon(sheet.get("weapon"))
        self.live = True
        self.xp = sheet.get("xp")
        self.speed = sheet.get("speed")
        self.position = position

    def roll_d20(self):
        dice = tool.Dice([20])
        dice.roll()
        roll = dice.get_roll_result()
        return roll

    def iniciative_roll(self):
        return self.roll_d20()

    def attack_roll(self):
        dice = self.roll_d20()
        if dice == 1:
            return False
        elif dice == 20:
            return True
        else:
            return dice

    def damage_roll(self):
        attack = self.damage + self.weapon.damage()
        return attack
    
    def heal(self,healing):
        self.hp += healing
    
    def take_damage(self,damage):
        self.hp -= damage

    def equip_weapon(self):
        self.weapon = 0
    
    def take_damage(self,damage):
        if self.live:
            self.hp -= damage
            if self.hp <= 0:
                self.live = False
    
    def walk(self,distance,position):
        self.position = position
        self.speed[1] += -distance

    def get_position(self):
        return self.position

    def get_speed(self):
        return self.speed

    #Build possible actions menu
    def get_actions(self,enimies_nearby):
        if self.speed > 0:
            pass
        if enimies_nearby:
            pass

class Player(Character):
    def __init__(self, sheet, position= [0,0]):
        super().__init__(sheet, position)
        self.name = tool.colors(self.name,"blue")
        self.level = sheet.get("level")

    def level_up(self,xp_gain):
        self.xp += xp_gain
        if self.xp > char_xp[self.level]:
            self.level += 1

    def act(self,menu,challenge,last_attack):

        os.system("clear")
        if last_attack != "":
            print(last_attack,end="\n\n")
        if "attack" in menu.keys(): #attack shows enemies on range 
            print(tool.colors("[attack] ","bold"),end="")
            print("The enemies nearby are:")
            targets_range = menu["attack"]
            targets = []

            for enemy in range(len(targets_range)): #read valid targets
                if targets_range[enemy][0]:
                    targets.append([enemy,targets_range[enemy][1]])

            challenge.show_enemies(targets) #show valid enemies target
        
        if "move" in menu.keys(): #move options
            print(tool.colors("[move]","bold"),end="")
            speed_left = menu["move"]
            print(" Your position is",self.position,f"and can move {speed_left:,.1f} meters")
        
        print(tool.colors("[end turn]","bold")) #Always have "end turn" option
        
        action = input(tool.colors("\nPlayer action: ","bold"))
        choice = self.choose(action)

        return [action,choice]

    #Player choose an action    
    def choose(self,action):
        if action == "move":
            position = [None,None]
            #print("Your position is",self.get_position(),"Choose your next position")
            position = input(tool.colors("New position: ","bold")).split(",")
            position = [int(i) for i in position]
            return position
        elif action == "attack":
            target = int(input(tool.colors("Choose your target: ","bold")))
            return target
        elif action == "end turn":
            return True

class Enemy(Character):
    def __init__(self, sheet, position):
        super().__init__(sheet, position)
        self.name = tool.colors(self.name,"yellow")
        
