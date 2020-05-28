# Roll a random DnD Character

# Import random number generator
import random
# Import math
import math

# Choose a race and class
playerRace = ["Aaracokra", "Dragonborn", "Dwarf", "Elf", "Genasi", "Gnome", "Goliath", "Half-Elf", "Halfling",
              "Half-Orc", "Human", "Tiefling"]
playerRace = random.choice(playerRace)
playerClass = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer",
               "Warlock", "Wizard"]
playerClass = random.choice(playerClass)

# Alignment
playerAlignment = ["Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil",
                   "Chaotic Good", "Chaotic Neutral", "Chaotic Evil", ]
playerAlignment = random.choice(playerAlignment)

# Backgrounds
playerBackground = ["Acolyte", "Charlatan", "Criminal/Spy",
                    "Entertainer", "Folk Hero", "Guild Artisan/Guild Merchant",
                    "Hermit", "Knight", "Outlander",
                    "Pirate", "Sage", "Sailor",
                    "Soldier", "Urchin"]
playerBackground = random.choice(playerBackground)

"""
Lists for Weapons and Packs
"""

simpleWeapons = ["Club", "Dagger", "Greatclub", "Handaxe",
                 "Javelin", "Light Hammer", "Mace", "Quarterstaff",
                 "Sickle", "Spear", "Light Crossbow", "Dart", "Shortbow", "Sling"]

martialMeleeWeapons = ["Battleaxe", "Flail", "Glaive", "Greataxe",
                       "Greatsword", "Halberd", "Lance", "Longsword",
                       "Maul", "Morningstar", "Pike", "Rapier",
                       "Scimitar", "Shortsword", "Trident", "War Pick",
                       "Warhammer", "Whip"]

martialWeapons = ["Battleaxe", "Flail", "Glaive", "Greataxe",
                  "Greatsword", "Halberd", "Lance", "Longsword",
                  "Maul", "Morningstar", "Pike", "Rapier",
                  "Scimitar", "Shortsword", "Trident", "War Pick",
                  "Warhammer", "Whip", "Blowgun", "Hand Crossbow",
                  "Heavy Crossbow", "Longbow", "Net"]

simpleMeleeWeapons = ["Club", "Dagger", "Greatclub", "Handaxe",
                      "Javelin", "Light Hammer", "Mace", "Quarterstaff",
                      "Sickle", "Spear"]

explorersPack = ["Backpack", "Bedroll", "Mess kit",
                 "Tinderbox", "Torches(10)", "Rations(10)",
                 "Waterskin", "Hempen rope(50ft)"]

diplomatsPack = ["Chest", "Cases for Maps and Scrolls(2)", "Set of Fine Clothes",
                 "Bottle of Ink", "Ink Pen", "Lamp",
                 "Flasks of Oil(2)", "Sheets of Paper(5)", "Vial of Perfume",
                 "Sealing wax", "Soap"]

entertainersPack = ["Backpack", "Bedroll", "Costumes(2)", "Candles(5)", "Rations(5)", "Waterskin", "Disguise Kit"]

priestsPack = ["Backpack", "Blanket", "Candles(10)",
               "Tinderbox", "Alms box", "Blocks of Incense(2)",
               "Censer", "Vestments", "Rations(2)", "Waterskin"]

dungeoneersPack = ["Backpack", "Crowbar", "Hammer",
                   "Piton(10)", "Torches(10)", "Tinderbox",
                   "Rations(10)", "Waterskin", "Hempen Rope"]

burglarsPack = ["Backpack", "A Bag of 1000 Ball Bearings", "10 feet of string", "Bell",
                "Candles(5)", "Crowbar", "Hammer", "Pitons(10)",
                "Hooded Lantern", "Flasks of Oil(2)", "Rations(5)", "Tinderbox",
                "Waterskin", "Hempen Rope(50 ft)"]

scholarsPack = ["Backpack", "Book of Lore", "Bottle of Ink",
                "Ink Pen", "Sheets of Parchment(10)", "Little Bag of Sand",
                "Small Knife"]

musicalInstruments = ["Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn", "Pan flute", "Shawm"]

"""
List of Languages
"""
languages = ["Common", "Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc",
             "Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon"]

# Assign variables
# Assign all stats to 0 by default.
strength = 0
dexterity = 0
constitution = 0
intelligence = 0
wisdom = 0
charisma = 0

# Defining Proficiency Bonus
proficiency = 2

# Assign player level
playerLevel = 1

# Roll for stats
dice = [1, 2, 3, 4, 5, 6]

# Generate list for stats
stats = []

# Track number of rolls
numberOfRolls = 0

# Roll until 6 stats are rolled
while numberOfRolls < 6:
    # Roll 4d6
    rolls = [random.choice(dice), random.choice(dice), random.choice(dice), random.choice(dice)]
    # Sort from lowest to highest
    rolls.sort()
    # Include only the first three rolls in the array
    array = rolls[1] + rolls[2] + rolls[3]
    # Add to list of stats
    stats.append(array)
    # Count one more roll
    numberOfRolls = numberOfRolls + 1

# Sort the stats from lowest to greatest
stats.sort()

#  Generate List for Skills
skills = []

# Define number of skills
numberOfSkills = 0

# Define background skills
bgSkillOne = "null"
bgSkillTwo = "null"

# Define Base Hit Points
baseHitPoints = 0

# Generate List for Equipment
equipment = []

# Choosing what stats go where depending on class
"""
Class specific additions, such as stats and saving throw proficiencies
"""
savingThrowOne, savingThrowTwo = "null", "null"
# Barbarian
if playerClass == "Barbarian":
    strength = stats[5]
    dexterity = stats[3]
    constitution = stats[4]
    intelligence = stats[0]
    wisdom = stats[2]
    charisma = stats[1]
    savingThrowOne, savingThrowTwo = "Strength", "Constitution"
    # Class Skills
    skills = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
    numberOfSkills = 2
    baseHitPoints = 12

    # Equipment

    # Main Weapon
    barbarianWeapon = random.randint(1, 2)
    if barbarianWeapon == 1:
        equipment.append("Greataxe")
    if barbarianWeapon == 2:
        equipment.append(random.choice(martialMeleeWeapons))

    # Secondary Weapon
    barbarianSecondWeapon = random.randint(1, 2)
    if barbarianSecondWeapon == 1:
        equipment.append("Handaxe(2)")
    if barbarianSecondWeapon == 2:
        equipment.append(random.choice(simpleWeapons))

    # Four Javelins
    equipment.append("Javelin(4)")

    # Explorer's Pack
    equipment.extend(explorersPack)

# Bard
if playerClass == "Bard":
    strength = stats[0]
    dexterity = stats[4]
    constitution = stats[3]
    intelligence = stats[1]
    wisdom = stats[2]
    charisma = stats[5]
    savingThrowOne, savingThrowTwo = "Dexterity", "Charisma"
    # Class Skills
    skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History",
              "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception",
              "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
    numberOfSkills = 3
    baseHitPoints = 8

    # Equipment

    # Main Weapon
    bardWeapon = random.randint(1, 3)
    if bardWeapon == 1:
        equipment.append("Greataxe")
    if bardWeapon == 2:
        equipment.append("Longsword")
    if bardWeapon == 3:
        equipment.append(random.choice(simpleWeapons))

    # Pack
    bardPack = random.randint(1, 2)
    if bardPack == 1:
        equipment.extend(diplomatsPack)
    if bardPack == 2:
        equipment.extend(entertainersPack)

    # Instrument
    equipment.append(random.choice(musicalInstruments))

    # Leather Armor and Dagger
    equipment.extend(["Leather Armor", "Dagger"])

# Cleric
clericDomains = ["Arcana", "Death", "Forge",
                 "Grave", "Knowledge", "Life",
                 "Light", "Nature", "Order",
                 "Tempest", "Trickery", "War"]
