import sys
from rpg.controller import GameController

def main():
    if len(sys.argv) > 1:
        difficulty = sys.argv[1].lower()
    else:
        difficulty = "lite"

    game = GameController(difficulty=difficulty)
    game.run()

if __name__=="__main__":
    main()
