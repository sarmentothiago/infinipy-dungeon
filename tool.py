import random as r

class Dice:
    def __init__(self,dices = [4]):
        self.dices = dices
        self.dices_number = len(dices)
        self.roll_play = [0] * self.dices_number
    
    def roll(self):
        for play in range(self.dices_number):
            dice = r.randint(1,self.dices[play])
            self.roll_play[play] = dice

    def get_roll_play(self):
        return self.roll_play
    
    def get_roll_result(self):
        result = sum(self.roll_play)
        return result
        
def colors(string,color):
    palette = {
        "bold": '\033[1m',
        "underline": '\033[4m',
        "grey": '\033[90m',
        "red": '\033[91m',
        "green": '\033[92m',
        "yellow": '\033[93m',
        "blue": '\033[94m',
        "purple": '\033[95m',
        "cyan": '\033[96m',
        "end": '\033[0m'
    }
    return palette[color] + string + palette["end"]