playerDomain = 0
clericSub = random.randint(1, 3)
if playerClass == "Cleric":
    if clericSub == 1:
        strength = stats[1]
        dexterity = stats[4]
        constitution = stats[3]
        intelligence = stats[0]
        wisdom = stats[5]
        charisma = stats[2]
    if clericSub == 2:
        strength = stats[1]
        dexterity = stats[3]
        constitution = stats[2]
        intelligence = stats[0]
        wisdom = stats[5]
        charisma = stats[2]
    if clericSub == 3:
        strength = stats[4]
        dexterity = stats[1]
        constitution = stats[3]
        intelligence = stats[0]
        wisdom = stats[5]
        charisma = stats[2]
    savingThrowOne, savingThrowTwo = "Wisdom", "Charisma"
    # Class Skills
    skills = ["History", "Insight", "Medicine", "Persuasion", "Religion"]
    numberOfSkills = 2

    # Randomly choose Domain
    playerDomain = random.choice(clericDomains)

    baseHitPoints = 8

    # Equipment

    # Main Weapon
    clericWeapon = random.randint(1, 2)
    if clericWeapon == 1:
        equipment.append("Mace")
    if clericWeapon == 2:
        equipment.append("Warhammer")

    # Armor
    clericArmor = random.randint(1, 3)
    if clericArmor == 1:
        equipment.append("Scale Mail")
    if clericArmor == 2:
        equipment.append("Leather Armor")
    if clericArmor == 3:
        equipment.append("Chain Mail")

    # Secondary Weapon
    clericWeaponTwo = random.randint(1, 2)
    if clericWeaponTwo == 1:
        equipment.extend(["Light Crossbow", "Bolts(20)"])
    if clericWeaponTwo == 2:
        equipment.append(random.choice(simpleWeapons))

    # Pack
    clericPack = random.randint(1, 2)
    if clericPack == 1:
        equipment.extend(priestsPack)
    if clericPack == 2:
        equipment.extend(explorersPack)

    # Shield and Holy Symbol
    equipment.extend(["Shield", "Holy Symbol"])

# Druid
if playerClass == "Druid":
    strength = stats[1]
    dexterity = stats[3]
    constitution = stats[4]
    intelligence = stats[2]
    wisdom = stats[5]
    charisma = stats[0]
    savingThrowOne, savingThrowTwo = "Intelligence", "Wisdom"
    # Class Skills
    skills = ["Animal Handling", "Arcana", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"]
    numberOfSkills = 2
    baseHitPoints = 8

    # Equipment

    # Main Weapon
    druidWeapon = random.randint(1, 2)
    if druidWeapon == 1:
        equipment.append("Wooden Shield")
    if druidWeapon == 2:
        equipment.append(random.choice(simpleWeapons))

    # Secondary Weapon
    druidWeaponTwo = random.randint(1, 2)
    if druidWeaponTwo == 1:
        equipment.append("Scimitar")
    if druidWeaponTwo == 2:
        equipment.append(random.choice(simpleMeleeWeapons))

    # Pack
    equipment.extend(explorersPack)

    # Armor and Focus
    equipment.extend(["Leather Armor", "Druidic Focus"])

# Fighter
fighterSub = random.randint(1, 2)
if playerClass == "Fighter":
    if fighterSub == 1:
        strength = stats[5]
        dexterity = stats[2]
        constitution = stats[4]
        intelligence = stats[0]
        wisdom = stats[3]
        charisma = stats[1]
    if fighterSub == 2:
        strength = stats[2]
        dexterity = stats[5]
        constitution = stats[4]
        intelligence = stats[0]
        wisdom = stats[3]
        charisma = stats[1]
    savingThrowOne, savingThrowTwo = "Strength", "Constitution"
    # Class Skills
    skills = ["Acrobatics", "Animal Handling", "Athletics", "History",
              "Insight", "Intimidation", "Perception", "Survival"]
    numberOfSkills = 2
    baseHitPoints = 10

    # Equipment

    # Armor
    fighterArmor = random.randint(1, 2)
    if fighterArmor == 1:
        equipment.append("Chain Mail")
    if fighterArmor == 2:
        equipment.extend(["Leather Armor", "Longbow", "Arrows(20)"])

    # Primary Weapon
    fighterWeapon = random.randint(1, 2)
    if fighterWeapon == 1:
        equipment.append(random.choice(martialWeapons))
        equipment.append("Shield")
    if fighterWeapon == 2:
        equipment.append(random.choice(martialWeapons))
        equipment.append(random.choice(martialWeapons))

    # Secondary Weapon
    fighterWeaponTwo = random.randint(1, 2)
    if fighterWeaponTwo == 1:
        equipment.extend(["Light Crossbow", "Bolts(20)"])
    if fighterWeaponTwo == 2:
        equipment.append("Handaxe(2)")

    # Pack
    fighterPack = random.randint(1, 2)
    if fighterPack == 1:
        equipment.extend(dungeoneersPack)
    if fighterPack == 2:
        equipment.extend(explorersPack)

# Monk
if playerClass == "Monk":
    strength = stats[2]
    dexterity = stats[5]
    constitution = stats[3]
    intelligence = stats[0]
    wisdom = stats[4]
    charisma = stats[1]
    savingThrowOne, savingThrowTwo = "Strength", "Dexterity"
    # Class Skills
    skills = ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]
    numberOfSkills = 2
    baseHitPoints = 8

    # Equipment

    # Primary Weapon
    monkWeapon = random.randint(1, 2)
    if monkWeapon == 2:
        if monkWeapon == 1:
            equipment.append("Shortsword")
        equipment.append(random.choice(simpleWeapons))

    # Pack
    monkPack = random.randint(1, 2)
    if monkPack == 1:
        equipment.extend(dungeoneersPack)
    if monkPack == 2:
        equipment.extend(explorersPack)

    # Darts
    equipment.append("10 darts")

# Paladin
paladinSub = random.randint(1, 2)
if playerClass == "Paladin":
    if paladinSub == 1:
        strength = stats[4]
        dexterity = stats[1]
        constitution = stats[3]
        intelligence = stats[0]
        wisdom = stats[2]
        charisma = stats[5]
    if paladinSub == 2:
        strength = stats[1]
        dexterity = stats[4]
        constitution = stats[3]
        intelligence = stats[0]
        wisdom = stats[2]
        charisma = stats[5]
    savingThrowOne, savingThrowTwo = "Wisdom", "Charisma"
    # Class Skills
    skills = ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"]
    numberOfSkills = 2
    baseHitPoints = 10

    # Equipment

    # Main Weapon
    paladinWeapon = random.randint(1, 2)
    if paladinWeapon == 1:
        equipment.append(random.choice(martialWeapons))
        equipment.append("Shield")
    if paladinWeapon == 2:
        equipment.append(random.choice(martialWeapons))
        equipment.append(random.choice(martialWeapons))

    # Secondary Weapon
    paladinWeaponTwo = random.randint(1, 2)
    if paladinWeaponTwo == 1:
        equipment.append("Five Javelins")
    if paladinWeaponTwo == 2:
        equipment.append(random.choice(simpleWeapons))

    # Pack
    paladinPack = random.randint(1, 2)
    if paladinPack == 1:
        equipment.extend(priestsPack)
    if paladinPack == 2:
        equipment.extend(explorersPack)

    # Shield and Holy Symbol
    equipment.extend(["Chain Mail", "Holy Symbol"])

# Ranger
if playerClass == "Ranger":
    strength = stats[1]
    dexterity = stats[5]
    constitution = stats[4]
    intelligence = stats[2]
    wisdom = stats[3]
    charisma = stats[0]
    savingThrowOne, savingThrowTwo = "Strength", "Dexterity"
    # Class Skills
    skills = ["Animal Handling", "Athletics", "Insight", "Intimidation", "Nature", "Perception", "Stealth", "Survival"]
    numberOfSkills = 3
    baseHitPoints = 10

    # Equipment

    # Armor
    rangerArmor = random.randint(1, 2)
    if rangerArmor == 1:
        equipment.append("Scale Mail")
    if rangerArmor == 2:
        equipment.append("Leather Armor")

    # Weapon
    rangerWeapon = random.randint(1, 2)
    if rangerWeapon == 1:
        equipment.append("Shortsword(2)")
    if rangerWeapon == 2:
        equipment.append(random.choice(simpleMeleeWeapons))
        equipment.append(random.choice(simpleMeleeWeapons))

    # Pack
    rangerPack = random.randint(1, 2)
    if rangerPack == 1:
        equipment.extend(dungeoneersPack)
    if rangerPack == 2:
        equipment.extend(explorersPack)

    # Longbow and Arrows
    equipment.extend(["Longbow", "Quiver of Arrows(20)"])

