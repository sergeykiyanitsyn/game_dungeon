from dataclasses import dataclass
from typing import Optional

@dataclass
class Weapon:
    name: str
    description: str
    damage: int
    hit_chance: int

@dataclass
class Armor:
    name: str
    description: str
    defense: int

@dataclass
class Combatant:
    name: str
    hp: int
    max_hp: int
    weapon: Weapon
    armor: Armor
    description: str = ""
    death_descriptions: str = ""

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, dmg: int) -> None:
        self.hp = max(0, self.hp - dmg)

@dataclass
class Player(Combatant):
    death_descriptions: Optional[list] = None

@dataclass
class Enemy(Combatant):
    death_description: Optional[str] = None

@dataclass
class Room:
    tag: str
    description: str
    enemy: Optional[Enemy] = None

    def has_enemy(self) -> bool:
        return self.enemy is not None and self.enemy.is_alive()
