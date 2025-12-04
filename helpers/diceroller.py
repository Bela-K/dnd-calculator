import random

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self, amount=1, modifier=0):
        return sum(random.randint(1, self.sides) for _ in range(amount)) + modifier
    
    def advantage_roll(self, sides, modifier=0):
        roll1 = random.randint(1, sides)
        roll2 = random.randint(1, sides)
        return max(roll1, roll2) + modifier
    
    def disadvantage_roll(self, sides, modifier=0):
        roll1 = random.randint(1, sides)
        roll2 = random.randint(1, sides)
        return min(roll1, roll2) + modifier
    
