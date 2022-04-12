#-----------------------------------------
# Libraries and Modules Summative.py
# Mason Skinner
# April 12, 2022
#-----------------------------------------
from presets import equipment as eqp
from presets import stats
from functions import fight as ft
import time
import random

def main():
    print("""Wake up prisoner!
It's your lucky day, you've been selected to have a chance at freedom.
Over the next week you will partake in 5 fights.
If you win them all, you'll be set free, pardoned of all crimes.
If you lose, well, your body will be good eating for the dogs!
""")
    print("What is your name?")
    stats.player_stats['name'] = input('> ')
    eqp.player_stats = eqp.set_stats(stats.player_stats, 10)
    print("""Look sharp prisoner!
My name is Roderic, it's my job to ensure your properly equipped for your fights,
the people want a spectacle, not a slaughter.
You better choose some gear fast, your first fight is going too begin within the hour.
""")
    ft.arena_cycle(stats.player_stats, stats.player_equipment, stats.stats, stats.equipment, 0)

#----------------------------------


main()