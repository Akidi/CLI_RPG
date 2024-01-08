import os
import colorama
from colorama import Fore
from battle import Battle
from confirm import confirm
from character import Hero, Enemy

colorama.init()

save = open("savegame.dat", "w+")
hero = Hero(name="Hero")
battle = Battle(hero=hero)

def main():
    os.system("cls")
    hero.display_stats_box(show_all_stats=True)
    hero.display_stats_box()

    if (confirm("Do you want to start a battle?")):
        battle.start(enemy=Enemy(name="Rat"))

    print(f"Here I would show your save file.")
    

if __name__ == "__main__":
    os.system("cls")
    main()
    