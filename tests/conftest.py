import pytest
from rpg.controller import GameController
from rpg.entities import Combatant, Weapon, Armor

@pytest.fixture
def game_lite():
    return GameController(difficulty="lite", player_name="Tester")

@pytest.fixture
def game_medium():
    return GameController(difficulty="medium", player_name="Tester")

@pytest.fixture
def game_hard():
    return GameController(difficulty="hard", player_name="Tester")

@pytest.fixture
def mock_input(monkeypatch):
    def setter(value):
        monkeypatch.setattr("builtins.input", lambda _: value)
    return setter

@pytest.fixture
def weak_enemy():
    return Combatant(
        name="Гуляка",
        hp=1,
        max_hp=1,
        weapon=Weapon("Палка", "Обычная палка", 1, 100),
        armor=Armor("Пусто","Голый", 0),
        description="Слабак",
        death_descriptions= "Умирать надо красиво"
    )

@pytest.fixture
def strong_enemy():
    return Combatant(
        name="Орк",
        hp=20,
        max_hp=20,
        weapon=Weapon("Дубина","Оружие с гвоздями", 10, 100),
        armor=Armor("Клжа","Обычная кожанная одежка", 0),
        description="Серьезный враг"
    )
