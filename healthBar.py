import os

os.system("")

class HealthBar:
    symbol_fill: str = "█"
    symbol_remaining: str = "_"
    symbol_border: str = "|"
    colors: dict = {
        "red": "\033[91m",
        "purple": "\33[95m",
        "blue":  "\33[34m",
        "blue2":  "\33[36m",
        "blue3":  "\33[96m",
        "green":  "\033[92m",
        "green2":  "\033[32m",
        "brown":  "\33[33m",
        "yellow":  "\33[93m",
        "grey":  "\33[37m",
        "default":  "\033[0m",
    }

    def __init__(self, entity, length: int = 30, is_colored: bool=True, color: str=""):
        self.entity = entity
        self.length = length
        self.current_value = entity.hp
        self.max_value = entity.hp_max

        self.is_colored = is_colored
        self.color = self.colors.get(color, "default")
    
    def update(self) -> None:
        self.current_value = self.entity.hp

    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s HEALTH: {self.entity.hp}/{self.entity.hp_max}")
        print(f"{self.symbol_border}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_fill}"
              f"{lost_bars * self.symbol_remaining}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.symbol_border}")