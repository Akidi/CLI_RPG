import os
import weapon
import Stats
from screen import Screen
from dice import Roll
from random import random, choice
from healthBar import HealthBar
from confirm import confirm
from colorama import Fore, Back, Style

dice = Roll()
weapons = [weapon.fists, weapon.club, weapon.dagger]
damage_types = [weapon.damage_type for weapon in weapons]
screen = Screen()

class Character:
    """docstring for Chatacter."""
    def __init__(self, name: str, base_stats) -> None:
        self.name = name
        self.stats = Stats(base_stats)
        self.newCharacter = True

    def attack(self, target) -> None:
        baseDamage = round(dice.roll(self.weapon.damage) + self.strength + (self.dexterity / 2))
        critHit = dice.roll("1d100") > 90
        damage = int(baseDamage * (dice.roll(f"1d80+50")/100) * (2.5 if critHit else 1))
        print(f"{self.name} {critHit and "critically hits for" or "deals"} {damage} {self.weapon.damage_type} to {target.name} with {self.weapon.name}")
        target.hp = max(int(target.hp - damage), 0)
        target.health_bar.update()

    def display_stats_box(self, color=Fore.GREEN, box_width=25, hp_bar_length=20, show_all_stats=False):
        top_border = f"{Fore.WHITE}{'-' * box_width}"
        bottom_border = f"{Fore.WHITE}{'-' * box_width}"
        stat_line = f"{color}{self.name.center(box_width)}"
        print(top_border)
        print(stat_line)
        if show_all_stats:
            for stat_name, stat_value in self.__dict__.items():
                if not stat_name.startswith("__") and not stat_name in ["weapon", "health_bar"]:  # Exclude internal attributes
                    print(f"{Fore.WHITE}{stat_name}: {stat_value}")
        else:
            print(f"{Fore.WHITE}HP: {self.health_bar.draw()}")
            print(f"{Fore.WHITE}/{self.hp_max}")
        print(bottom_border)

        print(Style.RESET_ALL, end="")

        


class Hero(Character):
    """docstring for Hero."""
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.gold = 0
        self.currentExp = 0
        self.level = 1
        self.toNextLevelExp = self.toLevelUp(self.level)
        self.equip(choice(weapons))
        self.generateHero()
        self.health_bar = HealthBar(self, color="green")

    def generateHero(self) -> None:
        if  (not self.newCharacter):
            return
        print("Generating stats\n--------------")
        statDice = "4d5+7"
        hpDice = "8d20+150"
        mpDice = "5d5+10"
        while True:
            self.strength = dice.roll(statDice)
            self.dexterity = dice.roll(statDice)
            self.intelligence = dice.roll(statDice)
            self.endurance = dice.roll(statDice)
            self.wisdom = dice.roll(statDice)
            self.hp = self.hp_max = dice.roll(hpDice) + self.endurance + int(self.strength / 2)
            self.mp = self.mp_max = dice.roll(mpDice) + self.intelligence + int(self.wisdom / 2)
            os.system("cls")
            self.display_stats_box(show_all_stats=True)
            if (confirm("Keep these stats?", False)):
                self.newCharater = False
                break
            

    def equip(self, weapon: weapon.Weapon) -> None:
        self.weapon = weapon

    def drop(self) -> None:
        self.weapon = self.default_weapon

    def toLevelUp(self, level: int) -> int:
        return (round((4 * pow(level+3, 3)) / 5) + 133)
    
    def getRewards(self, target: Character) -> None:
        self.currentExp += target.expAward
        self.gold += target.goldAward
        print(f"{target.name} awarded {target.expAward} experience points and received {target.goldAward} gold.")
        self.applyXp()

    def applyXp(self) -> None:
        readyToLevel = self.toNextLevelExp <= self.currentExp
        hpDice = "3d15+25"
        mpDice = "3d3+5"
        statDice = "1d5+3"
        while readyToLevel:
            hpIncrease = dice.roll(hpDice)
            mpIncrease = dice.roll(mpDice)
            strengthIncrease = random() > 0.2 and dice.roll(statDice) or 0
            dexterityIncrease = random() > 0.2 and dice.roll(statDice) or 0
            intelligenceIncrease = random() > 0.2 and dice.roll(statDice) or 0
            wisdomIncrease = random() > 0.2 and dice.roll(statDice) or 0
            luckIncrease = self.level % 3 == 0 or self.level == 1 and dice.roll(statDice) or 0
            self.hp = self.hp_max = (self.hp_max + hpIncrease)
            self.mp = self.mp_max = (self.mp_max + mpIncrease)
            self.strength += strengthIncrease
            self.dexterity += dexterityIncrease
            self.intelligence += intelligenceIncrease
            self.wisdom += wisdomIncrease
            self.luck += luckIncrease
            self.level += 1
            self.currentExp -= self.toNextLevelExp
            self.toNextLevelExp = self.toLevelUp(self.level)
            readyToLevel = self.toNextLevelExp <= self.currentExp
            print(f"{self.name} has grown in strength and achieved level {self.level}")
            print(f"HP has gone up {self.hp_max - hpIncrease} -> {self.hp_max}")
            print(f"MP has gone up {self.mp_max - mpIncrease} -> {self.mp_max}")
            if (strengthIncrease > 0):
                print(f"Strength has gone up {self.strength - strengthIncrease} -> {self.strength}")
            if (dexterityIncrease > 0):
                print(f"Dexterity has gone up {self.dexterity - dexterityIncrease} -> {self.dexterity}")
            if (intelligenceIncrease > 0):
                print(f"Intelligence has gone up {self.intelligence - intelligenceIncrease} -> {self.intelligence}")
            if (wisdomIncrease > 0):
                print(f"Wisdom has gone up {self.wisdom - wisdomIncrease} -> {self.wisdom}")
            if (luckIncrease > 0):
                print(f"Luck has gone up {self.luck - luckIncrease} -> {self.luck}")
        
        print(f"Current Exp {self.currentExp}")
        print(f"To Next Level {self.toNextLevelExp}")
    
    def save(self):
        pass
        

class Enemy(Character):
    """docstring for Enemy."""
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.weapon = choice(weapons)
        self.level = 1
        statDice = f"{1 + self.level +3}d5+7"
        hpDice = f"{4 + (self.level + 3)}d20+150"
        mpDice = f"{1 + (self.level + 3)}d5+10"
        self.hp = self.hp_max = dice.roll(hpDice)
        self.mp = self.mp_max = dice.roll(mpDice)
        self.strength = dice.roll(statDice)
        self.dexterity = dice.roll(statDice)
        self.intelligence = dice.roll(statDice)
        self.wisdom = dice.roll(statDice)
        self.expAward = int((6 * (self.level + 3) + pow(self.level, 3)) * ((random() *50) + 80) / 100) 
        self.goldAward = int(pow(self.level + 3,3) * (((random() * 50) + 80) / 100))
        self.health_bar = HealthBar(self, color="red")