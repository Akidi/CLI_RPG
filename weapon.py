class Weapon:
    """docstring for Weapon."""
    def __init__(self, name: str, weapon_type:str, damage_type: str, damage: int, value:int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage_type = damage_type
        self.damage = damage
        self.value = value

fists = Weapon(
    name="Fists",
    weapon_type="1-hand",
    damage_type="bludgeoning",
    damage="1d4",
    value="0"
)

club = Weapon(
    name="Club",
    weapon_type="1-handed",
    damage_type="bludgeoning",
    damage="1d4",
    value="1 silver"
)

dagger = Weapon(
    name="Dagger",
    weapon_type="1-handed",
    damage_type="piercing",
    damage="1d4",
    value="2 gold"
)