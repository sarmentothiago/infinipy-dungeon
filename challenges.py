from character import Character, Enemy
import tool

class Challenge:
    def __init__(self,name=None, locked= False):
        self.name = name
        self.locked = locked

    def walk():
        pass

class Healing(Challenge):
    def __init__(self, name="Healing room", heal = 0):
        super().__init__(name)
        self.heal = heal
    
    def healing(self,player):
        player.heal(self.heal)

class Combat(Challenge):
    def __init__(self, name="Battle room", enemies = []):
        super().__init__(name)
        self.name = name
        self.enemies = enemies
        self.enemies_number = len(enemies)
        
        self.enemies_position = [[0,0]] * self.enemies_number
        for i in range(self.enemies_number):
            self.enemies_position[i] = self.enemies[i].position
        
        self.turn = None
        self.round_number = 0
        self.any_lives = True
    
    def add_enemy(self,enemy):
        self.enemies.append(enemy)

    def remove_enemy(self,enemy_index):
        self.enemies.pop(enemy_index)

    def get_position(self):
        return self.enemies_position
    #Check if anyone in the room are alive
    def check_enemies(self):
        for enemy_index in range(self.enemies_number):
            if self.enemies[enemy_index].live:
                self.any_lives = True
                break
            else:
                self.any_lives = False
    
    #Determining the order of combatants’ turns
    def roll_iniciative(self,player):
        turn_len = self.enemies_number + 1
        self.turn = [''] * turn_len
        enemies_iniciative = [[0,0]] * self.enemies_number
        player_roll = player.iniciative_roll()

        for enemy in range(self.enemies_number):
            enemies_iniciative[enemy] = [self.enemies[enemy].iniciative_roll(), enemy]
        
        enemies_iniciative.append([player_roll,'p'])
        enemies_iniciative.sort(reverse=True)
        
        for character in range(turn_len):
            self.turn[character] = enemies_iniciative[character][1]
        
        return self.turn

    #Calculate combat xp
    def xp_gain(self):
        xp = 0
        for enemy in self.enemies:
            xp += enemy.xp
        return xp

    #Show enemies list
    def show_enemies(self,enemies_list=[]):
        if len(enemies_list) > 1:
            for enemy in range(len(self.enemies)):
                nearby = enemy in enemies_list[enemy]
                if self.enemies[enemy].live and nearby:
                    print('[',enemy,"] ",self.enemies[enemy].name,"\b: position",self.enemies[enemy].position,self.enemies[enemy].hp," hp")
        elif enemies_list != []: #just one target
            if self.enemies[enemies_list[0][0]].live:
                print('[',enemies_list[0][0],"] - ",self.enemies[enemies_list[0][0]].name,"\b: position",self.enemies[enemies_list[0][0]].position,self.enemies[enemies_list[0][0]].hp," hp")
            else:
                print("[",enemies_list[0][0],"] ",self.enemies[enemies_list[0][0]].name,"\b: ",tool.colors("dead","red"))
        else: #showing all enemies
            for enemy in range(len(self.enemies)):
                if self.enemies[enemy].live:
                    print('[',enemy,"] ",self.enemies[enemy].name,"\b: position",self.enemies[enemy].position,self.enemies[enemy].hp," hp")
                else:
                    print('[',enemy,"] ",self.enemies[enemy].name,"\b: ",tool.colors("dead","red"))
    
    #Player turn
    def player_turn(self,player):
        if len(self.enemies) > 1:
            print("Enemies left:")
            self.show_enemies()
            choice = int(input("Chose a target: "))
            self.char_vs_char_attack(player,self.enemies[choice],True)
        else:
            self.char_vs_char_attack(player,self.enemies[0],True)

    #Round Battle
    def round(self,player):
        self.round_number += 1
        print("Round ",self.round_number)
        for character in self.turn:
            if character == 'p':
                if player.live:
                    self.player_turn(player)
                else:
                    break
            elif self.enemies[character].live:
                self.char_vs_char_attack(self.enemies[character],player)
        self.check_enemies()

    #Make an character give damage to another character
    def damage_char(self,attack_char,char):
        damage = attack_char.damage_roll()
        char.take_damage(damage)
        result = " " + attack_char.name + " give " + tool.colors(str(damage),"red") + " damage and now " + char.name
        if char.live:
            result += " have " + tool.colors(str(char.hp),"green") + " hp"
        else:
            result += " are " + tool.colors("dead","red")
        return result
    
    #Make an character attack another character
    def char_vs_char_attack(self,attack_char,defend_char):
        attack_roll = attack_char.attack_roll()
        result = attack_char.name + " roll " + str(attack_roll)
        if attack_roll is True:
            result += "... Critical Hit! "
            #print("Critical Hit! ",end='')
            result += self.damage_char(attack_char,defend_char)
        elif attack_roll is False:
            result += "... Critical Fail! " + attack_char.name + " miss"
        else:
            if attack_roll >= defend_char.armor:
                result += self.damage_char(attack_char,defend_char)
            else:
                result += "... Fail! " + attack_char.name + " miss"
        return result