# Rogue
if playerClass == "Rogue":
    strength = stats[0]
    dexterity = stats[5]
    constitution = stats[3]
    intelligence = stats[1]
    wisdom = stats[2]
    charisma = stats[4]
    savingThrowOne, savingThrowTwo = "Dexterity", "Intelligence"
    # Class Skills
    skills = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception",
              "Performance", "Persuasion", "Sleight of Hand", "Stealth"]
    numberOfSkills = 4
    baseHitPoints = 8

    # Equipment

    # Weapon
    rogueWeapon = random.randint(1, 2)
    if rogueWeapon == 1:
        equipment.append("Rapier")
    if rogueWeapon == 2:
        equipment.append("Shortsword")

    # Secondary Weapon
    rogueWeaponTwo = random.randint(1, 2)
    if rogueWeaponTwo == 1:
        equipment.extend(["Shortbow", "Quiver of Arrows(20)"])
    if rogueWeaponTwo == 2:
        equipment.append("Shortsword")

    # Pack
    roguePack = random.randint(1, 3)
    if roguePack == 1:
        equipment.extend(burglarsPack)
    if roguePack == 2:
        equipment.extend(dungeoneersPack)
    if roguePack == 3:
        equipment.extend(explorersPack)

    # Extras
    equipment.extend(["Leather Armor", "Dagger(2)", "Thieves' Tools"])

# Sorcerer
sorcererOrigins = ["Draconic Bloodline", "Wild Magic"]
playerOrigin = 0
if playerClass == "Sorcerer":
    strength = stats[0]
    dexterity = stats[4]
    constitution = stats[3]
    intelligence = stats[1]
    wisdom = stats[2]
    charisma = stats[5]
    savingThrowOne, savingThrowTwo = "Constitution", "Charisma"

    # Randomly choose origin
    playerOrigin = random.choice(sorcererOrigins)
    # Class Skills
    skills = ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]
    numberOfSkills = 2
    baseHitPoints = 6

    # Equipment

    # Weapon
    sorcererWeapon = random.randint(1, 2)
    if sorcererWeapon == 1:
        equipment.extend(["Light Crossbow", "Bolts(20)"])
    if sorcererWeapon == 2:
        equipment.append(random.choice(simpleWeapons))

    # Focus
    sorcererFocus = random.randint(1, 2)
    if sorcererFocus == 1:
        equipment.append("Component Pouch")
    if sorcererFocus == 2:
        equipment.append("Arcane Focus")

    # Pack
    sorcererPack = random.randint(1, 2)
    if sorcererPack == 1:
        equipment.extend(dungeoneersPack)
    if sorcererPack == 2:
        equipment.extend(explorersPack)

    # Extras
    equipment.append("Dagger(2)")

# Warlock
warlockPatron = ["Archfey", "The Fiend", "The Old Great One"]
playerPatron = 0
if playerClass == "Warlock":
    strength = stats[0]
    dexterity = stats[3]
    constitution = stats[4]
    intelligence = stats[2]
    wisdom = stats[1]
    charisma = stats[5]
    savingThrowOne, savingThrowTwo = "Wisdom", "Charisma"

    # Randomly choose Patron
    playerPatron = random.choice(warlockPatron)
    # Class Skills
    skills = ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]
    numberOfSkills = 2
    baseHitPoints = 8

    # Equipment

    # Weapon
    warlockWeapon = random.randint(1, 2)
    if warlockWeapon == 1:
        equipment.extend(["Light Crossbow", "Bolts(20)"])
    if warlockWeapon == 2:
        equipment.append(random.choice(simpleWeapons))

    # Focus
    warlockFocus = random.randint(1, 2)
    if warlockFocus == 1:
        equipment.append("Component Pouch")
    if warlockFocus == 2:
        equipment.append("Arcane Focus")

    # Pack
    warlockPack = random.randint(1, 2)
    if warlockPack == 1:
        equipment.extend(scholarsPack)
    if warlockPack == 2:
        equipment.extend(dungeoneersPack)

    # Extras
    equipment.extend(["Leather Armor", "Dagger(2)"])
    equipment.append(random.choice(simpleWeapons))

# Wizard
if playerClass == "Wizard":
    strength = stats[0]
    dexterity = stats[4]
    constitution = stats[3]
    intelligence = stats[5]
    wisdom = stats[2]
    charisma = stats[1]
    savingThrowOne, savingThrowTwo = "Intelligence", "Charisma"
    # Class Skills
    skills = ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
    numberOfSkills = 2
    baseHitPoints = 6

    # Equipment

    # Weapon
    wizardWeapon = random.randint(1, 2)
    if wizardWeapon == 1:
        equipment.append("Quarterstaff")
    if wizardWeapon == 2:
        equipment.append("Dagger")

    # Focus
    wizardFocus = random.randint(1, 2)
    if wizardFocus == 1:
        equipment.append("Component Pouch")
    if wizardFocus == 2:
        equipment.append("Arcane Focus")

    # Pack
    wizardPack = random.randint(1, 2)
    if wizardPack == 1:
        equipment.extend(scholarsPack)
    if wizardPack == 2:
        equipment.extend(explorersPack)

    # Extras
    equipment.append("Spellbook")

"""
Backgrounds
"""

# Acolyte
if playerBackground == "Acolyte":
    bgSkillOne = "Insight"
    bgSkillTwo = "Religion"

# Charlatan
if playerBackground == "Charlatan":
    bgSkillOne = "Deception"
    bgSkillTwo = "Sleight of Hand"

# Criminal/Spy
if playerBackground == "Criminal/Spy":
    bgSkillOne = "Deception"
    bgSkillTwo = "Stealth"

# Entertainer
if playerBackground == "Entertainer":
    bgSkillOne = "Acrobatics"
    bgSkillTwo = "Performance"

# Folk Hero
if playerBackground == "Folk Hero":
    bgSkillOne = "Animal Handling"
    bgSkillTwo = "Survival"

# Gladiator
if playerBackground == "Gladiator":
    bgSkillOne = "Acrobatics"
    bgSkillTwo = "Performance"

# Guild Artisan/Guild Merchant
if playerBackground == "Guild Artisan/Guild Merchant":
    bgSkillOne = "Insight"
    bgSkillTwo = "Persuasion"

# Hermit
if playerBackground == "Hermit":
    bgSkillOne = "Medicine"
    bgSkillTwo = "Religion"

# Knight
if playerBackground == "Knight":
    bgSkillOne = "History"
    bgSkillTwo = "Persuasion"

# Noble
if playerBackground == "Noble":
    bgSkillOne = "History"
    bgSkillTwo = "Persuasion"

# Outlander
if playerBackground == "Outlander":
    bgSkillOne = "Athletics"
    bgSkillTwo = "Survival"

# Pirate
if playerBackground == "Pirate":
    bgSkillOne = "Athletics"
    bgSkillTwo = "Perception"

# Sage
if playerBackground == "Sage":
    bgSkillOne = "Arcana"
    bgSkillTwo = "History"

# Sailor
if playerBackground == "Sailor":
    bgSkillOne = "Athletics"
    bgSkillTwo = "Perception"

# Soldier
if playerBackground == "Soldier":
    bgSkillOne = "Athletics"
    bgSkillTwo = "Intimidation"

# Urchin
if playerBackground == "Urchin":
    bgSkillOne = "Sleight of Hand"
    bgSkillTwo = "Stealth"

"""
Races
"""

