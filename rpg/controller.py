from typing import List
from .dungeon import generate_dungeon_by_difficulty, create_player
from .combat import autobattle
from .entities import Room

class GameController:
    def __init__(self, difficulty: str = 'lite', player_name: str = None):
        self.rooms: List[Room] = generate_dungeon_by_difficulty(difficulty)
        self.player = create_player(player_name)
        self.position = self._find_start()
        self.running = True

    def _find_start(self):
        for idx, r in enumerate(self.rooms):
            if r.tag == "St":
                return idx
        return 0

    def current_room(self) -> Room:
        return self.rooms[self.position]

    def available_actions(self):
        room = self.current_room()
        actions=[]
        if room.has_enemy():
            actions.append(("Атаковать","attack"))
        if not room.has_enemy():
            if room.tag!="Ex":
                actions.append(("Пойти дальше","forward"))
            if room.tag!="St":
                actions.append(("Вернуться назад","back"))
        if room.tag=="Ex":
            actions.append(("Выйти из подземелья","exit"))
        actions.append(("Сбежать из подземелья (прервать игру)","quit"))
        return actions

    def print_current_state(self):
        room = self.current_room()
        print()
        print(f"Комната ({self.position+1}/{len(self.rooms)}): {room.description}")
        if room.has_enemy():
            e = room.enemy
            print(f"Здесь находится противник: {e.name} (HP {e.hp}/{e.max_hp}). {e.description}")
        else:
            print("Комната пуста.")
        print()

    def input_action(self):
        actions = self.available_actions()
        print("Вы можете:")
        for i,(label,_) in enumerate(actions,start=1):
            print(f"{i}. {label}")

        try:
            choice = input("Ваше действие: ").strip()
            num=int(choice)
            if 1<=num<=len(actions):
                return actions[num-1][1]

        except KeyboardInterrupt:
            self.running = False
            return actions[-1][1]

        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
        return None


    def handle_action(self, action: str):
        room=self.current_room()
        if action=="attack":
            autobattle(self.player, room.enemy, verbose=True)
            if not self.player.is_alive():
                death_texts=self.player.death_descriptions or []
                if death_texts:
                    import random
                    print(random.choice(death_texts))
                print("Игра окончена — вы погибли.")
                self.running=False
            else:
                print(f"Вы победили {room.enemy.name}!")
        elif action=="forward":
            if self.position+1<len(self.rooms):
                self.position+=1
                print("Вы двигаетесь вперёд...")
            else:
                print("Дальше идти некуда.")
        elif action=="back":
            if self.position>0:
                self.position-=1
                print("Вы возвращаетесь назад...")
            else:
                print("Назад идти нельзя.")
        elif action=="exit":
            print("Вы уходите из подземелья. Игра завершена.")
            self.running=False
        elif action=="quit":
            print("Игра прервана пользователем.")
            self.running=False
        else:
            print("Неизвестное действие.")

    def run(self):
        print("=== Добро пожаловать в текстовую RPG ===")

        print(f"\nВашего персонажа зовут {self.player.name}. Вы полностью здоровы: {self.player.hp}/{self.player.max_hp} HP.")
        print(f"{self.player.description}")
        print(f"\nВаш инвентарь: \nОружие: {self.player.weapon.name} (урон {self.player.weapon.damage})")
        print(f"Броня: {self.player.armor.name} (защита {self.player.armor.defense})")

        print("\nВаша задача - дойти до конца подземелья и спасти принцессу. Удачной игры! ")

        try:
            input("\nНажмите Enter, чтобы войти в подземелье...")
        except KeyboardInterrupt:
            self.running = False

        while self.running:
            self.print_current_state()
            action=None
            while action is None and self.running:
                action=self.input_action()
            self.handle_action(action)
        print("\n=== Игра завершена ===")
