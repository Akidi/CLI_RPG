class Battle:
    """
    Battle Class handles the 
    """
    def __init__(self, hero) -> None:
        self.hero = hero
        self.enemy = None
        self.is_active = False
        self.turn = 0
        self.round = 0
    
    def start(self, enemy) -> None:
        self.hero = hero
        self.enemy = enemy
        self.is_active = True
        self.turn = self.enemy.dexterity > self.hero.dexterity
        while not (self.hero.hp == 0 or self.enemy.hp == 0):
            self.hero.health_bar.draw()
            self.enemy.health_bar.draw()
            self.take_turn()

        self.end()

    def take_turn(self) -> None:
        self.hp = 0
        

    
    def end(self) -> None:
        self.hero = None
        self.enemy = None
        self.is_active = False