# Aarakockra
if playerRace == "Aaracokra":
    dexterity = dexterity + 2
    wisdom = wisdom + 1
    movement = f"Walking: 25\tFlight: 50"
    size = "Medium"
    languages = "Common, Aaracokra, Auran"
    perk1 = "Your talons are natural weapons.  If you attack with an unarmed strike, you deal 1d4 + strength modifier" \
            " slashing damage."
    bonusPerks = [perk1]

# Dragonborn
if playerRace == "Dragonborn":
    strength = strength + 2
    charisma = charisma + 1
    movement = "Walking: 30"
    size = "Medium"
    languages = "Common, Draconic"
    damageType = ["Acid", "Lightning", "Fire", "Poison", "Cold"]
    damageType = random.choice(damageType)
    if damageType == "Acid":
        ancestry = ["Black", "Copper"]
    if damageType == "Lightning":
        ancestry = ["Blue", "Bronze"]
    if damageType == "Fire":
        ancestry = ["Brass", "Gold", "Red"]
    if damageType == "Poison":
        ancestry = ["Green"]
    if damageType == "Cold":
        ancestry = ["Silver", "White"]
    # noinspection PyUnboundLocalVariable
    ancestry = random.choice(ancestry)
    playerRace = f"{ancestry} Dragonborn"
    perk1 = f"You hail from the race of {ancestry} dragons, and have an {damageType} breath weapon and resistance to " \
            f"{damageType} damage."
    bonusPerks = [perk1]

# Dwarf
if playerRace == "Dwarf":
    playerRace = ["Hill Dwarf", "Mountain Dwarf", "Underdark Dwarf"]
    playerRace = random.choice(playerRace)
    constitution = constitution + 2
    size = "Medium"
    movement = "Walking: 25 (Speed not reduced by heavy armor.)"
    languages = "Common, Dwarvish"
    toolProficiency = ["smith's tools", "brewer's supplies", "mason's tools"]
    toolProficiency = random.choice(toolProficiency)
    perk1 = "You have Darkvision up to 60 feet."
    perk2 = "You have advantage on saving throws against poison, and you have resistance against all poison damage."
    perk3 = "Whenever you make a History check related to stonework, you are considered and expert (double " \
            "proficiency bonus) on the subject."
    perk4 = f"You have proficiency with the battleaxe, handaxe, light hammer, warhammer, and {toolProficiency}."
    if playerRace == "Hill Dwarf":
        wisdom = wisdom + 1
        baseHitPoints = baseHitPoints + (1 * playerLevel)
        bonusPerks = [perk1, perk2, perk3, perk4]
    if playerRace == "Mountain Dwarf":
        strength = strength + 2
        perk4 = f"You have proficiency with light armor, medium armor, the battleaxe, handaxe, light hammer, " \
                f"warhammer, and {toolProficiency}."
        bonusPerks = [perk1, perk2, perk3, perk4]
    if playerRace == "Underdark Dwarf":
        strength = strength + 1
        perk1 = "You have Darkvision up to 120 feet."
        perk2 = "You have advantage on saving throws against illusions, against being charmed or paralyzed, and " \
                "against poison.  You also have resistance to poison damage."
        perk5 = "You have disadvantage on Attack rolls and Wisdom (Perception) checks that rely on sight when you, " \
                "the target of your attack, or whatever you are trying to perceive is in direct sunlight."
        perk6 = "When you reach 3rd level, you can cast the Enlarge/Reduce spell on yourself once with this trait, " \
                "using only the spell's enlarge option. When you reach 5th level, you can cast the Invisibility spell" \
                " on yourself once with this trait. You don't need material components for either spell, and you " \
                "can't cast them while you're in direct sunlight, although sunlight has no effect on them once cast." \
                " You regain the ability to cast these spells with this trait when you finish a long rest. " \
                "Intelligence is your spellcasting ability for these spells."
        bonusPerks = [perk1, perk2, perk3, perk4, perk5, perk6]

# Elf
if playerRace == "Elf":
    playerRace = ["Dark Elf", "High Elf", "Pallid Elf", "Sea Elf", "Wood Elf"]
    playerRace = random.choice(playerRace)
    dexterity = dexterity + 2
    size = "Medium"
    movement = "Walking: 30"
    languages = "Common, Elven"
    perk1 = "You have advantage on saving throws against being charmed, and magic can't put you to sleep."
    perk2 = "Elves do not sleep, instead they meditate deeply.  After resting in this way, you gain the same benefit" \
            " a human would from 8 hours of sleep."
    perk3 = "You have Darkvision up to 60 feet and proficiency in the Perception skill."
    if playerRace == "Dark Elf":
        charisma = charisma + 1
        perk3 = "You have Darkvision up to 120 feet and proficiency in the Perception skill."
        perk4 = "You are proficient with rapiers, shortswords, and hand crossbows."
        perk5 = "You know the Dancing Lights cantrip. When you reach 3rd level, you can cast Faerie Fire once, and" \
                " it recharges after a long rest. When you reach 5th level, you can cast Darkness once, and it" \
                " recharges after a long rest. Charisma is your spellcasting ability for these spells."
        perk6 = "You have disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight when you" \
                ", the target of the attack, or whatever you are trying to perceive is in direct sunlight."
        bonusPerks = [perk1, perk2, perk3, perk4, perk5, perk6]
    if playerRace == "High Elf":
        intelligence = intelligence + 1
        perk4 = f"You know the cantrip 'wizardCantrip' from the Wizard spell list.  Intelligence is your spellcasting" \
                f" ability for it."
        perk5 = "You have proficiency with longswords, shortswords, longbows, and shortbows."
        extraLanguage = random.choice(languages)
        while extraLanguage == "Common" or extraLanguage == "Elven":
            extraLanguage = random.choice(languages)
        languages = f"Common, Elven, {extraLanguage}"
        bonusPerks = [perk1, perk2, perk3, perk4, perk5]
    if playerRace == "Pallid Elf":
        wisdom = wisdom + 1
        perk4 = "You have advantage on Investigation and Insight checks."
        perk5 = "You know the Light cantrip. When you reach 3rd level, you can cast Sleep once, and it recharges" \
                " after a long rest. When you reach 5th level, you can cast Invisibility (Self Only) once, and it " \
                "recharges after a long rest. You do not need the material components required of the spells. Wisdom " \
                "is your spellcasting ability for these spells."
        bonusPerks = [perk1, perk2, perk3, perk4, perk5]
    if playerRace == "Sea Elf":
        constitution = constitution + 1
        perk4 = "You have proficiency with spears, tridents, light crossbows, and nets."
        perk5 = "You can breathe air and water."
        perk6 = "Using gestures and sounds, you can communicate simple ideas with any beast that has an innate " \
                "swimming speed."
        languages = "Common, Elven, Aquan"
        movement = "Walking: 30\tSwimming: 30"
        bonusPerks = [perk1, perk2, perk3, perk4, perk5, perk6]
    if playerRace == "Wood Elf":
        wisdom = wisdom + 1
        movement = "Walking: 35"
        perk4 = "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling " \
                "snow, mist, and other natural phenomena."
        perk5 = "You have proficiency with longswords, shortswords, longbows, and shortbows."
        bonusPerks = [perk1, perk2, perk3, perk4, perk5]

