import re
import tabletop
import tool
import character as chr

class Room:
    def __init__(self,neighbors =[],size= "normal",challenge= None):
        self.neighbors = neighbors
        self.size = size
        self.challenge = challenge 
    
    def add_link(self,link):
        if link not in self.neighbors:
            self.neighbors.append(link)
    
    def see_neighbors(self):
        return self.neighbors

class Battleroom(Room):
    def __init__(self, neighbors=[], size="normal", form="square", challenge=None):
        super().__init__(neighbors, size, challenge)
        self.victory = None
        self.board = tabletop.Board(enemies= self.challenge.enemies_number)

    #Move character
    def move_character(self,character,position):
        if isinstance(character,chr.Player):
            #position = character.choose("move")
            validation = self.board.char_move_to(character,position)
            if validation[0]:
                self.board.set(character.get_position(),self.challenge.get_position())
            elif validation[1] == "isin":
                print("This is not a valid position")
            elif validation[1] == "speed":
                print("You cannot reach this position")
            elif validation[1] == "free":
                print("This position are not free")
        else:
            pass
            #player_position = self.board.characters[0]
            #distance = self.board.distance(character,player_position)
    
    #Is any valid target?
    def can_attack(self,character):
        if isinstance(character,chr.Player): #if character are a player
            choices = []
            for enemy in self.challenge.enemies:
                distance = self.board.is_in_range(character,enemy.position)
                choices.append(distance)
            any = True in choices[:][0]
            return [any, choices]
        else:
            reach_player = self.board.is_in_range(character,self.challenge.enemies)
            return [reach_player,[]]
    
    #Can a character move yourself?
    def can_move(self,character):
        speed = character.speed[1]
        move = speed > 0
        return [move,speed]
    
    #build action options menu
    def action_menu(self,character):  
        menu = {} #make menu

        can_attack = self.can_attack(character) #if can attack anyone,
        if can_attack[0]:                       #add attack on menu
            menu["attack"] = can_attack[1]

        can_move = self.can_move(character) #if character can move,
        if can_move[0]:                     #add attack on menu
            menu["move"] = can_move[1]

        return menu
    
    def actions(self,character,action): #Choose an action
        result = ""
        if action[0] == "move":
            if character.speed[1] > 0:
                self.move_character(character,action[1])
            else:
                pass
        elif action[0] == "attack":
            if isinstance(character,chr.Player):
                result = self.challenge.char_vs_char_attack(character,self.challenge.enemies[action[1]])
        #use item
        return result
    #Check chars health to break the combat loop
    def check_char_health(self,player):
        if not self.challenge.any_lives:
            self.victory = True
        if not player.live:
            self.victory = False

    #Begins combat loop
    def begin_combat(self,player):
        self.challenge.roll_iniciative(player)
        while self.victory == None:
            self.challenge.round(player)
            self.check_char_health(player)
        
        if self.victory:
            room_xp = self.event.xp_gain()
            player.level_up(room_xp)
        else:
            print(tool.colors("You die","red"))