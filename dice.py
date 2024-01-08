import re
from random import random
class Roll:
  def __init__(self) -> None:
    self.dice = {}

  def roll(self, dice: str) -> None:
    dieTemplate = r"(\d*)[dD](\d*)\+?(\d*)"
    die: [str] = [int(die) for die in re.split(dieTemplate, dice) if die]
    
    total = sum([self.die_roll(die[1]) for _ in range(die[0])]) + (die[2] if len(die) > 2 else 0)
    return total
  
  def die_roll(self, sides):
    return round(random() * sides)