# Genasi
if playerRace == "Genasi":
    playerRace = ["Air Genasi", "Earth Genasi", "Fire Genasi", "Water Genasi"]
    playerRace = random.choice(playerRace)
    constitution = constitution + 2
    size = "Medium"
    movement = "Walking: 30"
    languages = "Common, Primordial"
    if playerRace == "Air Genasi":
        dexterity = dexterity + 1
        perk1 = "You can hold your breath indefinitely while not incapacitated."
        perk2 = "You can cast the Levitate spell once with this trait, requiring no material components, and you" \
                " regain the ability to cast it this way when you finish a long rest. Constitution is your spellcas" \
                "ting ability for this spell."
        bonusPerks = [perk1, perk2]
    if playerRace == "Earth Genasi":
        strength = strength + 1
        perk1 = "You can move across difficult terrain made of earth or stone without expending extra movement."
        perk2 = "You can cast the Pass without Trace spell once with this trait, requiring no material components," \
                " and you regain the ability to cast it this way when you finish a long rest. Constitution is your " \
                "spellcasting ability for this spell."
        bonusPerks = [perk1, perk2]
    if playerRace == "Fire Genasi":
        intelligence = intelligence + 1
        perk1 = "You have Darkvision for 60 feet."
        perk2 = "You have resistance to fire damage."
        perk3 = "You know the Produce Flame cantrip. Once you reach 3rd level, you can cast the Burning Hands spell" \
                " once with this trait as a 1st-level spell, and you regain the ability to cast it this way when you" \
                " finish a long rest. Constitution is your spellcasting ability for these spells."
        bonusPerks = [perk1, perk2, perk3]
    if playerRace == "Water Genasi":
        wisdom = wisdom + 1
        movement = f"Walking: 30\tSwimming: 30"
        perk1 = "You can breathe air and water."
        perk2 = "You have resistance to acid damage."
        perk3 = "You know the Shape Water cantrip. When you reach 3rd level, you can cast the Create or Destroy Water" \
                " spell as a 2nd-level spell once with this trait, and you regain the ability to cast it this way" \
                " when you finish a long rest. Constitution is your spellcasting ability for these spells."
        bonusPerks = [perk1, perk2, perk3]

# Gnome
if playerRace == "Gnome":
    playerRace = ["Forest Gnome", "Rock Gnome", "Svirfneblin"]
    playerRace = random.choice(playerRace)
    intelligence = intelligence + 2
    size = "Small"
    movement = "Walking: 25"
    languages = "Common, Gnomish"
    perk1 = "You have Darkvision for 60 feet."
    perk2 = "You have advantage on all Intelligence, Wisdom, and Charisma saves against magic."
    if playerRace == "Forest Gnome":
        dexterity = dexterity + 1
        perk3 = "You know the Minor Illusion cantrip. Intelligence is your spellcasting modifier for it."
        perk4 = "Through sound and gestures, you may communicate simple ideas with Small or smaller beasts."
        bonusPerks = [perk1, perk2, perk3, perk4]
    if playerRace == "Rock Gnome":
        constitution = constitution + 1
        perk3 = "Whenever you make an Intelligence (History) check related to magical, alchemical, or technological " \
                "items, you can add twice your proficiency bonus instead of any other proficiency bonus that may apply."
        perk4 = "You have proficiency with artisan tools (tinker's tools). Using those tools, you can spend 1 hour " \
                "and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases " \
                "to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), " \
                "or when you use your action to dismantle it; at that time, you can reclaim the materials used to " \
                "create it. You can have up to three such devices active at a time.  When you make a device, it can " \
                "have any of the properties of the Prestidigtation spell, or an effect of similar potency."
        bonusPerks = [perk1, perk2, perk3, perk4]
    if playerRace == "Svirfneblin":
        dexterity = dexterity + 1
        perk1 = "You have Darkvision for 60 feet."
        perk3 = "You have advantage on Dexterity (stealth) checks to hide in rocky terrain."
        bonusPerks = [perk1, perk2, perk3]

# Goliath
if playerRace == "Goliath":
    strength = strength + 2
    constitution = constitution + 1
    size = "Medium"
    movement = "Walking: 30"
    languages = "Common, Giant"
    perk1 = "You have proficiency in the Athletics skill."
    perk2 = "You can focus yourself to occasionally shrug off injury. When you take damage, you can use your reaction" \
            " to roll a d12. Add your Constitution modifier to the number rolled, and reduce the damage by that " \
            "total. After you use this trait, you can’t use it again until you finish a short or long rest."
    perk3 = "You count as one size larger when determining your carrying capacity and the weight you can push, drag," \
            " or lift."
    perk4 = "You’re acclimated to high altitude, including elevations above 20,000 feet. You’re also naturally " \
            "adapted to cold climates."
    bonusPerks = [perk1, perk2, perk3, perk4]

# Half-Elf
if playerRace == "Half-Elf":
    charisma = charisma + 2
    statPicker = [0, 1, 2, 3, 4]
    halfElfStat1, halfElfStat2 = 0, 0
    while halfElfStat1 == halfElfStat2:
        halfElfStat1, halfElfStat2 = random.choice(statPicker), random.choice(statPicker)
    if halfElfStat1 == 0 or halfElfStat2 == 0:
        strength = strength + 1
    if halfElfStat1 == 1 or halfElfStat2 == 1:
        constitution = constitution + 1
    if halfElfStat1 == 2 or halfElfStat2 == 2:
        dexterity = dexterity + 1
    if halfElfStat1 == 3 or halfElfStat2 == 3:
        wisdom = wisdom + 1
    if halfElfStat1 == 4 or halfElfStat2 == 4:
        intelligence = intelligence + 1
    movement = "Walking: 30"
    extraLanguage = random.choice(languages)
    while extraLanguage == "Common" or extraLanguage == "Elven":
        extraLanguage = random.choice(languages)
    languages = f"Common, Elven, {extraLanguage}"
    size = "Medium"
    perk1 = "You have Darkvision up to 60 feet."
    perk2 = "You have advantage on saving throws against being charmed, and magic can't put you to sleep."
    perk3 = "You gain proficiency in 'skill 1' and 'skill 2'"
    bonusPerks = [perk1, perk2, perk3]

# Halfling
if playerRace == "Halfling":
    playerRace = ["Lightfoot Halfling", "Stout Halfling", "Ghostwise Halfling"]
    playerRace = random.choice(playerRace)
    dexterity = dexterity + 2
    size = "Small"
    movement = "Walking: 25 Feet"
    languages = "Common, Halfling"
    perk1 = "You have advantage on saving throws against being frightened."
    perk2 = "When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must" \
            " use the new result, even if it is a 1."
    perk3 = "You can move through the space of any creature that is of a size larger than yours."
    if playerRace == "Lightfoot Halfling":
        charisma = charisma + 1
        perk4 = "You can attempt to hide when you are only obscured by a creature that is at least one size larger" \
                " than you."
    if playerRace == "Stout Halfling":
        constitution = constitution + 1
        perk4 = "You have advantage on saving throws against poison, and you have resistance to poison damage."
    if playerRace == "Ghostwise Halfling":
        wisdom = wisdom + 1
        perk4 = "You can speak telepathically to any creature within 30 feet of you. The creature understands you " \
                "only if the two of you share a language. You can speak telepathically in this way to one creature " \
                "at a time."
    # noinspection PyUnboundLocalVariable
    bonusPerks = [perk1, perk2, perk3, perk4]

# Half-Orc
if playerRace == "Half-Orc":
    strength = strength + 2
    constitution = constitution + 1
    size = "Medium"
    movement = "Walking: 30"
    languages = "Common, Orc"
    perk1 = "You have Darkvison up to 60 feet."
    perk2 = "You gain proficiency in the Intimidation skill."
    perk3 = "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. " \
            "You can't use this feature again until you finish a long rest."
    perk4 = "When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage " \
            "dice one additional time and add it to the extra damage of the critical hit."
    bonusPerks = [perk1, perk2, perk3, perk4]

# Human
if playerRace == "Human":
    playerRace = ["Human", "Variant Human"]
    playerRace = random.choice(playerRace)
    size = "Medium"
    movement = "Walking: 30"
    extraLanguage = random.choice(languages)
    while extraLanguage == "Common":
        extraLanguage = random.choice(languages)
    languages = f"Common, {extraLanguage}"
    if playerRace == "Human":
        strength = strength + 1
        dexterity = dexterity + 1
        constitution = constitution + 1
        wisdom = wisdom + 1
        intelligence = intelligence + 1
        charisma = charisma + 1
    if playerRace == "Variant Human":
        statPicker = [0, 1, 2, 3, 4, 5]
        humanStat1, humanStat2 = 0, 0
        while humanStat1 == humanStat2:
            humanStat1, humanStat2 = random.choice(statPicker), random.choice(statPicker)
        if humanStat1 == 0 or humanStat2 == 0:
            strength = strength + 1
        if humanStat1 == 1 or humanStat2 == 1:
            constitution = constitution + 1
        if humanStat1 == 2 or humanStat2 == 2:
            dexterity = dexterity + 1
        if humanStat1 == 3 or humanStat2 == 3:
            wisdom = wisdom + 1
        if humanStat1 == 4 or humanStat2 == 4:
            intelligence = intelligence + 1
        if humanStat1 == 5 or humanStat2 == 5:
            charisma = charisma + 1
        perk1 = "You gain proficiency in one thing."
        perk2 = "You gain one feat of your choice."
        bonusPerks = [perk1, perk2]

