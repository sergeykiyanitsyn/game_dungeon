from rpg.combat import autobattle
from rpg.controller import GameController
from rpg.entities import Combatant, Weapon, Armor, Room


def test_autobattle_win(weak_enemy):
    hero = Combatant("Герой", 10, 10, Weapon("Sword","Хороший меч", 5, 100), Armor("Cloth","Старая одежка", 0))
    result = autobattle(hero, weak_enemy, verbose=False)
    assert result["winner"] is hero


def test_autobattle_lose(strong_enemy):
    hero = Combatant("Герой", 1, 1, Weapon("Палка-выручалка","Хрупкая палка" , 1, 1), Armor("Пусто","Голый", 0))
    result = autobattle(hero, strong_enemy, verbose=False)
    assert result["winner"] is strong_enemy

def test_player_death_prints_message(capsys,weak_enemy, strong_enemy):
    game = GameController(difficulty="lite", player_name="Hero")
    game.player = weak_enemy

    game.rooms[0] = Room(tag="St", description="Test room", enemy=strong_enemy)
    game.handle_action("attack")

    output = capsys.readouterr().out
    assert "погибли" in output or "Игра окончена" in output
    assert game.running is False