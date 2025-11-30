from rpg.loader import load_players, load_enemies, load_weapons, load_armors, load_rooms

def test_load_players():
    players = load_players()
    assert "names" in players
    assert "base" in players
    assert "descriptions" in players
    assert "death_descriptions" in players
    assert players["base"]["hp"] == 10
    assert "weapon" in players["base"]
    assert "armor" in players["base"]

def test_load_enemies():
    enemies = load_enemies()
    assert "enemies" in enemies
    assert len(enemies["enemies"])>=1
    assert enemies["enemies"][0]["hp"] > 0

def test_load_weapons_and_armors():
    weapons = load_weapons()
    armors = load_armors()
    assert isinstance(weapons["weapons"], list)
    assert isinstance(armors["armors"], list)

    weapon = weapons["weapons"][0]
    armor = armors["armors"][0]
    assert "name" in weapon and "damage" in weapon and "hit_chance" in weapon
    assert "name" in armor and "defense" in armor

def test_load_rooms():
    rooms = load_rooms()
    assert "room_descriptions" in rooms
    assert len(rooms["room_descriptions"])>0
