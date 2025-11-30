def test_input_invalid_symbol(game_lite, mock_input, capsys):
    game = game_lite
    mock_input("abc")
    assert game.input_action() is None
    assert "Некорректный ввод" in capsys.readouterr().out


def test_input_valid_number(game_lite, mock_input):
    game = game_lite

    mock_input("1")
    action = game.input_action()
    assert action in [a[1] for a in game.available_actions()]


def test_input_ctrl_c(game_lite, monkeypatch):
    def raise_kb(_): raise KeyboardInterrupt
    monkeypatch.setattr("builtins.input", raise_kb)

    action = game_lite.input_action()
    assert action == game_lite.available_actions()[-1][1]
    assert game_lite.running is False
