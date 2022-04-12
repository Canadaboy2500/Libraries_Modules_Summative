import time
heavy = {'slashing':0.5, 'piercing':1, 'blunt':2}
light = {'slashing':2, 'piercing':1, 'blunt':0.5}

def set_stats(player_stats, points):
    print(f"""You have {points} stat point(s) remaining.
    Please input the name of the stat you would like to increase.
    Options: health, strength, agility, endurance
    Current stats: Health:{player_stats['health']}, Strength:{player_stats['strength']}, Agility:{player_stats['agility']}, Endurance:{player_stats['endurance']}
    To see the effects of all stats, enter 'help'""")
    stat = input("> ").lower()
    if stat == "help":
        stats_info()
        points = points + 1
    elif stat == "health":
        print("Health increased by 10!\n")
        player_stats['health'] = player_stats['health'] + 10
    elif stat == "strength":
        print("Strength increased by 1!\n")
        player_stats['strength'] = player_stats['strength'] + 1
    elif stat == "agility":
        print("Agility increased by 1!\n")
        player_stats['agility'] = player_stats['agility'] + 1
    elif stat == "endurance":
        print("Endurance increased by 5!\n")
        player_stats['endurance'] = player_stats['endurance'] + 5
    else:
        print("sorry I didn't catch that.\n")
        points = points + 1
    time.sleep(1)
    points = points - 1
    #player_stats = {'health':health, 'strength':strength, 'agility':agility, 'endurance':endurance, 'intelligence':intelligence}
    if points > 0:
        player_stats = set_stats(player_stats, points)
    player_stats['health_max'] = player_stats['health']
    player_stats['endurance_max'] = player_stats['endurance']
    return player_stats

def stats_info():
    print("""each stat affects certain aspects of your gameplay.
The Health stat determines your health points(HP) and your health regeneration.
    you start with 100 health, each stat increases it by 10!""")
    time.sleep(2)
    print("""The Strength stat determines how much damage your attacks can do,
    as well as your skill with heavy weapons.""")
    time.sleep(2)
    print("""The Agility stat determines the chance of you hitting your opponent and dodging their attacks,
    it also determines your effectivness with light weapons.""")
    time.sleep(2)
    print("""The Endurance stat determines how much energy you have, and how quickly you regain it,
    you start with 50 energy, and every stat increases it by 5.""")
    time.sleep(2)

def equipment_info():
    print("""There is two classes of armour, Light, and Heavy
    Heavy armour is strong against slashing weapons and weak against blunt weapons.
    Light armour is strong against blunt weapons and weak against slashing weapons.""")
    time.sleep(2)
    print("""Weapons come in two classes, one-handed and two-handed.
    Two-handed weapons are influenced by your strength stat.
    One-handed weapons are influenced by your agility stat.""")
    time.sleep(2)
    print("""All weapons deal a certain type of damage that varies in effectivness.
    Swords and axes deal slashing damage which is effective against light armour.
    Maces and bludgeons deal blunt damage which is effective against heavy armour.
    Spears and pikes deal piercing damage, which is mildly effective against all armour types""")
    
def equipment_select(equipment):
    print("Would you like an explanation of how different equipment interacts?")
    choice = input('> ').lower()
    if choice == 'yes' or choice == 'y':
        equipment_info()
    selected = False
    while selected == False:
        print("Do you choose heavy or light armour?")
        choice = input('> ').lower()
        if choice == 'heavy':
            print("Standard issue forged steel, you won't fall to even the mightiest blows!\n")
            equipment['armour'] = heavy
            selected = True
        elif choice == 'light':
            print("Leather, nice and light, you'll run circles around your enemy\n")
            equipment['armour'] = light
            selected = True
        else:
            print("I asked you a question! answer properly!")
    selected = False
    time.sleep(1.5)
    while selected == False:
        print("""What weapon will you wield?
Haliberd:(Two-handed, Slashing)
Short Sword:(One-handed, Slashing)
Warhammer:(Two-handed, Blunt)
Club:(One-handed, Blunt)
Infantry Pike:(Two-handed, Piercing)
Light Spear:(One-handed, Piercing)""")
        choice = input('> ').lower()
        selected = True
        if choice == 'haliberd':
            equipment['damage_type'] = 'slashing'
            equipment['handle_type'] = 'twohanded'
        elif choice == 'short sword':
            equipment['damage_type'] = 'slashing'
            equipment['handle_type'] = 'onehanded'
        elif choice == 'warhammer':
            equipment['damage_type'] = 'blunt'
            equipment['handle_type'] = 'twohanded'
        elif choice == 'club':
            equipment['damage_type'] = 'blunt'
            equipment['handle_type'] = 'onehanded'
        elif choice == 'infantry pike':
            equipment['damage_type'] = 'piercing'
            equipment['handle_type'] = 'twohanded'
        elif choice == 'light spear':
            equipment['damage_type'] = 'piercing'
            equipment['handle_type'] = 'onehanded'
        else:
            selected = False
            print("imaginary weapons won't help you in the arena comrade.")
        print("Excellent choice, may it serve you well.\n")
        time.sleep(2)
    return equipment