# Tiefling
if playerRace == "Tiefling":
    intelligence = intelligence + 1
    charisma = charisma + 2
    size = "Medium"
    movement = "Walking: 30"
    languages = "Common, Infernal"
    perk1 = "You have Darkvision up to 60 feet."
    perk2 = "You have resistance to fire damage."
    perk3 = "You know the thaumaturgy cantrip. When you reach 3rd level, you can cast the hellish rebuke spell as" \
            " a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. " \
            "When you reach 5th level, you can cast the darkness spell once with this trait and regain the ability " \
            "to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
    bonusPerks = [perk1, perk2, perk3]

"""
Stat Modifiers
"""
# Calculate the modifier by subtracting 10, then dividing by 2, then rounding down.
strengthModifier = math.floor((strength - 10) / 2)
dexterityModifier = math.floor((dexterity - 10) / 2)
constitutionModifier = math.floor((constitution - 10) / 2)
intelligenceModifier = math.floor((intelligence - 10) / 2)
wisdomModifier = math.floor((wisdom - 10) / 2)
charismaModifier = math.floor((charisma - 10) / 2)

"""
Saving Throws
"""
# Defining Saving Throw as the stat modifier, and if either saving throw is the type, add proficiency bonus
strengthSaveProf = ""
strengthSavingThrow = strengthModifier
if savingThrowOne == "Strength" or savingThrowTwo == "Strength":
    strengthSavingThrow = strengthSavingThrow + proficiency
    strengthSaveProf = "*"

dexteritySaveProf = ""
dexteritySavingThrow = dexterityModifier
if savingThrowOne == "Dexterity" or savingThrowTwo == "Dexterity":
    dexteritySavingThrow = dexteritySavingThrow + proficiency
    dexteritySaveProf = "*"

constitutionSaveProf = ""
constitutionSavingThrow = constitutionModifier
if savingThrowOne == "Constitution" or savingThrowTwo == "Constitution":
    constitutionSavingThrow = constitutionSavingThrow + proficiency
    constitutionSaveProf = "*"

intelligenceSaveProf = ""
intelligenceSavingThrow = intelligenceModifier
if savingThrowOne == "Intelligence" or savingThrowTwo == "Intelligence":
    intelligenceSavingThrow = intelligenceSavingThrow + proficiency
    intelligenceSaveProf = "*"

wisdomSaveProf = ""
wisdomSavingThrow = wisdomModifier
if savingThrowOne == "Wisdom" or savingThrowTwo == "Wisdom":
    wisdomSavingThrow = wisdomSavingThrow + proficiency
    wisdomSaveProf = "*"

charismaSaveProf = ""
charismaSavingThrow = charismaModifier
if savingThrowOne == "Charisma" or savingThrowTwo == "Charisma":
    charismaSavingThrow = charismaSavingThrow + proficiency
    charismaSaveProf = "*"

"""
Proficiencies
"""

# Add the two background skills to the beginning of the list of skills
skills.insert(0, bgSkillOne)
skills.insert(1, bgSkillTwo)

# Remove the duplicate abilities if there are any
skills = list(dict.fromkeys(skills))

# Remove the first two skills(The background skills)
del skills[0:2]

# Take random samples equal to the number of skills that the class can have.
classSkills = random.sample(skills, numberOfSkills)

# Raw skill modifiers
acrobatics = dexterityModifier
animalHandling = wisdomModifier
arcana = intelligenceModifier
athletics = strengthModifier
deception = charismaModifier
history = intelligenceModifier
insight = wisdomModifier
intimidation = charismaModifier
investigation = intelligenceModifier
medicine = wisdomModifier
nature = intelligenceModifier
perception = wisdomModifier
performance = charismaModifier
persuasion = charismaModifier
religion = intelligenceModifier
sleightOfHand = dexterityModifier
stealth = dexterityModifier
survival = wisdomModifier

# Grouping of all skills for use later
allSkills = [athletics, acrobatics, arcana, history, investigation, nature, religion, animalHandling, insight,
             medicine, perception, sleightOfHand, stealth, survival, deception, intimidation, performance, persuasion]

# Adding proficiency bonuses
acrobaticsProf = ""
for i in classSkills:
    if i == "Acrobatics":
        acrobatics = acrobatics + proficiency
        acrobaticsProf = "*"

animalHandlingProf = ""
for i in classSkills:
    if i == "Animal Handling":
        animalHandling = animalHandling + proficiency
        animalHandlingProf = "*"

arcanaProf = ""
for i in classSkills:
    if i == "Arcana":
        arcana = arcana + proficiency
        arcanaProf = "*"

athleticsProf = ""

for i in classSkills:
    if i == "Athletics":
        athletics = athletics + proficiency
        athleticsProf = "*"

deceptionProf = ""
for i in classSkills:
    if i == "Deception":
        deception = deception + proficiency
        deceptionProf = "*"

historyProf = ""
for i in classSkills:
    if i == "History":
        history = history + proficiency
        historyProf = "*"

insightProf = ""
for i in classSkills:
    if i == "Insight":
        insight = insight + proficiency
        insightProf = "*"

intimidationProf = ""
if playerRace == "Half-Orc":
    intimidation = intimidation + proficiency
    intimidationProf = "*"
for i in classSkills:
    if i == "Intimidation":
        intimidation = intimidation + proficiency
        intimidationProf = "*"

investigationProf = ""
for i in classSkills:
    if i == "Investigation":
        investigation = investigation + proficiency
        investigationProf = "*"

medicineProf = ""
for i in classSkills:
    if i == "Medicine":
        medicine = medicine + proficiency
        medicineProf = "*"

natureProf = ""
for i in classSkills:
    if i == "Nature":
        nature = nature + proficiency
        natureProf = "*"

perceptionProf = ""
for i in classSkills:
    if i == "Perception":
        perception = perception + proficiency
        perceptionProf = "*"

persuasionProf = ""
for i in classSkills:
    if i == "Persuasion":
        persuasion = persuasion + proficiency
        persuasionProf = "*"

performanceProf = ""
for i in classSkills:
    if i == "Performance":
        performance = performance + proficiency
        performanceProf = "*"

religionProf = ""
for i in classSkills:
    if i == "Religion":
        religion = religion + proficiency
        religionProf = "*"

sleightOfHandProf = ""
for i in classSkills:
    if i == "Sleight of Hand":
        sleightOfHand = sleightOfHand + proficiency
        sleightOfHandProf = "*"

stealthProf = ""
for i in classSkills:
    if i == "Stealth":
        stealth = stealth + proficiency
        stealthProf = "*"

survivalProf = ""
for i in classSkills:
    if i == "Survival":
        survival = survival + proficiency
        survivalProf = "*"

# Special Skill Cases
if playerRace == "Goliath":
    athletics = athletics + proficiency
    athleticsProf = "*"

if playerRace == "Dark Elf" or playerRace == "High Elf" or playerRace == "Sea Elf" or playerRace == "Wood Elf" or playerRace == "Pallid Elf":
    perception = perception + proficiency
    perceptionProf = "*"

if playerRace == "Variant Human":
    bonusSkill = random.choice(allSkills)

if playerRace == "Half-Elf":
    bonusSkill1 = random.choice(allSkills)
    bonusSkill2 = random.choice(allSkills)
    while bonusSkill1 == bonusSkill2:
        bonusSkill2 = random.choice(allSkills)

# Adding Background Skills
if bgSkillOne == "Acrobatics" or bgSkillTwo == "Acrobatics":
    acrobatics = acrobatics + proficiency
    acrobaticsProf = "*"

