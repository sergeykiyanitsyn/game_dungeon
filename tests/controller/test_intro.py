from rpg.controller import GameController

def test_player_intro_output(capsys, mock_input):
    mock_input("")
    game = GameController(difficulty="lite", player_name="Тестировщик")
    game.running = False
    game.run()

    captured = capsys.readouterr().out

    assert "Тестировщик" in captured
    assert "HP" in captured
    assert str(game.player.max_hp) in captured
    assert game.player.description in captured
    assert game.player.weapon.name in captured
    assert str(game.player.weapon.damage) in captured
    assert game.player.armor.name in captured
    assert str(game.player.armor.defense) in captured