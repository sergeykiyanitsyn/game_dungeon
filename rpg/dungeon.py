import random
from typing import List, Optional
from .loader import load_rooms, load_enemies, load_difficulties, load_weapons, load_armors, load_players
from .entities import Room, Enemy, Weapon, Armor, Player

DEFAULT_MAP = ['St', ' ', 'E', 'E', ' ', 'E', 'Ex']

def _make_weapon_by_name(weapons_data, name: str) -> Weapon:
    for w in weapons_data["weapons"]:
        if w["name"] == name:
            return Weapon(w["name"], w["description"], int(w["damage"]), int(w["hit_chance"]))
    raise ValueError(f"Weapon {name} not found")

def _make_armor_by_name(armors_data, name: str) -> Armor:
    for a in armors_data["armors"]:
        if a["name"] == name:
            return Armor(a["name"], a["description"], int(a["defense"]))
    raise ValueError(f"Armor {name} not found")

def create_player(seed_name: Optional[str] = None) -> Player:
    players = load_players()
    weapons = load_weapons()
    armors = load_armors()
    name = random.choice(players["names"]) if seed_name is None else seed_name
    weapon = _make_weapon_by_name(weapons, players["base"]["weapon"])
    armor = _make_armor_by_name(armors, players["base"]["armor"])
    hp = int(players["base"]["hp"])
    desc = random.choice(players["descriptions"])
    death_descs = players.get("death_descriptions", [])
    return Player(name=name, hp=hp, max_hp=hp, weapon=weapon, armor=armor, description=desc, death_descriptions=death_descs)

def create_enemy_from_template(template: dict):
    weapons = load_weapons()
    armors = load_armors()
    weapon = _make_weapon_by_name(weapons, template["weapon"])
    armor = _make_armor_by_name(armors, template["armor"])
    return Enemy(name=template["name"], hp=int(template["hp"]), max_hp=int(template["hp"]), weapon=weapon, armor=armor, description=template.get("description",""), death_description=template.get("death_description",""))

def generate_dungeon_by_difficulty(difficulty: str = "lite"):
    difficulties = load_difficulties()
    if difficulty not in difficulties:
        raise ValueError("Уровень сложности должен быть 'lite', 'medium' или 'hard'")

    settings = difficulties[difficulty]
    length = settings["length"]
    enemy_chance = settings["enemy_chance"]

    rooms_data = load_rooms()
    enemies_data = load_enemies()
    room_descs = rooms_data["room_descriptions"]

    rooms = []

    for i in range(length):
        desc = random.choice(room_descs)
        if i != 0 and i != length - 1 and random.random() < enemy_chance:
            template = random.choice(enemies_data["enemies"])
            enemy = create_enemy_from_template(template)
            rooms.append(Room(tag='E', description=desc, enemy=enemy))
        else:
            if i == 0:
                tag = 'St'
            elif i == length - 1:
                tag = 'Ex'
            else:
                tag = ' '
            rooms.append(Room(tag=tag, description=desc, enemy=None))

    has_enemy = any(room.tag == 'E' for room in rooms)

    if not has_enemy:
        idx = random.randint(1, length - 2)

        template = random.choice(enemies_data["enemies"])
        enemy = create_enemy_from_template(template)

        rooms[idx].tag = 'E'
        rooms[idx].enemy = enemy

    return rooms
