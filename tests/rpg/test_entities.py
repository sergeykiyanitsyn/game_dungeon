from rpg.entities import Weapon, Armor, Combatant, Room

def test_weapon_entity():
    w = Weapon("Меч", "Од да какой острый", 5, 80)
    assert w.damage == 5
    assert w.hit_chance == 80

def test_armor_entity():
    a = Armor("Латы", "О, это база", 2)
    assert a.defense == 2

def test_combatant_alive():
    c = Combatant("Герой", 5, 5, Weapon("W", "", 1, 100), Armor("A", "", 0))
    assert c.is_alive()
    c.take_damage(10)
    assert c.hp == 0
    assert not c.is_alive()

def test_room_entity():
    r = Room("St", "Тестовая комната", None)
    assert not r.has_enemy()
