def test_actions_start_room(game_lite):
    game = game_lite
    game.position = game._find_start()
    actions = [a[0] for a in game.available_actions()]

    assert "Пойти дальше" in actions
    assert "Сбежать из подземелья (прервать игру)" in actions


def test_actions_exit_room(game_lite):
    game = game_lite
    game.position = len(game.rooms) - 1
    actions = [a[0] for a in game.available_actions()]

    assert "Вернуться назад" in actions
    assert "Выйти из подземелья" in actions
    assert "Сбежать из подземелья (прервать игру)" in actions


def test_actions_middle_empty_room(game_lite):
    game = game_lite

    for i in range(1, len(game.rooms) - 1):
        if not game.rooms[i].has_enemy():
            game.position = i
            break

    actions = [a[0] for a in game.available_actions()]
    assert "Пойти дальше" in actions
    assert "Вернуться назад" in actions
    assert "Сбежать из подземелья (прервать игру)" in actions
