import random
import time

from .entities import Combatant

def _calc_damage(attacker: Combatant, defender: Combatant) -> int:
    dmg = attacker.weapon.damage - defender.armor.defense
    if dmg > 0:
        return dmg
    else:
        return 0

def _hit_succeeds(chance_percent: int) -> bool:
    return chance_percent >= random.randint(0,100)


def autobattle(player: Combatant, enemy: Combatant, verbose: bool = True):
    if verbose:
        print(f"Бой начинается: {player.name} (HP {player.hp}/{player.max_hp}) vs {enemy.name} (HP {enemy.hp}/{enemy.max_hp})")
        print()
        time.sleep(3)

    attacker, defender = player, enemy

    while player.is_alive() and enemy.is_alive():
        if verbose:
            print(f"{attacker.name} готовится атаковать {defender.name}.")
            time.sleep(3)

        hit = _hit_succeeds(attacker.weapon.hit_chance)

        if hit:
            dmg = _calc_damage(attacker, defender)
            defender.take_damage(dmg)

            if verbose:
                print(f"{attacker.name} попал! Нанёс {dmg} урона. У {defender.name} осталось HP {defender.hp}/{defender.max_hp}.")
                time.sleep(3)

            if not defender.is_alive() and verbose:
                death = getattr(defender, "death_description", None)
                if death:
                    print(death)
                else:
                    print(f"{defender.name} погиб.")
                time.sleep(3)
        else:
            if verbose:
                print(f"{attacker.name} промахнулся.")
                time.sleep(3)

        attacker, defender = defender, attacker

    if player.is_alive():
        winner = player
        loser = enemy
    else:
        winner = enemy
        loser = player

    return {"winner": winner, "loser": loser}


