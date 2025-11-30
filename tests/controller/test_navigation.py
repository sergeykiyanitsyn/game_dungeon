def test_forward_movement(game_lite, capsys):
    game = game_lite
    start = game.position

    game.handle_action("forward")
    assert game.position == start + 1


def test_back_movement(game_lite):
    game = game_lite
    game.position = 1
    game.handle_action("back")
    assert game.position == 0


def test_exit_action(game_lite):
    game = game_lite
    game.position = len(game.rooms) - 1
    game.handle_action("exit")
    assert game.running is False
