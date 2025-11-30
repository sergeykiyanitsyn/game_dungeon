import pytest

from rpg.dungeon import generate_dungeon_by_difficulty

@pytest.mark.parametrize("difficulty", ["lite", "medium", "hard"])
def test_room_descriptions_exist(difficulty):
    rooms = generate_dungeon_by_difficulty(difficulty)
    for r in rooms:
        assert isinstance(r.description, str)
        assert len(r.description.strip()) > 0

@pytest.mark.parametrize("difficulty", ["lite", "medium", "hard"])
def test_enemy_description_format(difficulty):
    rooms = generate_dungeon_by_difficulty(difficulty)

    for r in rooms:
        if r.has_enemy():
            e = r.enemy
            assert isinstance(e.name, str)
            assert e.hp > 0
            assert isinstance(e.description, str)
            break
    else:
        assert False, f"В {difficulty} не найдено ни одной комнаты с врагом"