if bgSkillOne == "Animal Handling" or bgSkillTwo == "Animal Handling":
    animalHandling = animalHandling + proficiency
    animalHandlingProf = "*"

if bgSkillOne == "Arcana" or bgSkillTwo == "Arcana":
    arcana = arcana + proficiency
    arcanaProf = "*"

if bgSkillOne == "Athletics" or bgSkillTwo == "Athletics":
    athletics = athletics + proficiency
    athleticsProf = "*"

if bgSkillOne == "Deception" or bgSkillTwo == "Deception":
    deception = deception + proficiency
    deceptionProf = "*"

if bgSkillOne == "History" or bgSkillTwo == "History":
    history = history + proficiency
    historyProf = "*"

if bgSkillOne == "Insight" or bgSkillTwo == "Insight":
    insight = insight + proficiency
    insightProf = "*"

if bgSkillOne == "Intimidation" or bgSkillTwo == "Intimidation":
    intimidation = intimidation + proficiency
    intimidationProf = "*"

if bgSkillOne == "Investigation" or bgSkillTwo == "Investigation":
    investigation = investigation + proficiency
    investigationProf = "*"

if bgSkillOne == "Medicine" or bgSkillTwo == "Medicine":
    medicine = medicine + proficiency
    medicineProf = "*"

if bgSkillOne == "Nature" or bgSkillTwo == "Nature":
    nature = nature + proficiency
    natureProf = "*"

if bgSkillOne == "Perception" or bgSkillTwo == "Perception":
    perception = perception + proficiency
    perceptionProf = "*"

if bgSkillOne == "Persuasion" or bgSkillTwo == "Persuasion":
    persuasion = persuasion + proficiency
    persuasionProf = "*"

if bgSkillOne == "Performance" or bgSkillTwo == "Performance":
    performance = performance + proficiency
    performanceProf = "*"

if bgSkillOne == "Religion" or bgSkillTwo == "Religion":
    religion = religion + proficiency
    religionProf = "*"

if bgSkillOne == "Sleight of Hand" or bgSkillTwo == "Sleight of Hand":
    sleightOfHand = sleightOfHand + proficiency
    sleightOfHandProf = "*"

if bgSkillOne == "Stealth" or bgSkillTwo == "Stealth":
    stealth = stealth + proficiency
    stealthProf = "*"

if bgSkillOne == "Survival" or bgSkillTwo == "Survival":
    survival = survival + proficiency
    survivalProf = "*"

"""
Armor Class
"""

AC = 10
AC = AC + dexterityModifier

# Setting base AC for each armor
for i in equipment:
    if i == "Leather Armor":
        AC = 11
        AC = AC + dexterityModifier

for i in equipment:
    if i == "Scale Mail":
        AC = 14
        AC = AC + dexterityModifier
        if AC > 16:
            AC = 16

for i in equipment:
    if i == "Chain Mail":
        AC = 16

if playerClass == "Monk":
    AC = 10 + dexterityModifier + wisdomModifier

"""
Characteristics: Personality Traits, Ideals, Bonds, Flaws
"""
personalityTraits = ["Kind", "Evil", "Just plain meh"]
personalityTraits = random.sample(personalityTraits, 2)
ideals = ["Stop", "Breaking", "My", "Code!"]
ideals = random.choice(ideals)
bonds = ["This", "Is", "Getting", "Annoying"]
bonds = random.choice(bonds)
flaws = ["Better", "Be", "The", "Last", "One"]
flaws = random.choice(flaws)

"""
Attacks
"""

# Defining Attacks
attacks = []

for i in equipment:
    if i == "Club":
        attacks.extend(["Club:", "1d4 bludgeoning", "5 feet", "Light", ""])

for i in equipment:
    if i == "Dagger":
        attacks.extend(["Dagger:", "1d4 piercing", "5 feet", "Finesse, Light, Thrown(range 20/60)", ""])

for i in equipment:
    if i == "Dagger(2)":
        attacks.extend(["Dagger:", "1d4 piercing", "5 feet", "Finesse, Light, Thrown(range 20/60)", ""])

for i in equipment:
    if i == "Greatclub":
        attacks.extend(["Greatclub:", "1d8 bludgeoning", "5 feet", "Two-Handed", ""])

for i in equipment:
    if i == "Handaxe":
        attacks.extend(["Handaxe:", "1d6 slashing", "5 feet", "Light, Thrown(range 20/60)", ""])

for i in equipment:
    if i == "Handaxe(2)":
        attacks.extend(["Handaxe:", "1d6 slashing", "5 feet", "Light, Thrown(range 20/60)", ""])

for i in equipment:
    if i == "Javelin":
        attacks.extend(["Javelin:", "1d6 piercing", "5 feet", "Thrown(range 30/120)", ""])

for i in equipment:
    if i == "Javelin(4)":
        attacks.extend(["Javelin:", "1d6 piercing", "5 feet", "Thrown(range 30/120)", ""])

for i in equipment:
    if i == "Five Javelins":
        attacks.extend(["Javelin:", "1d6 piercing", "5 feet", "Thrown(range 30/120)", ""])

for i in equipment:
    if i == "Light Hammer":
        attacks.extend(["Light Hammer:", "1d4 bludgeoning", "5 feet", "Light, Thrown(range 20/60)", ""])

for i in equipment:
    if i == "Mace":
        attacks.extend(["Mace:", "1d6 bludgeoning", "5 feet", ""])

for i in equipment:
    if i == "Quarterstaff":
        attacks.extend(["Quarterstaff:", "1d6 piercing(1d8 piercing)", "5 feet", "Versatile", ""])

for i in equipment:
    if i == "Sickle":
        attacks.extend(["Sickle:", "1d4 slashing", "5 feet", "Light", ""])

for i in equipment:
    if i == "Spear":
        attacks.extend(["Spear:", "1d6 piercing(1d8 piercing)", "5 feet", "Thrown(range 20/60), Versatile", ""])

for i in equipment:
    if i == "Light Crossbow":
        attacks.extend(["Light Crossbow:", "1d8 Piercing", "80/320 feet", "Ammunition (range 80/320), Loading, "
                                                                          "Two-Handed", ""])

for i in equipment:
    if i == "Dart":
        attacks.extend(["Dart:", "1d4 Piercing", "20/60 feet", "Finesse, Thrown (range 20/60)", ""])

for i in equipment:
    if i == "Shortbow":
        attacks.extend(["Shortbow:", "1d6 Piercing", "80/320 feet", "Ammunition (range 80/320), Two-Handed", ""])

for i in equipment:
    if i == "Sling":
        attacks.extend(["Sling:", "1d4 Bludgeoning", "30/120 feet", "Ammunition (range 30/120)", ""])

for i in equipment:
    if i == "Battleaxe":
        attacks.extend(["Battleaxe:", "1d8 slashing(1d10 slashing)", "5 feet", "Versatile", ""])

for i in equipment:
    if i == "Flail":
        attacks.extend(["Flail:", "1d8 bludgeoning", "5 feet", ""])

for i in equipment:
    if i == "Glaive":
        attacks.extend(["Glaive:", "1d10 slashing,", "10 feet", "Heavy, Reach, Two-Handed", ""])

for i in equipment:
    if i == "Greataxe":
        attacks.extend(["Greataxe:", "1d12 slashing", "5 feet", "Heavy, Two-handed", ""])

for i in equipment:
    if i == "Halberd":
        attacks.extend(["Halberd:", "1d10 slashing", "10 feet", "Heavy, Reach, Two-Handed", ""])

for i in equipment:
    if i == "Lance":
        attacks.extend(["Lance:", "1d12 Piercing", "10 feet", "Reach, Special", ""])

for i in equipment:
    if i == "Longsword":
        attacks.extend(["Longsword:", "1d8 Slashing(1d10 Slashing)", "5 feet", "Versatile", ""])

for i in equipment:
    if i == "Maul":
        attacks.extend(["Maul:", "2d6 bludgeoning", "5 feet", "Heavy, Two-handed", ""])

