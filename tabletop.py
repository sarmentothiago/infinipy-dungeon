import math
import random
from tabnanny import check
import character as chr

class Board:
    def __init__(self,length=[30,30],enemies=0):
        self.board_len = length
        self.characters_number = enemies +1
        self.characters = [[0,0]] * self.characters_number

    #Verify a attack range
    def is_in_range(self,character,target):
        distance = self.distance(character.position,target)
        #Check if target are in char 1 weapon range
        if distance <= character.weapon.range:
            return [True,distance]
        else:
            return [False,distance]

    def random_position(self,character):
        valid_position = False
        
        while valid_position:
            x = random.randint(0,self.board_len[0])
            y = random.randint(0,self.board_len[1])
            valid_position,_ = self.char_move_to(character,[x,y])

    #Distance between two points
    def distance(self,origin,target):
        return math.sqrt(pow(origin[0] - target[0], 2) + pow(origin[1] - target[1], 2))

    #Move an character to a position
    def char_move_to(self,character,position):
        free = self.is_free(position)
        speed = self.can_reach(character,position)
        isin = self.is_in_board(position)
        
        if free and speed[0] and isin:
            character.walk(speed[1],position)           
            return [True,"move"]
        elif not isin:
            return [False,"isin"]
        elif not speed[0]:
            return [False,"speed"]
        elif not free:
            return [False,"free"]

    #Update board|Obs 1: The first char in array is always the player
    def set(self,player_position,enemies_position):
        self.characters[0] = player_position
        self.characters[1:] = enemies_position
        
    #Check if position is free
    def is_free(self,char_new_position):
        return not char_new_position in self.characters
    
    #Verify if character have speed for move
    def can_reach(self,character,position):
        distance = self.distance(character.position,position)
        if distance <= character.speed[1]:
            return [True,distance]
        else:
            return [False,distance]
    
    #Verify if position is in the board
    def is_in_board(self, position):
        if position[0] >= 0 and position <= self.board_len:
            return True
        else:
            return False

    def is_target_nearby(self,character,enemies):
        if isinstance(character,chr.Player):
            targets = []
            for enemy in range(len(enemies)):
                is_range = self.is_in_range(character,enemies[enemy].position)
                if is_range[0]:
                    targets.append(enemy)
            return targets
        else:
            return self.is_in_range(character,self.characters[0])