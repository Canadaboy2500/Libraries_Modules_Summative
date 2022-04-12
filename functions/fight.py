import random
from presets import stats
import time
from presets import equipment as eqp

def condition(stats, name):
    if stats['health'] >= stats['health_max'] - (stats['health_max'] / 3):
        print(f"{name} still in good condition, {stats['health']} Health remaining.")
        chance = 0
    elif stats['health'] < (stats['health_max'] / 3):
        print(f"{name} in bad condition, {stats['health']} health remaining.")
        chance = 2
    else:
        print(f"{name} in decent condtion, {stats['health']} health remaining.")
        chance = 1
    if stats['endurance'] > 20:
        print(f"{name} still full of energy, {stats['endurance']} energy left.")
    elif stats['endurance'] < 5:
        print(f"{name} exhausted, can only defend, {stats['endurance']} energy left.")
    else:
        print(f"{name} starting too tire, {stats['endurance']} energy left.")
    return chance

def stumble(chance):
    miss = False
    while chance > 0:
        roll = random.randint(1,4)
        if roll == 1:
            miss = True
        chance = chance - 1
    return miss

def arena_fight(p_stats, o_stats, p_equip, o_equip):
    stumble_chance = condition(o_stats, f"{o_stats['name']} is")
    time.sleep(1)
    miss = stumble(stumble_chance)
    if miss == True:
        print(f"{o_stats['name']} misses!\n")
    else:
        ai_attack(o_stats, p_stats, o_equip, p_equip)
    if p_stats['health'] <= 0:
        print("You have died!")
    else:
        condition(p_stats, "You're")
        choice = 0
        choice = choose_attack(p_stats, choice)
        if choice == 1:
            stamina = ((p_stats['endurance_max'] / 5) + random.randint(1,5)) - random.randint(0,5)
            p_stats['endurance'] = p_stats['endurance'] + stamina
            if p_stats['endurance'] > p_stats['endurance_max']:
                p_stats['endurance'] = p_stats['endurance_max']
            print(f"{p_stats['name']} hangs back, catching their breath!")
            print(f"{p_stats['name']} recovers {stamina} points of energy!!")
        elif choice == 2:
            p_stats['endurance'] = p_stats['endurance'] - 5
            stamina = ((p_stats['endurance_max'] / 10) + random.randint(1,5)) - random.randint(0,5)
            p_stats['endurance'] = p_stats['endurance'] + stamina
            if p_stats['endurance'] > p_stats['endurance_max']:
                p_stats['endurance'] = p_stats['endurance_max']
            print(f"{p_stats['name']} makes a reserved swing!")
            o_stats = attack(o_stats, p_stats, p_equip, o_equip, 5)
            print(f"{p_stats['name']} recovers {stamina} points of energy!")
        elif choice == 3:
            p_stats['endurance'] = p_stats['endurance'] - 10
            print(f"{p_stats['name']} attacks!")
            o_stats = attack(o_stats, p_stats, p_equip, o_equip, 10)
        elif choice == 4:
            p_stats['endurance'] = p_stats['endurance'] - 20
            print(f"{p_stats['name']} lunges forward with an aggresive strike!")
            o_stats = attack(o_stats, p_stats, p_equip, o_equip, 20)
        time.sleep(1)
        if o_stats['health'] > 0:
            win = arena_fight(p_stats, o_stats, p_equip, o_equip)
        else:
            print(f"The crowd cheers as {o_stats['name']} falls to the ground with a thud, his body laying lifeless in a pool of his own blood!")
            win = True
        return(win)
        
def ai_attack(ai_stats, p_stats, ai_equip, p_equip):
    if ai_stats['endurance'] > 20:
        attack_type = random.randint(1, 2)
    elif ai_stats['endurance'] < 5:
        attack_type = 4
    elif ai_stats['endurance'] < 10:
        attack_type = random.randint(3, 4)
    else:
        attack_type = random.randint(2, 4)
    if attack_type == 1:
        ai_stats['endurance'] = ai_stats['endurance'] - 20
        print(f"{ai_stats['name']} lunges forward at you with an aggresive strike!")
        p_stats = attack(p_stats, ai_stats, ai_equip, p_equip, 20)
    elif attack_type == 2:
        ai_stats['endurance'] = ai_stats['endurance'] - 10
        print(f"{ai_stats['name']} attacks you!")
        p_stats = attack(p_stats, ai_stats, ai_equip, p_equip, 10)
    elif attack_type == 3:
        ai_stats['endurance'] = ai_stats['endurance'] - 5
        print(f"{ai_stats['name']} makes a reserved swing at you, conserving his energy!")
        stamina = ((ai_stats['endurance_max'] / 10) + random.randint(1,5)) - random.randint(0,5)
        ai_stats['endurance'] = ai_stats['endurance'] + stamina
        if ai_stats['endurance'] > ai_stats['endurance_max']:
            ai_stats['endurance'] = ai_stats['endurance_max']
        p_stats = attack(p_stats, ai_stats, ai_equip, p_equip, 5)
        print(f"{ai_stats['name']} recovers {stamina} points of energy!!")
    elif attack_type == 4:
        stamina = ((ai_stats['endurance_max'] / 5) + random.randint(1,5)) - random.randint(0,5)
        ai_stats['endurance'] = ai_stats['endurance'] + stamina
        if ai_stats['endurance'] > ai_stats['endurance_max']:
            ai_stats['endurance'] = ai_stats['endurance_max']
        print(f"{ai_stats['name']} hangs back, catching their breath!")
        print(f"{ai_stats['name']} recovers {stamina} points of energy!!")
    return(ai_stats, p_stats)