for i in equipment:
    if i == "Morningstar":
        attacks.extend(["Morningstar:", "1d8 Piercing", "5 feet", ""])

for i in equipment:
    if i == "Pike":
        attacks.extend(["Pike:", "1d10 Piercing", "10 feet", "Heavy, Reach, Two-handed", ""])

for i in equipment:
    if i == "Rapier":
        attacks.extend(["Rapier:", "1d8 Piercing", "5 feet", "Finesse", ""])

for i in equipment:
    if i == "Scimitar":
        attacks.extend(["Scimitar:", "1d6 Slashing", "5 feet", "Finesse, Light", ""])

for i in equipment:
    if i == "Shortsword":
        attacks.extend(["Shortsword:", "1d6 Piercing", "5 feet", "Finesse, Light", ""])

for i in equipment:
    if i == "Trident":
        attacks.extend(["Trident:", "1d6 Piercing(1d8 Piercing)", "5 feet", "Thrown (range 20/60), Versatile", ""])

for i in equipment:
    if i == "War Pick":
        attacks.extend(["War Pick:", "1d8 Piercing", "5 feet", ""])

for i in equipment:
    if i == "Warhammer":
        attacks.extend(["Warhammer:", "1d8 Bludgeoning(1d10 Bludgeoning)", "5 feet", "Versatile", ""])

for i in equipment:
    if i == "Whip":
        attacks.extend(["Whip:", "1d4 Slashing", "10 feet", "Finesse, Reach", ""])

for i in equipment:
    if i == "Blowgun":
        attacks.extend(["Blowgun:", "1 Piercing", "25/100 feet", "Ammunition(range 25/100), Loading", ""])

for i in equipment:
    if i == "Hand Crossbow":
        attacks.extend(["Hand Crossbow:", "1d6 Piercing", "30/120 feet", "Ammunition(range 30/120), Light, Loading",
                        ""])

for i in equipment:
    if i == "Heavy Crossbow":
        attacks.extend(["Heavy Crossbow:", "1d10 Piercing", "100/400 feet",
                        "Ammunition(range 100/400), Heavy, Loading, Two-Handed", ""])

for i in equipment:
    if i == "Longbow":
        attacks.extend(["Longbow:", "1d8 Piercing", "150/600 feet", "Ammunition(range 150/600), Heavy, Two-Handed", ""])

for i in equipment:
    if i == "Net":
        attacks.extend(["Net:", "5/15 feet", "Special, Thrown(range 5/15)", ""])


# Print Statements
print(f"Race: \t{playerRace} \nClass: \t{playerClass}")

# Optional Cleric Level 1 Domain
if playerClass == "Cleric":
    print(f"Domain: {playerDomain}")

# Optional Sorcerer Level 1 Origin
if playerClass == "Sorcerer":
    print(f"Origin: {playerOrigin}")

# Optional Warlock Level 1 Patron
if playerClass == "Warlock":
    print(f"Patron: {playerPatron}")

# Alignment
print(f"\nAlignment: \t\t{playerAlignment}")

# Background
print(f"Background:\t\t{playerBackground}")

# Health
print(f"Health:\t\t\t" + str(baseHitPoints + constitutionModifier))

# Hit Die
print(f"Hit Die:\t\t" + "1d" + str(baseHitPoints))

# Armor Class
print(f"Armor Class:\t" + str(AC))

# Print Stats
print(f"\nStats:")
print(f"Strength:\t\t{strength}\t" "(" + "%+d" % strengthModifier + ")")
print(f"Dexterity:\t\t{dexterity}\t" "(" + "%+d" % dexterityModifier + ")")
print(f"Constitution:\t{constitution}\t" "(" + "%+d" % constitutionModifier + ")")
print(f"Intelligence:\t{intelligence}\t" "(" + "%+d" % intelligenceModifier + ")")
print(f"Wisdom:\t\t\t{wisdom}\t" "(" "%+d" % wisdomModifier + ")")
print(f"Charisma:\t\t{charisma}\t" "(" + "%+d" % charismaModifier + ")")

# Print racial traits
print(f"\nRacial Traits:\nMovement:\t{movement}\nLanguages:\t{languages}\nSize:\t\t{size}")
if len(bonusPerks) == 1:
    print(f"\nBonus Perks:\n{bonusPerks[0]}")
if len(bonusPerks) == 2:
    print(f"\nBonus Perks:\n{bonusPerks[0]}\n{bonusPerks[1]}")
if len(bonusPerks) == 3:
    print(f"\nBonus Perks:\n{bonusPerks[0]}\n{bonusPerks[1]}\n{bonusPerks[2]}")
if len(bonusPerks) == 4:
    print(f"\nBonus Perks:\n{bonusPerks[0]}\n{bonusPerks[1]}\n{bonusPerks[2]}\n{bonusPerks[3]}")
if len(bonusPerks) == 5:
    print(f"\nBonus Perks:\n{bonusPerks[0]}\n{bonusPerks[1]}\n{bonusPerks[2]}\n{bonusPerks[3]}\n{bonusPerks[4]}")
if len(bonusPerks) == 6:
    print(f"\nBonus Perks:\n{bonusPerks[0]}\n{bonusPerks[1]}\n{bonusPerks[2]}\n{bonusPerks[3]}\n{bonusPerks[4]}\n{bonusPerks[5]}")

# Print Saving Throws
print(f"\nSaving Throws:")
print(f"Strength:\t\t\t" + "%+d" % strengthSavingThrow, strengthSaveProf)
print(f"Dexterity:\t\t\t" + "%+d" % dexteritySavingThrow, dexteritySaveProf)
print(f"Constitution:\t\t" + "%+d" % constitutionSavingThrow, constitutionSaveProf)
print(f"Intelligence:\t\t" + "%+d" % intelligenceSavingThrow, intelligenceSaveProf)
print(f"Wisdom:\t\t\t\t" "%+d" % wisdomSavingThrow, wisdomSaveProf)
print(f"Charisma:\t\t\t" + "%+d" % charismaSavingThrow, charismaSaveProf)

# Print Skills
print(f"\nSkills:")
print(f"Acrobatics:\t\t\t" + "%+d" % acrobatics, acrobaticsProf)
print(f"Animal Handling:\t" + "%+d" % animalHandling, animalHandlingProf)
print(f"Arcana:\t\t\t\t" + "%+d" % arcana, arcanaProf)
print(f"Athletics:\t\t\t" + "%+d" % athletics, athleticsProf)
print(f"Deception:\t\t\t" + "%+d" % deception, deceptionProf)
print(f"History:\t\t\t" + "%+d" % history, historyProf)
print(f"Insight:\t\t\t" + "%+d" % insight, insightProf)
print(f"Intimidation:\t\t" + "%+d" % intimidation, intimidationProf)
print(f"Investigation:\t\t" + "%+d" % investigation, investigationProf)
print(f"Medicine:\t\t\t" + "%+d" % medicine, medicineProf)
print(f"Nature:\t\t\t\t" + "%+d" % nature, natureProf)
print(f"Perception:\t\t\t" + "%+d" % perception, perceptionProf)
print(f"Performance:\t\t" + "%+d" % performance, performanceProf)
print(f"Persuasion:\t\t\t" + "%+d" % persuasion, persuasionProf)
print(f"Religion:\t\t\t" + "%+d" % religion, religionProf)
print(f"Sleight of Hand:\t" + "%+d" % sleightOfHand, sleightOfHandProf)
print(f"Stealth:\t\t\t" + "%+d" % stealth, stealthProf)
print(f"Survival:\t\t\t" + "%+d" % survival, survivalProf)

# Attacks
print(f"\nAttacks:")
for x in range(len(attacks)):
    print(attacks[x])

# Equipment
print(f"\nEquipment:")
for x in range(len(equipment)):
    print(equipment[x])

# Characteristics
print(f"\nCharacteristics:")
print("Personality Traits:")
for x in range(len(personalityTraits)):
    print(personalityTraits[x])
print("Ideals:", ideals)
print("Bond:", bonds)
print("Flaws:", flaws)
