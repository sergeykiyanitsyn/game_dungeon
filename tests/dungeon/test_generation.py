from rpg.dungeon import generate_dungeon_by_difficulty
import pytest

@pytest.mark.parametrize("difficulty", ["lite", "medium", "hard"])
def test_dungeon_has_enemy(difficulty):
    assert any(r.has_enemy() for r in generate_dungeon_by_difficulty(difficulty))

@pytest.mark.parametrize("difficulty, exp_rooms", [("lite", 5), ("medium", 8), ("hard", 12)])
def test_dungeon_min_length(difficulty, exp_rooms: int):
    assert len(rooms := generate_dungeon_by_difficulty(difficulty)) == exp_rooms

def test_invalid_difficulty():
    with pytest.raises(ValueError):
        generate_dungeon_by_difficulty("ultra")