def choose_attack(stats, choice):
    max = 1
    print("1) Defend (recover energy)")
    if stats['endurance'] >= 5:
        print("2) Light attack (5 energy, gain a small amount of energy at the end of turn)")
        max = max + 1
    if stats['endurance'] >= 10:
        print("3) Standard attack (10 energy)")
        max = max + 1
    if stats['endurance'] >= 20:
        print("4) Heavy attack (20 energy)")
        max = max + 1
    print(' ')
    selected = False
    while selected == False:
        try:
            choice = int(input('> '))
            if choice == 1 or choice == 2 or choice == 3 or choice == 4:
                if choice > max:
                    print("You can't select that!")
                else:
                    selected = True
                    return(choice)
            else:
                print("That's not an option!")
        except ValueError:
            print("please input a numbered choice")
            
def try_crit(crit_attack, attack_stats):
    crit = False
    while crit_attack > 0:
        crit_hit = random.randint(1, 2)
        if crit_hit == 1:
            crit = True
        crit_attack = crit_attack - 0.5
    if crit == True:
        crit = 2
        print(f"{attack_stats['name']} lands a critical hit! Double Damage!")
    else:
        crit = 1
    return crit

def attack(defend_stats, attack_stats, attack_equip, defend_equip, energy):
    armour = defend_equip['armour']
    dmg_type = attack_equip['damage_type']
    dmg_typemult = armour[dmg_type]
    if attack_equip['handle_type'] == 'twohanded':
        handle_mult = 2.5 * attack_stats['strength'] * 0.25
        crit = try_crit(attack_stats['strength'] / (attack_stats['strength'] / 6), attack_stats) #chance the attack is a critical hit
    elif attack_equip['handle_type'] == 'onehanded':
        handle_mult = 2.5 * attack_stats['agility'] * 0.25 
        crit = try_crit(attack_stats['agility'] / 2, attack_stats) #chance the attack is a critical hit
    damage = (energy / 5) * handle_mult * dmg_typemult * crit
    if damage >= 10:
        print(f"{attack_stats['name']} strikes a mighty blow! {damage} points of health damage!")
    elif damage == 0:
        print(f"{attack_stats['name']}'s blow misses! {damage} points of health damage!")
    elif damage < 5:
        print(f"{attack_stats['name']}'s swing glances off! {damage} points of health damage!")
    else:
        print(f"{attack_stats['name']}'s attack hits its mark! {damage} points of health damage!")
    print(' ')
    time.sleep(1)
    defend_stats['health'] = defend_stats['health'] - damage
    return(defend_stats)

def arena_cycle(player_stats, player_equipment, stats, equipment, wins):
    opponent_stats = stats.pop(0)
    opponent_equipment = equipment.pop(0)
    print(f"""Today you will be fighting {opponent_stats['name']}.
Most likely he will be wearing {opponent_equipment['armour_type']}.
He is also known too wield a {opponent_equipment['weapon_name']}.\n""")
    time.sleep(2)
    eqp.equipment_select(player_equipment)
    win = arena_fight(player_stats, opponent_stats, player_equipment, opponent_equipment)
    if win == True:
        wins = wins + 1
        player_stats['health'] = player_stats['health_max']
        player_stats['endurance'] = player_stats['endurance_max']
        if wins == 5:
            print("Well you have done it prisoner, you won all 5 fights, you have earned your freedom, get out of my sight!")
        else:
            print("Congratulations on your win prisoner, now go to your cell for rest till tommorow!")
            print("You have gained some stats!")
            eqp.set_stats(player_stats, random.randint(3, 5))
            arena_cycle(player_stats, player_equipment, stats, equipment, wins)
    else:
        print("Haha! Looks like the dogs will eat good tonight!")