# Roll a random DnD Character

# Import random number generator
import random

# Choose a race and class
playerRace = ["Aaracokra", "Dragonborn", "Dwarf", "Elf", "Genasi", "Gnome", "Goliath", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]
playerRace = random.choice(playerRace)
playerClass = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
playerClass = random.choice(playerClass)
print(f"Your character's race is {playerRace}. \nYour character's class is {playerClass}.")

# Roll for stats
# Generate dice
dice = [1, 2, 3, 4, 5, 6]
# Generate list for stats
stats = []
# Track number of rolls
numberOfRolls = 0
while numberOfRolls < 6:
    # Roll 4d6 drop lowest
    rolls = [random.choice(dice), random.choice(dice), random.choice(dice), random.choice(dice)]
    rolls.sort()
    trait = rolls[1] + rolls[2] + rolls[3]
    # Add to list of stats
    stats.append(trait)
    numberOfRolls = numberOfRolls + 1
# Sort and print
stats.sort()
print(f"Your character's stats are {stats}. \nHave fun with your new character!")
