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
playerBackground = ["Acolyte", "Charlatan", "Criminal/Spy", "Entertainer", "Folk Hero", "Guild Artisan/Guild Merchant",
                    "Hermit", "Knight", "Outlander", "Pirate", "Sage", "Sailor", "Soldier", "Urchin"]
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

"""
Cantrips
"""

cantripsKnown = 0
cantrips = []
bardCantrips = ["Blade Ward", "Dancing Lights", "Friends", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion",
                "Prestidigitation", "Thunderclap", "True Strike", "Vicious Mockery"]
clericCantrips = ["Guidance", "Word of Radiance", "Light", "Mending", "Resistance", "Sacred Flame", "Spare the Dying",
                  "Thaumaturgy", "Toll the Dead", "Virtue"]
druidCantrips = ["Control Flames", "Create Bonfire", "Druidcraft", "Frostbite", "Guidance", "Gust", "Infestation",
                 "Magic Stone", "Mending", "Mold Earth", "Poison Spray", "Primal Savagery", "Produce Flame",
                 "Resistance", "Shape Water", "Shillelagh", "Thorn Whip", "Thunderclap"]
sorcererCantrips = ["Acid Splash", "Blade Ward", "Booming Blade", "Chill Touch", "Control Flames", "Create Bonfire",
                    "Dancing Lights", "Fire Bolt", "Friends", "Frostbite", "Green Flame Blade", "Gust", "Infestation",
                    "Light", "Lightning Lure", "Mage Hand", "Mending", "Message", "Minor Illusion", "Mold Earth",
                    "Poison Spray", "Prestidigitation", "Ray of Frost", "Shape Water", "Shocking Grasp", "Sword Burst",
                    "Thunderclap", "True Strike"]
warlockCantrips = ["Blade Ward", "Booming Blade", "Chill Touch", "Create Bonfire", "Eldritch Blast", "Friends",
                   "Frostbite", "Green Flame Blade", "Infestation", "Lightning Lure", "Mage Hand", "Magic Stone",
                   "Minor Illusion", "Poison Spray", "Prestidigitation", "Sword Burst", "Thunderclap",
                   "Toll the Dead", "True Strike"]
wizardCantrips = ["Acid Splash", "Blade Ward", "Booming Blade", "Chill Touch", "Control Flames", "Create Bonfire",
                  "Dancing Lights", "Encode Thoughts", "Fire Bolt", "Friends", "Frostbite", "Green Flame Blade", "Gust",
                  "Infestation", "Light", "Lightning Lure", "Mage Hand", "Mending", "Message", "Minor Illusion",
                  "Mold Earth", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shape Water", "Shocking Grasp",
                  "Sword Burst", "Thunderclap", "Toll the Dead", "True Strike"]

"""
Class Specific Spells
"""
# This is to have all variables defined at all times.
bardSpells = []
clericSpells = []
druidSpells = []
paladinSpells = []
rangerSpells = []
sorcererSpells = []
warlockSpells = []
wizardSpells = []

"""
Level 1 Spells
"""

numberOfSpells = 0
spells = []
bard1Spells = ["Animal Friendship", "Bane", "Charm Person", "Comprehend Languages", "Cure Wounds", "Detect Magic",
               "Disguise Self", "Dissonant Whispers", "Earth Tremor", "Faerie Fire", "False Life", "Feather Fall",
               "Guiding Hand", "Healing Word", "Heroism", "Identify", "Illusory Script", "Longstrider", "Sense Emotion",
               "Silent Image", "Sleep", "Speak with Animals", "Sudden Awakening", "Tasha's Hideous Laughter",
               "Thunderwave", "Unearthly Chorus", "Unseen Servant"]
cleric1Spells = ["Bane", "Bless", "Command", "Create or Destroy Water", "Cure Wounds", "Detect Evil and Good",
                 "Detect Magic", "Detect Poison and Disease", "Divine Favor", "Guiding Bolt", "Guiding Hand",
                 "Healing Word", "Inflict Wounds", "Protection from Evil and Good", "Purify Food and Drink",
                 "Sanctuary", "Shield of Faith"]
druid1Spells = ["Absorb Elements", "Animal Friendship", "Beast Bond", "Charm Person", "Create or Destroy Water",
                "Cure Wounds", "Detect Magic", "Detect Poison and Disease", "Earth Tremor", "Entangle",
                "Faerie Fire", "Fog Cloud", "Goodberry", "Guiding Hand", "Healing Word", "Ice Knife", "Jump",
                "Longstrider", "Purify Food and Drink", "Speak with Animals", "Thunderwave", "Wild Cunning"]
paladin1Spells = ["Bless", "Command", "Compelled Duel", "Cure Wounds", "Detect Good and Evil", "Detect Magic",
                  "Detect Poison and Disease", "Divine Favor", "Heroism", "Protection from Evil and Good",
                  "Purify Food and Drink", "Searing Smite", "Shield of Faith", "Silent Image", "Thunderous Strike",
                  "Wrathful Smite"]
ranger1Spells = ["Absorb Elements", "Alarm", "Animal Friendship", "Beast Bond", "Cure Wounds", "Detect Magic",
                 "Detect Poison and Disease", "Ensnaring Strike", "Fog Cloud", "Goodberry", "Hail of Thorns",
                 "Hunter's Mark", "Jump", "Longstrider", "Snare", "Speak with Animals", "Sudden Awakening",
                 "Wild Cunning", "Zephyr Strike"]
sorcerer1Spells = ["Burning Hands", "Catapult", "Charm Person", "Chaos Bolt", "Chromatic Orb", "Comprehend Languages",
                   "Detect Magic", "Disguise Self", "Earth Tremor", "Expeditious Retreat", "False Life", "Feather Fall",
                   "Fog Cloud", "Ice Knife", "Jump", "Mage Armor", "Magic Missile", "Ray of Sickness", "Shield",
                   "Silent Image", "Sleep", "Sudden Awakening", "Thunderwave", "Witch Bolt"]
warlock1Spells = ["Armor of Agathys", "Arms of Hadar", "Cause Fear", "Charm Person", "Comprehend Languages",
                  "Expeditious Retreat", "Healing Elixer", "Hellish Rebuke", "Hex", "Illusory Script",
                  "Protection from Good and Evil", "Puppet", "Sense Emotion", "Unseen Servant", "Witch Bolt"]
wizard1Spells = ["Absorb Elements", "Alarm", "Burning Hands", "Catapult", "Cause Fear", "Charm Person", "Chromatic Orb",
                 "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self", "Earth Tremor",
                 "Expeditious Retreat", "False Life", "Feather Fall", "Find Familiar", "Fog Cloud", "Grease",
                 "Ice Knife", "Identify", "Illusory Script", "Jump", "Longstrider", "Mage Armor",
                 "Protection from Evil and Good", "Puppet", "Ray of Sickness", "Sense Emotion", "Shield",
                 "Silent Image", "Snare", "Sleep", "Sudden Awakening", "Tasha's Hideous Laughter",
                 "Tenser's Floating Disk", "Thunderwave", "Unseen Servant", "Witch Bolt"]

"""
Level 2 Spells
"""

bard2Spells = ["Animal Messenger", "Blindness/Deafness", "Calm Emotions", "Cloud of Daggers", "Crown of Madness",
               "Detect Thoughts", "Enhance Ability", "Enthrall", "Heat Metal", "Hold Person", "Invisibility",
               "Knock", "Lesser Restoration", "Locate Animals or Plants", "Locate Object", "Magic Mouth",
               "Phantasmal Force", "Pyrotechnics", "See Invisibility", "Shatter", "Silence", "Skywrite", "Suggestion",
               "Warding Wind", "Zone of Truth"]
cleric2Spells = ["Aid", "Augury", "Blindness/Deafness", "Calm Emotions", "Continual Flame", "Enhance Ability",
                 "Find Traps", "Gentle Repose", "Hold Person", "Lesser Restoration", "Locate Object",
                 "Prayer of Healing", "Protection from Poison", "Silence", "Spiritual Weapon", "Warding Bond",
                 "Zone of Truth"]
druid2Spells = ["Animal Messenger", "Barkskin", "Beast Sense", "Darkvision", "Dust Devil", "Earthbind",
                "Enhance Ability", "Find Traps", "Flame Blade", "Flaming Sphere", "Gust of Wind", "Heat Metal",
                "Hold Person", "Lesser Restoration", "Locate Animals or Plants", "Locate Object", "Moonbeam",
                "Pass Without Trace", "Protection from Poison", "Skywrite", "Spike Growth", "Warding Wind"]
paladin2Spells = ["Aid", "Branding Smite", "Find Steed", "Lesser Restoration", "Locate Object", "Magic Weapon",
                  "Protection from Poison", "Zone of Truth"]
ranger2Spells = ["Animal Messenger", "Barkskin", "Beast Sense", "Cordon of Arrows", "Darkvision", "Find Traps",
                 "Lesser Restoration", "Locate Animals or Plants", "Locate Object", "Pass without Trace",
                 "Protection from Poison", "Silence", "Spike Growth"]
sorcerer2Spells = ["Aganazzar's Scorcher", "Alter Self", "Blindness/Deafness", "Blur", "Cloud of Daggers",
                   "Crown of Madness", "Darkness", "Darkvision", "Detect Thoughts", "Dragon's Breath", "Dust Devil",
                   "Earthbind", "Enhance Ability", "Enlarge/Reduce", "Gust of Wind", "Hold Person", "Invisibility",
                   "Knock", "Levitate", "Maximillian's Earthen Grasp", "Mirror Image", "Misty Step", "Phantasmal Force",
                   "Pyrotechnics", "Scorching Ray", "See Invisibility", "Shatter", "Snilloc's Snowball Storm",
                   "Spider Climb", "Suggestion", "Warding Wind", "Web"]
warlock2Spells = ["Cloud of Daggers", "Crown of Madness", "Darkness", "Earthbind", "Enthrall", "Flock of Familiars",
                  "Hold Person", "Invisibility", "Mirror Image", "Misty Step", "Ray of Enfeeblement", "Shatter",
                  "Spider Climb", "Suggestion"]
wizard2Spells = ["Aganazzar's Scorcher", "Alter Self", "Arcane Lock", "Blindness/Deafness", "Blur", "Cloud of Daggers",
                 "Continual Flame", "Crown of Madness", "Darkness", "Darkvision", "Detect Thoughts", "Dragon's Breath",
                 "Dust Devil", "Earthbind", "Enlarge/Reduce", "Flaming Sphere", "Flaming Sphere", "Gentle Repose",
                 "Gust of Wind", "Hold Person", "Invisibility", "Knock", "Levitate", "Locate Object", "Magic Mouth",
                 "Magic Weapon", "Maximillian's Earthen Grasp", "Melf's Acid Arrow", "Mirror Image", "Misty Step",
                 "Nystul's Magic Aura", "Phantasmal Force", "Pyrotechnics", "Ray of Enfeeblement", "Rope Trick",
                 "Scorching Ray", "See Invisibility", "Shatter", "Skywrite", "Snilloc's Snowball Storm", "Spider Climb",
                 "Suggestion", "Web"]

"""
Level 3 Spells
"""

bard3Spells = ["Bestow Curse", "Clairvoyance", "Dispel Magic", "Enemies Abound", "Fear", "Feign Death",
               "Glyph of Warding", "Hypnotic Pattern", "Leomund's Tiny Hut", "Major Image", "Nondetection",
               "Plant Growth", "Sending", "Speak with Dead", "Speak with Plants", "Stinking Cloud", "Tongues"]
cleric3Spells = ["Animate Dead", "Beacon of Hope", "Bestow Curse", "Clairvoyance", "Create Food and Water", "Daylight",
                 "Dispel Magic", "Feign Death", "Glyph of Warding", "Magic Circle", "Mass Healing Word",
                 "Meld into Stone", "Protection from Energy", "Remove Curse", "Revivify", "Sending", "Speak with Dead",
                 "Spirit Guardians", "Tongues", "Water Walk"]
druid3Spells = ["Call Lightning", "Conjure Animals", "Daylight", "Dispel Magic", "Erupting Earth", "Feign Death",
                "Flame Arrows", "Meld into Stone", "Plant Growth", "Protection from Energy", "Sleet Storm",
                "Speak with Plants", "Tidal Wave", "Wall of Water", "Water Breathing", "Water Walk", "Wind Wall"]
paladin3Spells = ["Aura of Vitaity", "Blinding Smite", "Create Food and Water", "Crusader's Mantle", "Daylight",
                  "Dispel Magic", "Elemental Weapon", "Magic Circle", "Remove Curse", "Revivify"]
ranger3Spells = ["Conjure Animals", "Conjure Barrage", "Daylight", "Flame Arrows", "Lightning Arrow", "Nondetection",
                 "Plant Growth", "Protection from Energy", "Speak with Plants", "Water Breathing", "Water Walk",
                 "Wind Wall"]
sorcerer3Spells = ["Blink", "Clairvoyance", "Counterspell", "Conjure Lesser Demons", "Daylight", "Dispel Magic",
                   "Enemies Abound", "Erupting Earth", "Fear", "Fireball", "Flame Arrows", "Fly", "Gaseous Form",
                   "Haste", "Hypnotic Pattern", "Lightning Bolt", "Major Image", "Melf's Minute Meteors",
                   "Protection from Energy", "Sleet Storm", "Slow", "Stinking Cloud", "Tongues", "Wall of Water",
                   "Water Breathing", "Water Walk"]
warlock3Spells = ["Counterspell", "Dispel Magic", "Enemies Abound", "Fear", "Fly", "Gaseous Form", "Hunger of Hadar",
                  "Hypnotic Pattern", "Magic Circle", "Major Image", "Remove Curse", "Tounges", "Vampiric Touch"]
wizard3Spells = ["Animate Dead", "Bestow Curse", "Blink", "Clairvoyance", "Conjure Lesser Demons", "Counterspell",
                 "Dispel Magic", "Enemies Abound", "Erupting Earth", "Fear", "Feign Death", "Fireball", "Flame Arrows",
                 "Fly", "Galder's Tower", "Gaseous Form", "Glyph of Warding", "Haste", "Hypnotic Pattern",
                 "Leomund's Tiny Hut", "Lightning Bolt", "Magic Circle", "Major Image", "Melf's Minute Meteors",
                 "Nondetection", "Phantom Steed", "Protection from Energy", "Remove Curse", "Sending", "Sleet Storm",
                 "Slow", "Stinking Cloud", "Tidal Wave", "Tongues", "Vampiric Touch", "Wall of Sand", "Wall of Water",
                 "Water Breathing"]

"""
Level 4 Spells
"""

bard4Spells = ["Compulsion", "Confusion", "Dimension Door", "Freedom of Movement", "Greater Invisibility",
               "Hallucinatory Terrain", "Locate Creature", "Polymorph"]
cleric4Spells = ["Banishment", "Control Water", "Death Ward", "Divination", "Freedom of Movement", "Guardian of Faith",
                 "Locate Creature", "Stone Shape"]
druid4Spells = ["Blight", "Confusion", "Conjure Minor Elementals", "Conjure Woodland Beings", "Control Water",
                "Dominate Beast", "Elemental Bane", "Freedom of Movement", "Giant Insect", "Grasping Vine",
                "Guardian of Nature", "Hallucinatory Terrain", "Ice Storm", "Locate Creature", "Polymorph",
                "Stone Shape", "Stoneskin", "Wall of Fire", "Watery Sphere"]
paladin4Spells = ["Aura of Life", "Aura of Purity", "Banishment", "Death Ward", "Locate Creature", "Staggering Smite"]
ranger4Spells = ["Conjure Woodland Beings", "Freedom of Movement", "Grasping Vine", "Guardian of Nature",
                 "Locate Creature", "Stoneskin"]
sorcerer4Spells = ["Banishment", "Blight", "Confusion", "Conjure Barlgura", "Conjure Shadow Demon", "Dimension Door",
                   "Dpminate Beast", "Greater Invisibility", "Ice Storm", "Polymorph", "Stoneskin", "Storm Sphere",
                   "Vitiolic Sphere", "Wall of Fire", "Watery Sphere"]
warlock4Spells = ["Banishment", "Blight", "Dimension Door", "Elemental Bane", "Galder's Speedy Courier",
                  "Hallucinatory Terrain"]
wizard4Spells = ["Arcane Eye", "Banishment", "Blight", "Confusion", "Conjure Barlgura", "Conjure Minor Elementals",
                 "Conjure Shadow Demon", "Control Water", "Dimension Door", "Elemental Bane", "Evard's Black Tentacles",
                 "Fabricate", "Fire Shield", "Galder's Speedy Courier", "Greater Invisibility", "Hallucinatory Terrain",
                 "Ice Storm", "Leomund's Secret Chest", "Locate Creature", "Mordenkainen's Faithful Hound",
                 "Mordenkainen's Private Sanctum", "Otiluke's Resilient Sphere", "Phantasmal Killer", "Polymorph",
                 "Stone Shape", "Stoneskin", "Storm Sphere", "Vitriolic Sphere", "Wall of Fire", "Watery Sphere"]

"""
Level 5 Spells
"""

bard5Spells = ["Animate Objects", "Awaken", "Dominate Person", "Dream", "Geas", "Greater Restoration", "Hold Monster",
               "Legend Lore", "Mass Cure Wounds", "Mislead", "Modify Memory", "Planar Binding", "Raise Dead", "Scrying",
               "Seeming", "Teleportation Circle"]
cleric5Spells = ["Commune", "Contagion", "Dispel Evil and Good", "Flame Strike", "Geas", "Greater Restoration",
                 "Hallow", "Insect Plague", "Legend Lore", "Mass Cure Wounds", "Planar Binding", "Raise Dead",
                 "Scrying"]
druid5Spells = ["Antilife Shell", "Awaken", "Commune With Nature", "Conjure Elemental", "Contagion", "Control Winds",
                "Geas", "Greater Restoration", "Insect Plague", "Maelstrom", "Mass Cure Wounds", "Planar Binding",
                "Reincarnate", "Scrying", "Transmute Rock", "Tree Stride", "Wall of Stone"]
paladin5Spells = ["Banishing Smite", "Circle of Power", "Destructive Wave", "Dispel Evil and Good", "Geas",
                  "Raise Dead"]
ranger5Spells = ["Commune with Nature", "Conjure Volley", "Swift Quiver", "Tree Stride"]
sorcerer5Spells = ["Animate Objects", "Cloudkill", "Cone of Cold", "Conjure Vrock", "Control Winds", "Creation",
                   "Dominate Person", "Hold Monster", "Immolation", "Insect Plague", "Seeming", "Telekenesis",
                   "Teleportation Circle", "Wall of Stone"]
warlock5Spells = ["Contact other Plane", "Dream", "Hold Monster", "Scrying"]
wizard5Spells = ["Animate Objects", "Bigby's Hand", "Cloudkill", "Cone of Cold", "Conjure Elemental", "Conjure Vrock",
                 "Contact Other Plane", "Control Winds", "Creation", "Dominate Person", "Dream", "Geas", "Hold Monster",
                 "Immolation", "Legend Lore", "Mislead", "Modify Memory", "Passwall", "Planar Binding",
                 "Rary's Telepathic Bond", "Scrying", "Seeming", "Telekinesis", "Teleportation Circle",
                 "Transmute Rock", "Wall of Force", "Wall of Stone"]

"""
Level 6 Spells
"""

bard6Spells = ["Eyebite", "Find the Path", "Guards and Wards", "Mass Suggestion", "Otto's Irresistible Dance",
               "Programmed Illusion", "True Seeing"]
cleric6Spells = ["Blade Barrier", "Create Undead", "Find the Path", "Forbiddance", "Harm", "Heal", "Heroes' Feast",
                 "Planar Ally", "True Seeing", "Word of Recall"]
druid6Spells = ["Bones of the Earth", "Conjure Fey", "Find the Path", "Heal", "Heroe's Feast", "Investiture of Flame",
                "Investiture of Ice", "Investiture of Stone", "Investiture of Wind", "Move Earht", "Primordeal Ward",
                "Sunbeam", "Transport via Plants", "Wall of Thorns", "Wind Walk"]
sorcerer6Spells = ["Arcane Gate", "Chain Lightning", "Circle of Death", "Disintegrate", "Eyebite",
                   "Globe of Invulnerability", "Investiture of Flame", "Investiture of Ice", "Investiture of Stone",
                   "Investiture of Wind", "Mass Suggestion", "Move Earth", "Sunbeam", "True Seeing"]
warlock6Spells = ["Arcane Gate", "Circle of Death", "Conjure Fey", "Create Undead", "Eyebite", "Flesh to Stone",
                  "Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind",
                  "Mass Suggestion", "True Seeing"]
wizard6Spells = ["Arcane Gate", "Chain Lightning", "Circle of Death", "Contingency", "Create Undead", "Disintegrate",
                 "Drawmij's Instant Summons", "Eyebite", "Flesh to Stone", "Globe of Invulnerability",
                 "Guards and Wards", "Investiture of Flame", "Investiture of Ice", "Investiture of Stone",
                 "Investiture of Wind", "Magic Jar", "Mass Suggestion", "Move Earth", "Otiluke's Freezing Sphere",
                 "Otto's Irresistible Dance", "Programmed Illusion", "Sunbeam", "True Seeing", "Wall of Ice"]

"""
Level 7 Spells
"""

bard7Spells = ["Etherealness", "Forcecage", "Mirage Arcane", "Mordenkainen's Magnificent Mansion",
               "Mordenkainen's Sword", "Project Image", "Regenerate", "Resurrection", "Symbol", "Teleport"]
cleric7Spells = ["Conjure Celestial", "Divine Word", "Etherealness", "Fire Storm", "Plane Shift", "Regenerate",
                 "Resurrection", "Symbol"]
druid7Spells = ["Fire Storm", "Mirage Arcane", "Plane Shift", "Regenerate", "Reverse Gravity", "Whirlwind"]
sorcerer7Spells = ["Conjure Hezrou", "Delayed Blast Fireball", "Etherealness", "Finger of Death", "Fire Storm",
                   "Plane Shift", "Prismatic Spray", "Reverse Gravity", "Teleport"]
warlock7Spells = ["Etherealness", "Finger of Death", "Forcecage", "Plane Shift"]
wizard7Spells = ["Conjure Hezrou", "Delayed Blast Fireball", "Etherealness", "Etherealness", "Finger of Death",
                 "Forcecage", "Mirage Arcane", "Mordenkainen's Magnificent Mansion", "Mordenkainen's Sword",
                 "Plane Shift", "Prismatic Spray", "Project Image", "Reverse Gravity", "Sequester", "Simulacrum",
                 "Symbol", "Teleport", "Whirlwind"]

"""
Level 8 Spells
"""

bard8Spells = ["Dominate Monster", "Feeblemind", "Glibness", "Mind Blank", "Power Word: Stun"]
cleric8Spells = ["Antimagic Field", "Control Weather", "Earthquake", "Holy Aura"]
druid8Spells = ["Animal Shapes", "Antipathy/Sympathy", "Control Weather", "Earthquake", "Feeblemind", "Sunburst",
                "Tsunami"]
sorcerer8Spells = ["Abi-Dalzim's Horrid Wilting", "Dominate Monster", "Earthquake", "Incindiary Cloud",
                   "Power Word: Stun", "Sunburst"]
warlock8Spells = ["Demiplane", "Dominate Monster", "Feeblemind", "Glibness", "Power Word: Stun"]
wizard8Spells = ["Abi-Dalzim's Horrid Wilting", "Antimagic Field", "Antipathy/Sympathy", "Clone", "Control Weather",
                 "Demiplane", "Dominate Monster", "Feeblemind", "Incendiary Cloud", "Maze", "Mind Blank",
                 "Power Word: Stun", "Sunburst", "Telepathy"]

"""
Level 9 Spells
"""

bard9Spells = ["Foresight", "Power Word: Heal", "Power Word: Kill", "True Polymorph"]
cleric9Spells = ["Astral Projection", "Gate", "Mass Heal", "True Resurrection"]
druid9Spells = ["Foresight", "Shapechange", "Storm of Vengeance", "True Resurrection"]
sorcerer9Spells = ["Gate", "Meteor Swarm", "Power Word: Kill", "Time Stop", "Wish"]
warlock9Spells = ["Astral Projection", "Foresight", "Imprisonment", "Power Word: Kill", "True Polymorph"]
wizard9Spells = ["Astral Projection", "Foresight", "Gate", "Improsonment", "Meteor Swarm", "Power Word: Kill",
                 "Prismatic Wall", "Shapechange", "Time Stop", "True Polymorph", "Weird", "Wish"]

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
clericDomains = ["Arcana", "Death", "Forge", "Grave", "Knowledge", "Life", "Light", "Nature", "Order", "Tempest",
                 "Trickery", "War"]
clericDomain = random.choice(clericDomains)
clericSub = random.randint(1, 3)
domainCantrips = []
domainSpells = []
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
    druidCircle = ["Circle of Dreams", "Circle of the Moon", "Circle of the Land: Arctic", "Circle of the Land: Coast",
                   "Circle of the Land: Desert", "Circle of the Land: Forest", "Circle of the Land: Grassland",
                   "Circle of the Land: Mountain", "Circle of the Land: Swamp", "Circle of the Land: Underdark",
                   "Circle of the Shepherd", "Circle of Spores"]
    druidCircle = random.choice(druidCircle)

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

    # Oaths
    paladinOaths = ["Oath of the Ancients", "Oath of Conquest", "Oath of the Crown", "Oath of Devotion",
                    "Oath of Vengeance", "Oathbreaker"]
    sacredOath = random.choice(paladinOaths)

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

    rangerConclaves = ["Beast Master Conclave", "Gloom Stalker Conclave", "Horizon Walker Conclave", "Hunter Conclave",
                       "Monster Slayer Conclave"]
    rangerConclave = random.choice(rangerConclaves)

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
sorcererOrigins = ["Divine Soul", "Draconic Bloodline", "Shadow", "Storm", "Wild Magic"]
sorcerousOrigin = random.choice(sorcererOrigins)

if playerClass == "Sorcerer":
    strength = stats[0]
    dexterity = stats[4]
    constitution = stats[3]
    intelligence = stats[1]
    wisdom = stats[2]
    charisma = stats[5]
    savingThrowOne, savingThrowTwo = "Constitution", "Charisma"

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
wizardSchool = []
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

    # Magic School
    wizardSchools = ["Abjuration", "Bladesinger", "Chronurgy", "Conjuration", "Divination", "Enchantment",
                     "Evocation", "Illusion", "Necromancy", "Transmutation", "War Magic"]
    wizardSchool = random.choice(wizardSchools)

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

# Declare standard variables to avoid error if not declared in certain races.
playerSubRace = "None"
movement = "Walking: 30"
size = "Medium"
bonusPerks = []

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
    dragonTypes = ["Just to make the program happy"]
    if damageType == "Acid":
        dragonTypes = ["Black", "Copper"]
    if damageType == "Lightning":
        dragonTypes = ["Blue", "Bronze"]
    if damageType == "Fire":
        dragonTypes = ["Brass", "Gold", "Red"]
    if damageType == "Poison":
        dragonTypes = ["Green"]
    if damageType == "Cold":
        dragonTypes = ["Silver", "White"]
    playerSubRace = random.choice(dragonTypes)
    perk1 = f"You hail from the race of {playerSubRace} dragons, giving you a {damageType} breath weapon and " \
            f"resistance to {damageType} damage."
    bonusPerks = [perk1]

# Dwarf
if playerRace == "Dwarf":
    playerSubRace = ["Hill Dwarf", "Mountain Dwarf", "Underdark Dwarf"]
    playerSubRace = random.choice(playerSubRace)
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
    if playerSubRace == "Hill Dwarf":
        wisdom = wisdom + 1
        baseHitPoints = baseHitPoints + (1 * playerLevel)
        bonusPerks = [perk1, perk2, perk3, perk4]
    if playerSubRace == "Mountain Dwarf":
        strength = strength + 2
        perk4 = f"You have proficiency with light armor, medium armor, the battleaxe, handaxe, light hammer, " \
                f"warhammer, and {toolProficiency}."
        bonusPerks = [perk1, perk2, perk3, perk4]
    if playerSubRace == "Underdark Dwarf":
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
    playerSubRace = ["Dark Elf", "High Elf", "Pallid Elf", "Sea Elf", "Wood Elf"]
    playerSubRace = random.choice(playerSubRace)
    dexterity = dexterity + 2
    size = "Medium"
    movement = "Walking: 30"
    languages = "Common, Elven"
    perk1 = "You have advantage on saving throws against being charmed, and magic can't put you to sleep."
    perk2 = "Elves do not sleep, instead they meditate deeply.  After resting in this way, you gain the same benefit" \
            " a human would from 8 hours of sleep."
    perk3 = "You have Darkvision up to 60 feet and proficiency in the Perception skill."
    if playerSubRace == "Dark Elf":
        charisma = charisma + 1
        perk3 = "You have Darkvision up to 120 feet and proficiency in the Perception skill."
        perk4 = "You are proficient with rapiers, shortswords, and hand crossbows."
        perk5 = "You know the Dancing Lights cantrip. When you reach 3rd level, you can cast Faerie Fire once, and" \
                " it recharges after a long rest. When you reach 5th level, you can cast Darkness once, and it" \
                " recharges after a long rest. Charisma is your spellcasting ability for these spells."
        perk6 = "You have disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight when you" \
                ", the target of the attack, or whatever you are trying to perceive is in direct sunlight."
        bonusPerks = [perk1, perk2, perk3, perk4, perk5, perk6]
    if playerSubRace == "High Elf":
        intelligence = intelligence + 1
        perk4 = f"You know the cantrip 'wizardCantrip' from the Wizard spell list.  Intelligence is your spellcasting" \
                f" ability for it."
        perk5 = "You have proficiency with longswords, shortswords, longbows, and shortbows."
        extraLanguage = random.choice(languages)
        while extraLanguage == "Common" or extraLanguage == "Elven":
            extraLanguage = random.choice(languages)
        languages = f"Common, Elven, {extraLanguage}"
        bonusPerks = [perk1, perk2, perk3, perk4, perk5]
    if playerSubRace == "Pallid Elf":
        wisdom = wisdom + 1
        perk4 = "You have advantage on Investigation and Insight checks."
        perk5 = "You know the Light cantrip. When you reach 3rd level, you can cast Sleep once, and it recharges" \
                " after a long rest. When you reach 5th level, you can cast Invisibility (Self Only) once, and it " \
                "recharges after a long rest. You do not need the material components required of the spells. Wisdom " \
                "is your spellcasting ability for these spells."
        bonusPerks = [perk1, perk2, perk3, perk4, perk5]
    if playerSubRace == "Sea Elf":
        constitution = constitution + 1
        perk4 = "You have proficiency with spears, tridents, light crossbows, and nets."
        perk5 = "You can breathe air and water."
        perk6 = "Using gestures and sounds, you can communicate simple ideas with any beast that has an innate " \
                "swimming speed."
        languages = "Common, Elven, Aquan"
        movement = "Walking: 30\tSwimming: 30"
        bonusPerks = [perk1, perk2, perk3, perk4, perk5, perk6]
    if playerSubRace == "Wood Elf":
        wisdom = wisdom + 1
        movement = "Walking: 35"
        perk4 = "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling " \
                "snow, mist, and other natural phenomena."
        perk5 = "You have proficiency with longswords, shortswords, longbows, and shortbows."
        bonusPerks = [perk1, perk2, perk3, perk4, perk5]

# Genasi
if playerRace == "Genasi":
    playerSubRace = ["Air Genasi", "Earth Genasi", "Fire Genasi", "Water Genasi"]
    playerSubRace = random.choice(playerSubRace)
    constitution = constitution + 2
    size = "Medium"
    movement = "Walking: 30"
    languages = "Common, Primordial"
    if playerSubRace == "Air Genasi":
        dexterity = dexterity + 1
        perk1 = "You can hold your breath indefinitely while not incapacitated."
        perk2 = "You can cast the Levitate spell once with this trait, requiring no material components, and you" \
                " regain the ability to cast it this way when you finish a long rest. Constitution is your spellcas" \
                "ting ability for this spell."
        bonusPerks = [perk1, perk2]
    if playerSubRace == "Earth Genasi":
        strength = strength + 1
        perk1 = "You can move across difficult terrain made of earth or stone without expending extra movement."
        perk2 = "You can cast the Pass without Trace spell once with this trait, requiring no material components," \
                " and you regain the ability to cast it this way when you finish a long rest. Constitution is your " \
                "spellcasting ability for this spell."
        bonusPerks = [perk1, perk2]
    if playerSubRace == "Fire Genasi":
        intelligence = intelligence + 1
        perk1 = "You have Darkvision for 60 feet."
        perk2 = "You have resistance to fire damage."
        perk3 = "You know the Produce Flame cantrip. Once you reach 3rd level, you can cast the Burning Hands spell" \
                " once with this trait as a 1st-level spell, and you regain the ability to cast it this way when you" \
                " finish a long rest. Constitution is your spellcasting ability for these spells."
        bonusPerks = [perk1, perk2, perk3]
    if playerSubRace == "Water Genasi":
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
    playerSubRace = ["Forest Gnome", "Rock Gnome", "Svirfneblin"]
    playerSubRace = random.choice(playerSubRace)
    intelligence = intelligence + 2
    size = "Small"
    movement = "Walking: 25"
    languages = "Common, Gnomish"
    perk1 = "You have Darkvision for 60 feet."
    perk2 = "You have advantage on all Intelligence, Wisdom, and Charisma saves against magic."
    if playerSubRace == "Forest Gnome":
        dexterity = dexterity + 1
        perk3 = "You know the Minor Illusion cantrip. Intelligence is your spellcasting modifier for it."
        perk4 = "Through sound and gestures, you may communicate simple ideas with Small or smaller beasts."
        bonusPerks = [perk1, perk2, perk3, perk4]
    if playerSubRace == "Rock Gnome":
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
    if playerSubRace == "Svirfneblin":
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
    playerSubRace = ["Lightfoot Halfling", "Stout Halfling", "Ghostwise Halfling"]
    playerSubRace = random.choice(playerSubRace)
    dexterity = dexterity + 2
    size = "Small"
    movement = "Walking: 25 Feet"
    languages = "Common, Halfling"
    perk1 = "You have advantage on saving throws against being frightened."
    perk2 = "When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must" \
            " use the new result, even if it is a 1."
    perk3 = "You can move through the space of any creature that is of a size larger than yours."
    if playerSubRace == "Lightfoot Halfling":
        charisma = charisma + 1
        perk4 = "You can attempt to hide when you are only obscured by a creature that is at least one size larger" \
                " than you."
    if playerSubRace == "Stout Halfling":
        constitution = constitution + 1
        perk4 = "You have advantage on saving throws against poison, and you have resistance to poison damage."
    if playerSubRace == "Ghostwise Halfling":
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
    playerSubRace = ["Human", "Variant Human"]
    playerSubRace = random.choice(playerSubRace)
    size = "Medium"
    movement = "Walking: 30"
    extraLanguage = random.choice(languages)
    while extraLanguage == "Common":
        extraLanguage = random.choice(languages)
    languages = f"Common, {extraLanguage}"
    if playerSubRace == "Human":
        strength = strength + 1
        dexterity = dexterity + 1
        constitution = constitution + 1
        wisdom = wisdom + 1
        intelligence = intelligence + 1
        charisma = charisma + 1
    if playerSubRace == "Variant Human":
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
if playerRace == "Elf":
    perception = perception + proficiency
    perceptionProf = "*"

if playerRace == "Goliath":
    athletics = athletics + proficiency
    athleticsProf = "*"

if playerRace == "Half-Elf":
    bonusSkill1 = random.choice(allSkills)
    bonusSkill2 = random.choice(allSkills)
    while bonusSkill1 == bonusSkill2:
        bonusSkill2 = random.choice(allSkills)

if playerRace == "Half-Orc":
    intimidation = intimidation + proficiency
    intimidationProf = "*"

if playerSubRace == "Variant Human":
    bonusSkill = random.choice(allSkills)

"""
Adding Background Skills
"""

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
Spellcasting
"""

# Declarations for all variables used
numberOfCantrips = 0
preparedSpellcasting = False

# Bard
if playerClass == "Bard":
    if playerLevel < 4:
        cantripsKnown = 2
    if 3 < playerLevel < 10:
        cantripsKnown = 3
    if playerLevel > 9:
        cantripsKnown = 4
    if playerLevel < 10 or 11 < playerLevel < 14 or 15 < playerLevel < 18:
        numberOfSpells = playerLevel + 3
    if 9 < playerLevel < 12 or 13 < playerLevel < 16:
        numberOfSpells = playerLevel + 4
    if 17 < playerLevel < 21:
        numberOfSpells = 22
    if playerLevel < 3:
        bardSpells = bard1Spells
    if 2 < playerLevel < 5:
        bardSpells = bard1Spells + bard2Spells
    if 4 < playerLevel < 7:
        bardSpells = bard1Spells + bard2Spells + bard3Spells
    if 6 < playerLevel < 9:
        bardSpells = bard1Spells + bard2Spells + bard3Spells + bard4Spells
    if 8 < playerLevel < 11:
        bardSpells = bard1Spells + bard2Spells + bard3Spells + bard4Spells + bard5Spells
    if 10 < playerLevel < 13:
        bardSpells = bard1Spells + bard2Spells + bard3Spells + bard4Spells + bard5Spells + bard6Spells
    if 12 < playerLevel < 15:
        bardSpells = bard1Spells + bard2Spells + bard3Spells + bard4Spells + bard5Spells + bard6Spells + bard7Spells
    if 14 < playerLevel < 17:
        bard1Spells = bard1Spells + bard2Spells + bard3Spells + bard4Spells
        bardSpells = bard1Spells + bard5Spells + bard6Spells + bard7Spells + bard8Spells
    if playerLevel > 16:
        bard1Spells = bard1Spells + bard2Spells + bard3Spells + bard4Spells
        bardSpells = bard1Spells + bard5Spells + bard6Spells + bard7Spells + bard8Spells + bard9Spells
    cantrips = random.sample(bardCantrips, cantripsKnown)
    numberOfCantrips = cantripsKnown
    spells = random.sample(bardSpells, numberOfSpells)
    saveDC = 8 + proficiency + charismaModifier
    attackModifier = proficiency + charismaModifier

# Cleric
if playerClass == "Cleric":
    preparedSpellcasting = True
    if playerLevel < 4:
        cantripsKnown = 3
    if 3 < playerLevel < 10:
        cantripsKnown = 4
    if playerLevel > 9:
        cantripsKnown = 5
    if playerLevel < 3:
        clericSpells = cleric1Spells
    if 2 < playerLevel < 5:
        clericSpells = cleric1Spells + cleric2Spells
    if 4 < playerLevel < 7:
        clericSpells = cleric1Spells + cleric2Spells + cleric3Spells
    if 6 < playerLevel < 9:
        clericSpells = cleric1Spells + cleric2Spells + cleric3Spells + cleric4Spells
    if 8 < playerLevel < 11:
        clericSpells = cleric1Spells + cleric2Spells + cleric3Spells + cleric4Spells + cleric5Spells
    if 10 < playerLevel < 13:
        cleric1Spells = cleric1Spells + cleric2Spells + cleric3Spells + cleric4Spells + cleric5Spells
        clericSpells = cleric1Spells + cleric6Spells
    if 12 < playerLevel < 15:
        cleric1Spells = cleric1Spells + cleric2Spells + cleric3Spells + cleric4Spells + cleric5Spells
        clericSpells = cleric1Spells + cleric6Spells + cleric7Spells
    if 14 < playerLevel < 17:
        cleric1Spells = cleric1Spells + cleric2Spells + cleric3Spells + cleric4Spells + cleric5Spells
        clericSpells = cleric1Spells + cleric6Spells + cleric7Spells + cleric8Spells
    if playerLevel > 16:
        cleric1Spells = cleric1Spells + cleric2Spells + cleric3Spells + cleric4Spells + cleric5Spells
        clericSpells = cleric1Spells + cleric6Spells + cleric7Spells + cleric8Spells + cleric9Spells

    # Arcane Spells
    if clericDomain == "Arcana":
        if playerLevel >= 1:
            domainSpells = ["Detect Magic", "Magic Missle"]
        if playerLevel >= 3:
            domainSpells.append("Magic Weapon")
            domainSpells.append("Nystul's Magic Aura")
        if playerLevel >= 5:
            domainSpells.append("Dispel Magic")
            domainSpells.append("Magic Circle")
        if playerLevel >= 7:
            domainSpells.append("Arcane Eye")
            domainSpells.append("Leomund's Secret Chest")
        if playerLevel >= 9:
            domainSpells.append("Planar Binding")
            domainSpells.append("Teleportation Circle")
        domainCantrips = random.sample(wizardCantrips, 2)

    # Death Spells
    if clericDomain == "Death":
        if playerLevel >= 1:
            domainSpells = ["False Life", "Ray of Sickness"]
        if playerLevel >= 3:
            domainSpells.append("Blindness/Deafness")
            domainSpells.append("Ray of Enfeeblement")
        if playerLevel >= 5:
            domainSpells.append("Animate Dead")
            domainSpells.append("Vampiric Touch")
        if playerLevel >= 7:
            domainSpells.append("Blight")
            domainSpells.append("Death Ward")
        if playerLevel >= 9:
            domainSpells.append("Antilife Shell")
            domainSpells.append("Cloudkill")
        domainCantrips = ["Chill Touch", "Spare the Dying", "Toll the Dead"]
        domainCantrips = [random.choice(domainCantrips)]

    # Forge Spells
    if clericDomain == "Forge":
        if playerLevel >= 1:
            domainSpells = ["Identify", "Searing Smite"]
        if playerLevel >= 3:
            domainSpells.append("Heat Metal")
            domainSpells.append("Magic Weapon")
        if playerLevel >= 5:
            domainSpells.append("Elemental Weapon")
            domainSpells.append("Protection from Energy")
        if playerLevel >= 7:
            domainSpells.append("Fabricate")
            domainSpells.append("Wall of Fire")
        if playerLevel >= 9:
            domainSpells.append("Animate Objects")
            domainSpells.append("Creation")

    # Grave Spells
    if clericDomain == "Grave":
        if playerLevel >= 1:
            domainSpells = ["Bane", "False Life"]
        if playerLevel >= 3:
            domainSpells.append("Gentle Repose")
            domainSpells.append("Ray of Enfeeblement")
        if playerLevel >= 5:
            domainSpells.append("Revivify")
            domainSpells.append("Vampiric Touch")
        if playerLevel >= 7:
            domainSpells.append("Blight")
            domainSpells.append("Death Ward")
        if playerLevel >= 9:
            domainSpells.append("Antilife Shell")
            domainSpells.append("Raise Dead")
        domainCantrips = ["Spare the Dying"]

    # Knowledge Spells
    if clericDomain == "Knowledge":
        if playerLevel >= 1:
            domainSpells = ["Command", "Identify"]
        if playerLevel >= 3:
            domainSpells.append("Augury")
            domainSpells.append("Suggestion")
        if playerLevel >= 5:
            domainSpells.append("Nondetection")
            domainSpells.append("Speak with Death")
        if playerLevel >= 7:
            domainSpells.append("Arcane Eye")
            domainSpells.append("Confusion")
        if playerLevel >= 9:
            domainSpells.append("Legend Lore")
            domainSpells.append("Scrying")

    # Life Spells
    if clericDomain == "Life":
        if playerLevel >= 1:
            domainSpells = ["Detect Magic", "Magic Missle"]
        if playerLevel >= 3:
            domainSpells.append("Magic Weapon")
            domainSpells.append("Nystul's Magic Aura")
        if playerLevel >= 5:
            domainSpells.append("Dispel Magic")
            domainSpells.append("Magic Circle")
        if playerLevel >= 7:
            domainSpells.append("Arcane Eye")
            domainSpells.append("Leomund's Secret Chest")
        if playerLevel >= 9:
            domainSpells.append("Planar Binding")
            domainSpells.append("Teleportation Circle")

    # Light Spells
    if clericDomain == "Light":
        if playerLevel >= 1:
            domainSpells = ["Burning Hands", "Faerie Fire"]
        if playerLevel >= 3:
            domainSpells.append("Flaming Sphere")
            domainSpells.append("Scorching Ray")
        if playerLevel >= 5:
            domainSpells.append("Daylight")
            domainSpells.append("Fireball")
        if playerLevel >= 7:
            domainSpells.append("Guardian of Faith")
            domainSpells.append("Wall of Fire")
        if playerLevel >= 9:
            domainSpells.append("Flame Strike")
            domainSpells.append("Scrying")
        domainCantrips = ["Light"]

    # Nature Spells
    if clericDomain == "Nature":
        if playerLevel >= 1:
            domainSpells = ["Animal Frindship", "Speak with Animals"]
        if playerLevel >= 3:
            domainSpells.append("Barkskin")
            domainSpells.append("Spike Growth")
        if playerLevel >= 5:
            domainSpells.append("Plant Growth")
            domainSpells.append("Wind Wall")
        if playerLevel >= 7:
            domainSpells.append("Dominate Beast")
            domainSpells.append("Grasping Vine")
        if playerLevel >= 9:
            domainSpells.append("Insect Plague")
            domainSpells.append("Tree Stride")
        domainCantrips = [random.choice(druidCantrips)]

    # Order Spells
    if clericDomain == "Order":
        if playerLevel >= 1:
            domainSpells = ["Command", "Heroism"]
        if playerLevel >= 3:
            domainSpells.append("Hold Person")
            domainSpells.append("Zone of Truth")
        if playerLevel >= 5:
            domainSpells.append("Mass Healing Word")
            domainSpells.append("Slow")
        if playerLevel >= 7:
            domainSpells.append("Compulsion")
            domainSpells.append("Locate Creature")
        if playerLevel >= 9:
            domainSpells.append("Commune")
            domainSpells.append("Dominate Person")

    # Tempest Spells
    if clericDomain == "Tempest":
        if playerLevel >= 1:
            domainSpells = ["Fog Cloud", "Thunderwave"]
        if playerLevel >= 3:
            domainSpells.append("Gust of Wind")
            domainSpells.append("Shatter")
        if playerLevel >= 5:
            domainSpells.append("Call Lightning")
            domainSpells.append("Sleet Storm")
        if playerLevel >= 7:
            domainSpells.append("Control Water")
            domainSpells.append("Ice Storm")
        if playerLevel >= 9:
            domainSpells.append("Destructive Wave")
            domainSpells.append("Insect Plague")

    # Trickery Spells
    if clericDomain == "Trickery":
        if playerLevel >= 1:
            domainSpells = ["Charm Person", "Disguise Self"]
        if playerLevel >= 3:
            domainSpells.append("Mirror Image")
            domainSpells.append("Pass without Trace")
        if playerLevel >= 5:
            domainSpells.append("Blink")
            domainSpells.append("Dispel Magic")
        if playerLevel >= 7:
            domainSpells.append("Dimension Door")
            domainSpells.append("Polymorph")
        if playerLevel >= 9:
            domainSpells.append("Dominate Person")
            domainSpells.append("Modify Memory")

    # War Spells
    if clericDomain == "War":
        if playerLevel >= 1:
            domainSpells = ["Divine Favor", "Shield of Faith"]
        if playerLevel >= 3:
            domainSpells.append("Magic Weapon")
            domainSpells.append("Spiritual Weapon")
        if playerLevel >= 5:
            domainSpells.append("Crusader's Mantle")
            domainSpells.append("Spirit Guardians")
        if playerLevel >= 7:
            domainSpells.append("Freedom of Movement")
            domainSpells.append("Stoneskin")
        if playerLevel >= 9:
            domainSpells.append("Flame Strike")
            domainSpells.append("Hold Monster")

    saveDC = 8 + proficiency + wisdomModifier
    attackModifier = proficiency + wisdomModifier
    cantrips = random.sample(clericCantrips, cantripsKnown) + domainCantrips
    numberOfCantrips = f"{cantripsKnown} + Domain Cantrips ({len(domainCantrips)})"
    numberOfSpells = wisdomModifier + playerLevel
    spells = random.sample(clericSpells, numberOfSpells) + domainSpells

# Druid
druidCircle = ""
circleSpells = []
if playerClass == "Druid":
    preparedSpellcasting = True
    if playerLevel < 4:
        cantripsKnown = 2
    if 3 < playerLevel < 10:
        cantripsKnown = 3
    if playerLevel > 9:
        cantripsKnown = 4
    if playerLevel < 3:
        druidSpells = druid1Spells
    if 2 < playerLevel < 5:
        druidSpells = druid1Spells + druid2Spells
    if 4 < playerLevel < 7:
        druidSpells = druid1Spells + druid2Spells + druid3Spells
    if 6 < playerLevel < 9:
        druidSpells = druid1Spells + druid2Spells + druid3Spells + druid4Spells
    if 8 < playerLevel < 11:
        druidSpells = druid1Spells + druid2Spells + druid3Spells + druid4Spells + druid5Spells
    if 10 < playerLevel < 13:
        druidSpells = druid1Spells + druid2Spells + druid3Spells + druid4Spells + druid5Spells + druid6Spells
    if 12 < playerLevel < 15:
        druid1Spells = druid1Spells + druid2Spells + druid3Spells + druid4Spells + druid5Spells + druid6Spells
        druidSpells = druid1Spells + druid7Spells
    if 14 < playerLevel < 17:
        druid1Spells = druid1Spells + druid2Spells + druid3Spells + druid4Spells
        druidSpells = druid1Spells + druid5Spells + druid6Spells + druid7Spells + druid8Spells
    if playerLevel > 16:
        druid1Spells = druid1Spells + druid2Spells + druid3Spells + druid4Spells
        druidSpells = druid1Spells + druid5Spells + druid6Spells + druid7Spells + druid8Spells + druid9Spells

    # Circle Spells
    if druidCircle == "Circle of Spores":
        if playerLevel >= 3:
            circleSpells = ["Blindness/Deafness", " Gentle Repose"]
        if playerLevel >= 5:
            circleSpells.append("Animate Dead")
            circleSpells.append("Gaseous Form")
        if playerLevel >= 7:
            circleSpells.append("Blight")
            circleSpells.append("Confusion")
        if playerLevel >= 9:
            circleSpells.append("Cloudkill")
            circleSpells.append("Contagion")

    if druidCircle == "Circle of the Land: Arctic":
        cantripsKnown = cantripsKnown + 1
        if playerLevel >= 3:
            circleSpells = ["Blindness/Deafness", "Gentle Repose"]
        if playerLevel >= 5:
            circleSpells.append("Animate Dead")
            circleSpells.append("Gaseous Form")
        if playerLevel >= 7:
            circleSpells.append("Blight")
            circleSpells.append("Confusion")
        if playerLevel >= 9:
            circleSpells.append("Cloudkill")
            circleSpells.append("Contagion")

    if druidCircle == "Circle of the Land: Coast":
        cantripsKnown = cantripsKnown + 1
        if playerLevel >= 3:
            circleSpells = ["Mirror Image", "Misty Step"]
        if playerLevel >= 5:
            circleSpells.append("Water Breathing")
            circleSpells.append("Water Walk")
        if playerLevel >= 7:
            circleSpells.append("Control Water")
            circleSpells.append("Freedom of Movement")
        if playerLevel >= 9:
            circleSpells.append("Conjure Elemental")
            circleSpells.append("Scrying")

    if druidCircle == "Circle of the Land: Desert":
        cantripsKnown = cantripsKnown + 1
        if playerLevel >= 3:
            circleSpells = ["Blur", "Silence"]
        if playerLevel >= 5:
            circleSpells.append("Create Food and Water")
            circleSpells.append("Protection from Energy")
        if playerLevel >= 7:
            circleSpells.append("Blight")
            circleSpells.append("Hallucinatory Terrain")
        if playerLevel >= 9:
            circleSpells.append("Insect Plague")
            circleSpells.append("Wall of Stone")

    if druidCircle == "Circle of the Land: Forest":
        cantripsKnown = cantripsKnown + 1
        if playerLevel >= 3:
            circleSpells = ["Barkskin", "Spider Climb"]
        if playerLevel >= 5:
            circleSpells.append("Call Lightning")
            circleSpells.append("Plant Growth")
        if playerLevel >= 7:
            circleSpells.append("Divination")
            circleSpells.append("Freedom of Movement")
        if playerLevel >= 9:
            circleSpells.append("Commune with Nature")
            circleSpells.append("Tree Stride")

    if druidCircle == "Circle of the Land: Grassland":
        cantripsKnown = cantripsKnown + 1
        if playerLevel >= 3:
            circleSpells = ["Invisibility", "Pass Without Trace"]
        if playerLevel >= 5:
            circleSpells.append("Daylight")
            circleSpells.append("Haste")
        if playerLevel >= 7:
            circleSpells.append("Divination")
            circleSpells.append("Freedom of Movement")
        if playerLevel >= 9:
            circleSpells.append("Dream")
            circleSpells.append("Insect Plague")

    if druidCircle == "Circle of the Land: Mountain":
        cantripsKnown = cantripsKnown + 1
        if playerLevel >= 3:
            circleSpells = ["Spider CLimb", "Spike Growth"]
        if playerLevel >= 5:
            circleSpells.append("Lightning Bolt")
            circleSpells.append("Meld into Stone")
        if playerLevel >= 7:
            circleSpells.append("Stone Shape")
            circleSpells.append("Stoneskin")
        if playerLevel >= 9:
            circleSpells.append("Passwall")
            circleSpells.append("Wall of Stone")

    if druidCircle == "Circle of the Land: Swamp":
        cantripsKnown = cantripsKnown + 1
        if playerLevel >= 3:
            circleSpells = ["Darkness", "Melf's Acid Arrow"]
        if playerLevel >= 5:
            circleSpells.append("Water Walk")
            circleSpells.append("Stinking Cloud")
        if playerLevel >= 7:
            circleSpells.append("Freedom of Movement")
            circleSpells.append("Locate Creature")
        if playerLevel >= 9:
            circleSpells.append("Insect Plague")
            circleSpells.append("Scrying")

    if druidCircle == "Circle of the Land: Underdark":
        cantripsKnown = cantripsKnown + 1
        if playerLevel >= 3:
            circleSpells = ["Spider CLimb", "Web"]
        if playerLevel >= 5:
            circleSpells.append("Gaseous Form")
            circleSpells.append("Stinking Cloud")
        if playerLevel >= 7:
            circleSpells.append("Greater Invisibility")
            circleSpells.append("Stone Shape")
        if playerLevel >= 9:
            circleSpells.append("Cloudkill")
            circleSpells.append("Insect Plague")

    saveDC = 8 + proficiency + wisdomModifier
    attackModifier = proficiency + wisdomModifier
    numberOfCantrips = cantripsKnown
    cantrips = random.sample(druidCantrips, cantripsKnown)
    numberOfSpells = wisdomModifier + playerLevel
    spells = random.sample(druidSpells, numberOfSpells)

# Paladin
oathSpells = []
if playerClass == "Paladin":
    preparedSpellcasting = True
    if 1 < playerLevel < 5:
        paladinSpells = paladin1Spells
    if 4 < playerLevel < 9:
        paladinSpells = paladin1Spells + paladin2Spells
    if 8 < playerLevel < 13:
        paladinSpells = paladin1Spells + paladin2Spells + paladin3Spells
    if 12 < playerLevel < 17:
        paladinSpells = paladin1Spells + paladin2Spells + paladin3Spells + paladin4Spells
    if 16 < playerLevel:
        paladinSpells = paladin1Spells + paladin2Spells + paladin3Spells + paladin4Spells + paladin5Spells

    if sacredOath == "Oath of the Ancients":
        if playerLevel > 2:
            oathSpells = ["Ensnaring Strike", "Speak with Animals"]
        if playerLevel > 4:
            oathSpells.append("Moonbeam")
            oathSpells.append("Misty Step")
        if playerLevel > 8:
            oathSpells.append("Plant Growth")
            oathSpells.append("Protection From Energy")
        if playerLevel > 12:
            oathSpells.append("Ice Storm")
            oathSpells.append("Stoneskin")
        if playerLevel > 16:
            oathSpells.append("Commune with Nature")
            oathSpells.append("Tree Stride")

    if sacredOath == "Oath of Conquest":
        if playerLevel > 2:
            oathSpells = ["Armor of Agathys", "Command"]
        if playerLevel > 4:
            oathSpells.append("Hold Person")
            oathSpells.append("Spiritual Weapon")
        if playerLevel > 8:
            oathSpells.append("Bestow Curse")
            oathSpells.append("Fear")
        if playerLevel > 12:
            oathSpells.append("Dominate Beast")
            oathSpells.append("Stoneskin")
        if playerLevel > 16:
            oathSpells.append("Cloudkill")
            oathSpells.append("Dominate Person")

    if sacredOath == "Oath of the Crown":
        if playerLevel > 2:
            oathSpells = ["Command", "Compelled Duel"]
        if playerLevel > 4:
            oathSpells.append("Warding Bond")
            oathSpells.append("Zone of Truth")
        if playerLevel > 8:
            oathSpells.append("Aura of Vitality")
            oathSpells.append("Spirit Guardians")
        if playerLevel > 12:
            oathSpells.append("Banishment")
            oathSpells.append("Guardian of Faith")
        if playerLevel > 16:
            oathSpells.append("Circle of Power")
            oathSpells.append("Geas")

    if sacredOath == "Oath of Devotion":
        if playerLevel > 2:
            oathSpells = ["Protection from Evil and Good", "Sanctuary"]
        if playerLevel > 4:
            oathSpells.append("Lesser Restoration")
            oathSpells.append("Zone of Truth")
        if playerLevel > 8:
            oathSpells.append("Beacon of Hope")
            oathSpells.append("Dispel Magic")
        if playerLevel > 12:
            oathSpells.append("Freedom of Movement")
            oathSpells.append("Guardian of Faith")
        if playerLevel > 16:
            oathSpells.append("Commune")
            oathSpells.append("Flame Strike")

    if sacredOath == "Oath of Vengeance":
        if playerLevel > 2:
            oathSpells = ["Bane", "Hunter's Mark"]
        if playerLevel > 4:
            oathSpells.append("Hold Person")
            oathSpells.append("Misty Step")
        if playerLevel > 8:
            oathSpells.append("Haste")
            oathSpells.append("Protection from Energy")
        if playerLevel > 12:
            oathSpells.append("Banishment")
            oathSpells.append("Dimension Door")
        if playerLevel > 16:
            oathSpells.append("Hold Monster")
            oathSpells.append("Scrying")

    if sacredOath == "Oathbreaker":
        if playerLevel > 2:
            oathSpells = ["Hellish Rebuke", "Inflict Wounds"]
        if playerLevel > 4:
            oathSpells.append("Crown of Madness")
            oathSpells.append("Darkness")
        if playerLevel > 8:
            oathSpells.append("Animate Dead")
            oathSpells.append("Bestow Curse")
        if playerLevel > 12:
            oathSpells.append("Blight")
            oathSpells.append("Confusion")
        if playerLevel > 16:
            oathSpells.append("Contagion")
            oathSpells.append("Dominate Person")

    numberOfSpells = charismaModifier + math.floor(playerLevel / 2)
    spells = random.sample(paladinSpells, numberOfSpells)
    saveDC = 8 + proficiency + charismaModifier
    attackModifier = proficiency + charismaModifier

# Ranger
conclaveSpells = []
if playerClass == "Ranger":
    if 1 < playerLevel < 5:
        rangerSpells = ranger1Spells
    if 4 < playerLevel < 9:
        rangerSpells = ranger1Spells + ranger2Spells
    if 8 < playerLevel < 13:
        rangerSpells = ranger1Spells + ranger2Spells + ranger3Spells
    if 12 < playerLevel < 17:
        rangerSpells = ranger1Spells + ranger2Spells + ranger3Spells + ranger4Spells
    if 16 < playerLevel:
        rangerSpells = ranger1Spells + ranger2Spells + ranger3Spells + ranger4Spells + ranger5Spells

    if rangerConclave == "Gloom Stalker":
        if playerLevel > 2:
            conclaveSpells = ["Disguise Self"]
        if playerLevel > 4:
            conclaveSpells.append("Rope Trick")
        if playerLevel > 8:
            conclaveSpells.append("Fear")
        if playerLevel > 12:
            conclaveSpells.append("Greater Invisibility")
        if playerLevel > 16:
            conclaveSpells.append("Seeming")

    if rangerConclave == "Horizon Walker Conclave":
        if playerLevel > 2:
            conclaveSpells = ["Protection from Evil and Good"]
        if playerLevel > 4:
            conclaveSpells.append("Misty Step")
        if playerLevel > 8:
            conclaveSpells.append("Haste")
        if playerLevel > 12:
            conclaveSpells.append("Banishment")
        if playerLevel > 16:
            conclaveSpells.append("Teleportaion Circle")

    if rangerConclave == "Monster Slayer Conclave":
        if playerLevel > 2:
            conclaveSpells = ["Protection From Good and Evil"]
        if playerLevel > 4:
            conclaveSpells.append("Zone of Truth")
        if playerLevel > 8:
            conclaveSpells.append("Magic Circle")
        if playerLevel > 12:
            conclaveSpells.append("Banishment")
        if playerLevel > 16:
            conclaveSpells.append("Hold Monster")

    numberOfSpells = wisdomModifier + math.floor(playerLevel / 2)
    spells = random.sample(rangerSpells, numberOfSpells) + conclaveSpells
    saveDC = 8 + proficiency + wisdomModifier
    attackModifier = proficiency + wisdomModifier

# Sorcerer
divineAffinity = ""
if playerClass == "Sorcerer":
    # This Origin is declared early because it changes the spell lists that can be used in the spell selection options.
    if sorcerousOrigin == "Divine Soul":
        sorcererCantrips = sorcererCantrips + clericCantrips
        sorcerer1spells = sorcerer1Spells + cleric1Spells
        sorcerer2spells = sorcerer2Spells + cleric2Spells
        sorcerer3spells = sorcerer3Spells + cleric3Spells
        sorcerer4spells = sorcerer4Spells + cleric4Spells
        sorcerer5spells = sorcerer5Spells + cleric5Spells
        sorcerer6spells = sorcerer6Spells + cleric6Spells
        sorcerer7spells = sorcerer7Spells + cleric7Spells
        sorcerer8spells = sorcerer8Spells + cleric8Spells
        sorcerer9spells = sorcerer9Spells + cleric9Spells
        divineAffinity = ["Good", "Evil", "Law", "Chaos", "Neutrality"]
        divineAffinity = random.choice(divineAffinity)
    if playerLevel < 4:
        cantripsKnown = 4
    if 3 < playerLevel < 10:
        cantripsKnown = 5
    if playerLevel > 9:
        cantripsKnown = 6
    if playerLevel < 12:
        numberOfSpells = playerLevel + 1
    if playerLevel == 12 or playerLevel == 13:
        numberOfSpells = playerLevel
    if playerLevel == 14:
        numberOfSpells = 13
    if playerLevel == 15 or playerLevel == 16:
        numberOfSpells = 14
    if playerLevel > 16:
        numberOfSpells = 15
    if playerLevel < 3:
        sorcererSpells = sorcerer1Spells
    if 2 < playerLevel < 5:
        sorcererSpells = sorcerer1Spells + sorcerer2Spells
    if 4 < playerLevel < 7:
        sorcererSpells = sorcerer1Spells + sorcerer2Spells + sorcerer3Spells
    if 6 < playerLevel < 9:
        sorcererSpells = sorcerer1Spells + sorcerer2Spells + sorcerer3Spells + sorcerer4Spells
    if 8 < playerLevel < 11:
        sorcererSpells = sorcerer1Spells + sorcerer2Spells + sorcerer3Spells + sorcerer4Spells + sorcerer5Spells
    if 10 < playerLevel < 13:
        sorcerer1Spells = sorcerer1Spells + sorcerer2Spells + sorcerer3Spells + sorcerer4Spells + sorcerer5Spells
        sorcererSpells = sorcerer1Spells + sorcerer6Spells
    if 12 < playerLevel < 15:
        sorcerer1Spells = sorcerer1Spells + sorcerer2Spells + sorcerer3Spells + sorcerer4Spells + sorcerer5Spells
        sorcererSpells = sorcerer1Spells + sorcerer6Spells + sorcerer7Spells
    if 14 < playerLevel < 17:
        sorcerer1Spells = sorcerer1Spells + sorcerer2Spells + sorcerer3Spells + sorcerer4Spells + sorcerer5Spells
        sorcererSpells = sorcerer1Spells + sorcerer6Spells + sorcerer7Spells + sorcerer8Spells
    if playerLevel > 16:
        sorcerer1Spells = sorcerer1Spells + sorcerer2Spells + sorcerer3Spells + sorcerer4Spells + sorcerer5Spells
        sorcererSpells = sorcerer1Spells + sorcerer6Spells + sorcerer7Spells + sorcerer8Spells + sorcerer9Spells
    if divineAffinity == "Good":
        sorcererSpells.append("Cure Wounds")
    if divineAffinity == "Evil":
        sorcererSpells.append("Inflict Wounds")
    if divineAffinity == "Law":
        sorcererSpells.append("Bless")
    if divineAffinity == "Chaos":
        sorcererSpells.append("Bane")
    if divineAffinity == "Neutrality":
        sorcererSpells.append("Protection from Good and Evil")
    cantrips = random.sample(sorcererCantrips, cantripsKnown)
    numberOfCantrips = cantripsKnown
    spells = random.sample(sorcererSpells, numberOfSpells)
    saveDC = 8 + proficiency + charismaModifier
    attackModifier = proficiency + charismaModifier

# Warlock
arcanumSpells = []
if playerClass == "Warlock":
    if playerLevel < 4:
        cantripsKnown = 2
    if 3 < playerLevel < 10:
        cantripsKnown = 3
    if playerLevel > 9:
        cantripsKnown = 4
    if playerLevel <= 9:
        numberOfSpells = playerLevel + 1
    if playerLevel == 10:
        numberOfSpells = 10
    if playerLevel == 11 or playerLevel == 12:
        numberOfSpells = 11
    if playerLevel == 13 or playerLevel == 14:
        numberOfSpells = 12
    if playerLevel == 15 or playerLevel == 16:
        numberOfSpells = 13
    if playerLevel == 17 or playerLevel == 18:
        numberOfSpells = 14
    if playerLevel >= 19:
        numberOfSpells = 15
    if 0 < playerLevel < 3:
        warlockSpells = warlock1Spells
    if 2 < playerLevel < 5:
        warlockSpells = warlock1Spells + warlock2Spells
    if 4 < playerLevel < 7:
        warlockSpells = warlock1Spells + warlock2Spells + warlock3Spells
    if 6 < playerLevel < 9:
        warlockSpells = warlock1Spells + warlock2Spells + warlock3Spells + warlock4Spells
    if 8 < playerLevel:
        warlockSpells = warlock1Spells + warlock2Spells + warlock3Spells + warlock4Spells + warlock5Spells
    if playerLevel >= 11:
        arcanumSpells.append(random.choice(warlock6Spells))
    if playerLevel >= 13:
        arcanumSpells.append(random.choice(warlock7Spells))
    if playerLevel >= 15:
        arcanumSpells.append(random.choice(warlock8Spells))
    if playerLevel >= 17:
        arcanumSpells.append(random.choice(warlock9Spells))

    cantrips = random.sample(warlockCantrips, cantripsKnown)
    numberOfCantrips = cantripsKnown
    spells = random.sample(warlockSpells, numberOfSpells) + arcanumSpells
    saveDC = 8 + proficiency + charismaModifier
    attackModifier = proficiency + charismaModifier

# Wizard
if playerClass == "Wizard":
    preparedSpellcasting = True
    if playerLevel < 4:
        cantripsKnown = 3
    if 3 < playerLevel < 10:
        cantripsKnown = 4
    if playerLevel > 9:
        cantripsKnown = 5
    if playerLevel < 3:
        wizardSpells = wizard1Spells
    if 2 < playerLevel < 5:
        wizardSpells = wizard1Spells + wizard2Spells
    if 4 < playerLevel < 7:
        wizardSpells = wizard1Spells + wizard2Spells + wizard3Spells
    if 6 < playerLevel < 9:
        wizardSpells = wizard1Spells + wizard2Spells + wizard3Spells + wizard4Spells
    if 8 < playerLevel < 11:
        wizardSpells = wizard1Spells + wizard2Spells + wizard3Spells + wizard4Spells + wizard5Spells
    if 10 < playerLevel < 13:
        wizardSpells = wizard1Spells + wizard2Spells + wizard3Spells + wizard4Spells + wizard5Spells + wizard6Spells
    if 12 < playerLevel < 15:
        wizard1Spells = wizard1Spells + wizard2Spells + wizard3Spells + wizard4Spells + wizard5Spells + wizard6Spells
        wizardSpells = wizard1Spells + wizard7Spells
    if 14 < playerLevel < 17:
        wizard1Spells = wizard1Spells + wizard2Spells + wizard3Spells + wizard4Spells + wizard5Spells + wizard6Spells
        wizardSpells = wizard1Spells + wizard7Spells + wizard8Spells
    if playerLevel > 16:
        wizard1Spells = wizard1Spells + wizard2Spells + wizard3Spells + wizard4Spells + wizard5Spells + wizard6Spells
        wizardSpells = wizard1Spells + wizard7Spells + wizard8Spells + wizard9Spells

    if wizardSchool == "School of Illusion":
        cantripsKnown = cantripsKnown + 1

    cantrips = random.sample(wizardCantrips, cantripsKnown)
    numberOfCantrips = cantripsKnown
    spellsKnown = random.sample(wizardSpells, (4 + (playerLevel * 2)))
    numberOfSpells = intelligenceModifier + playerLevel
    spells = random.sample(spellsKnown, numberOfSpells)
    saveDC = 8 + proficiency + intelligenceModifier
    attackModifier = proficiency + intelligenceModifier


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

if playerClass == "Barbarian":
    AC = 10 + constitutionModifier + dexterityModifier

if playerClass == "Monk":
    AC = 10 + dexterityModifier + wisdomModifier

"""
Characteristics: Personality Traits, Ideals, Bonds, Flaws
"""
# Personality Traits
personalityTraits = ["I idolize a particular hero of my faith and constantly refer to that person's deeds and example.",
                     "I can find common ground between the fiercest enemies, empathizing with them and always working "
                     "toward peace.",
                     "I see omens in every event and action. The gods try to speak to us, we just need to listen.",
                     "Nothing can shake my optimistic attitude.",
                     "I quote (or misquote) the sacred texts and proverbs in almost every situation.",
                     "I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods.",
                     "I've enjoyed fine food, drink, and high society among my temple's elite. Rough living "
                     "grates on me.",
                     "I've spent so long in the temple that I have little practical experience dealing with "
                     "people in the outside world.",
                     "I fall in and out of love easily, and am always pursuing someone.",
                     "I have a joke for every occasion, especially occasions where humor is inappropriate.",
                     "Flattery is my preferred trick for getting what I want.",
                     "I'm a born gambler who can't resist taking a risk for a potential payoff.",
                     "I lie about almost everything, even when there's no good reason to.",
                     "Sarcasm and insults are my weapons of choice.",
                     "I keep multiple holy symbols on me and invoke whatever deity might come in useful at "
                     "any given moment.",
                     "I pocket anything I see that might have some value.",
                     "I always have plan for what to do when things go wrong.",
                     "I am always calm, no matter what the situation. I never raise my voice or let my emotions"
                     " control me.",
                     "The first thing I do in a new place is note the locations of everything valuable--or"
                     " where such things could be hidden.",
                     "I would rather make a new friend than a new enemy.",
                     "I am incredibly slow to trust. Those who seem the fairest often have the most to hide.",
                     "I don't pay attention to the risks in a situation. Never tell me the odds.",
                     "The best way to get me to do something is to tell me I can't do it.",
                     "I blow up at the slightest insult.", "I know a story relevant to almost every situation.",
                     "Whenever I come to a new place, I collect local rumors and spread gossip.",
                     "I'm a hopeless romantic, always searching for that 'special someone'.",
                     "Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
                     "I love a good insult, even one directed at me.",
                     "I get bitter if I'm not the center of attention.",
                     "I'll settle for nothing less than perfection.",
                     "I change my mood or my mind as quickly as I change key in a song.",
                     "I judge people by their actions, not their words.",
                     "If someone is in trouble, I'm always willing to lend help.",
                     "When I set my mind to something, I follow through no matter what gets in my way.",
                     "I have a strong sense of fair play and always try to find the most equitable solution to "
                     "arguments.",
                     "I'm confident in my own abilities and do what I can to instill confidence in others.",
                     "Thinking is for other people. I prefer action.",
                     "I misuse long words in an attempt to sound smarter.",
                     "I get bored easily. When am I going to get on with my destiny.",
                     "I believe that everything worth doing is worth doing right. I can't help it-"
                     "-I'm a perfectionist.", "I'm a snob who looks down on those who can't appreciate fine art.",
                     "I always want to know how things work and what makes people tick.",
                     "I'm full of witty aphorisms and have a proverb for every occasion.",
                     "I'm rude to people who lack my commitment to hard work and fair play.",
                     "I like to talk at length about my profession.",
                     "I don't part with my money easily and will haggle tirelessly to get the best deal possible.",
                     "I'm well known for my work, and I want to make sure everyone appreciates it. "
                     "I'm always taken aback when people haven't heard of me.",
                     "I've been isolated for so long that I rarely speak, preferring gestures and the occasional g"
                     "runt.", "I am utterly serene, even in the face of disaster.",
                     "The leader of my community has something wise to say on every topic, and I am eager to sh"
                     "are that wisdom.", "I feel tremendous empathy for all who suffer.",
                     "I'm oblivious to etiquette and social expectations.",
                     "I connect everything that happens to me to a grand cosmic plan.",
                     "I often get lost in my own thoughts and contemplations, becoming oblivious to my surroundings.",
                     "I am working on a grand philosophical theory and love sharing my ideas.",
                     "My eloquent flattery makes everyone I talk to feel like the most wonderful and important person "
                     "in the world.", "The common folk love me for my kindness and generosity.",
                     "No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses.",
                     "I take great pains to always look my best and follow the latest fashions.",
                     "I don't like to get my hands dirty, and I won't be caught dead in unsuitable accommodations.",
                     "Despite my birth, I do not place myself above other folk. We all have the same blood.",
                     "My favor, once lost, is lost forever.",
                     "If you do me an injury, I will crush you, ruin your name, and salt your fields.",
                     "I'm driven by a wanderlust that led me away from home.",
                     "I watch over my friends as if they were a litter of newborn pups.",
                     "I once ran twenty-five miles without stopping to warn my clan of an approaching orc horde. I'd d"
                     "o it again if I had to.", "I have a lesson for every situation, drawn from observing nature.",
                     "I place no stock in wealthy or well-mannered folk. Money and manners won't save you from a hungr"
                     "y owlbear.", "I was, in fact, raised by wolves.",
                     "I'm always picking things up, absently fiddling with them, and sometimes accidentally breaking t"
                     "hem.", "I feel far more comfortable around animals than people.",
                     "I use polysyllabic words to convey the impression of great erudition.",
                     "I've read every book in the world's greatest libraries--or like to boast that I have.",
                     "I'm used to helping out those who aren't as smart as I am, and I patiently explain anything and "
                     "everything to others.", "There's nothing I like more than a good mystery.",
                     "I'm willing to listen to every side of an argument before I make my own judgment.",
                     "I...speak...slowly...when talking...to idiots...which...almost...everyone...is...compared...to m"
                     "e.", "I am horribly, horribly awkward in social situations.",
                     "I'm convinced that people are always trying to steal my secrets.",
                     "My friends know they can rely on me, no matter what.",
                     "I work hard so that I can play hard when the work is done.",
                     "I enjoy sailing into new ports and making new friends over a flagon of ale.",
                     "I stretch the truth for the sake of a good story.",
                     "To me, a tavern brawl is a nice way to get to know a new city.",
                     "I never pass up a friendly wager.", "My language is as foul as an otyugh nest.",
                     "I like a job well done, especially if I can convince someone else to do it.",
                     "I'm always polite and respectful.",
                     "I'm haunted by memories of war. I can't get the images of violence out of my mind.",
                     "I've lost too many friends, and I'm slow to make new ones.",
                     "I'm full of inspiring and cautionary tales from my military experience relevant to almost every "
                     "combat situation.", "I can stare down a hellhound without flinching.",
                     "I enjoy being strong and like breaking things.", "I have a crude sense of humor.",
                     "I face problems head-on. A simple direct solution is the best path to success.",
                     "I hide scraps of food and trinkets away in my pockets.",
                     "I ask a lot of questions.",
                     "I like to squeeze into small places where no one else can get to me.",
                     "I sleep with my back to a wall or tree, with everything I own wrapped in a bundle in my arms.",
                     "I eat like a pig and have bad manners.",
                     "I think anyone who's nice to me is hiding evil intent.", "I don't like to bathe.",
                     "I bluntly say what other people are hinting or hiding."]
personalityTraits = random.sample(personalityTraits, 2)

# Ideals Lists and Selection
lawfulIdeals = ["Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld.",
                "Power. I hope to one day rise to the top of my faith's religious hierarchy.",
                "Fairness. I never target people who can't afford to lose a few coins.",
                "Honor. I don't steal from others in the trade.",
                "Tradition. The stories, legends, and songs of the past must never be forgotten.",
                "Fairness. No one should get preferential treatment before the law, and no one is above the law.",
                "Community. It is the duty of all civilized people to strengthen the bonds of community and "
                "the security of civilization.",
                "Logic. Emotions must not cloud our sense of what is right and true, or our logical thinking.",
                "Responsibility. It is my duty to respect the authority of those above me, just as those below "
                "me must respect mine.", "Honor. If I dishonor myself, I dishonor my whole clan.",
                "Logic. Emotions must not cloud our logical thinking.",
                "Fairness. We all do the work, so we all share in the rewards.",
                "Responsibility. I do what I must and obey just authority.",
                "Community. We have to take care of each other, because no one else is going to do it."]
chaoticIdeals = ["Change. We must help bring about the changes the gods are constantly working in the world.",
                 "Independence. I am a free spirit--no one tells me what to do.",
                 "Creativity. I never run the same con twice.",
                 "Freedom. Chains are meant to be broken, as are those who would forge them.",
                 "Creativity. The world is in need of new ideas and bold action.",
                 "Freedom. Tyrants must not be allowed to oppress the people.",
                 "Freedom. Everyone should be free to pursue his or her livelihood.",
                 "Free Thinking. Inquiry and curiosity are the pillars of progress.",
                 "Independence. I must prove that I can handle myself without the coddling of my family.",
                 "Change. Life is like the seasons, in constant change, and we must change with it.",
                 "No Limits. Nothing should fetter the infinite possibility inherent in all existence.",
                 "Freedom. The sea is freedom--the freedom to go anywhere and do anything.",
                 "Independence. When people follow orders blindly they embrace a kind of tyranny.",
                 "Change. The low are lifted up, and the high and mighty are brought down. Change is the "
                 "nature of things."]
goodIdeals = ["Respect. All people, rich or poor, deserve respect.",
              "Greater Good. Our lot is to lay down our lives in defense of others.",
              "Respect. The thing that keeps a ship together is mutual respect between captain and crew.",
              "Beauty. What is beautiful points us beyond itself toward what is true.",
              "Greater Good. It is each person's responsibility to make the most happiness for the whole tribe.",
              "Noble Obligation. It is my duty to protect and care for the people beneath me.",
              "Respect. Respect is due to me because of my position, but all people regardless of station deserve "
              "to be treated with dignity.",
              "Greater Good. My gifts are meant to be shared with all, not used for my own benefit.",
              "Generosity. My talents were given to me so that I could use them to benefit the world.",
              "Respect. People deserve to be treated with dignity and respect.",
              "Redemption. There's a spark of good in everyone.",
              "Beauty. When I perform, I make the world better than it was.",
              "Charity. I steal from the wealthy so that I can help people in need.",
              "Friendship. Material goods come and go. Bonds of friendship last forever.",
              "Charity. I distribute money I acquire to the people who really need it.",
              "Charity. I always try to help those in need, no matter what the personal cost."]
evilIdeals = ["Greed. I will do whatever it takes to become wealthy.",
              "Greed. I'm only in it for the money and fame. ",
              "Might. If I become strong, I can take what I want--what I deserve.",
              "Greed. I'm only in it for the money.",
              "Power. Solitude and contemplation are paths toward mystical or magical power.",
              "Power. If I can attain more power, no one will tell me what to do.",
              "Might. The strongest are meant to rule.",
              "Power. Knowledge is the path to power and domination.",
              "Master. I'm a predator, and the other ships on the sea are my prey.",
              "Might. In life as in war, the stronger force wins.",
              "Retribution. The rich need to be shown what life and death are like in the gutters."]
neutralIdeals = ["People. I help people who help me--that's what keeps us alive.",
                 "Ideals aren't worth killing for or going to war for.",
                 "People. I'm committed to my crewmates, not to ideals.",
                 "Knowledge. The path to power and self-improvement is through knowledge.",
                 "Nature. The natural world is more important than all the constructs of civilization.",
                 "Live and Let Live. Meddling in the affairs of others only causes trouble.",
                 "People. I'm committed to the people I care about, not to ideals.",
                 "Sincerity. There's no good pretending to be something I'm not.",
                 "People. I like seeing the smiles on people's faces when I perform. That's all that matters.",
                 "People. I'm loyal to my friends, not to any ideals, and everyone else can take a trip down the "
                 "Styx for all I care."]
anyIdeals = ["Aspiration. I'm going to prove that I'm worthy of a better life.",
             "Nation. My city, nation, or people are all that matter.",
             "Aspiration. Someday I'll own my own ship and chart my own destiny.",
             "Self-improvement. The goal of a life of study is the betterment of oneself.",
             "Glory. I must earn glory in battle, for myself and my clan.",
             "Family. Blood runs thicker than water.",
             "Self-Knowledge. If you know yourself, there're nothing left to know.",
             "Aspiration. I work hard to be the best there is at my craft.",
             "Destiny. Nothing and no one can steer me away from my higher calling.",
             "Honesty. Art should reflect the soul; it should come from within and reveal who we really are.",
             "Aspiration. I'm determined to make something of myself.",
             "Aspiration. I seek to prove my self worthy of my god's favor by matching my actions against his or "
             "her teachings."]

# Adding in the ideals applicable to anyone.
lawfulIdeals = lawfulIdeals + anyIdeals
chaoticIdeals = chaoticIdeals + anyIdeals
goodIdeals = goodIdeals + anyIdeals
evilIdeals = evilIdeals + anyIdeals
neutralIdeals = neutralIdeals + anyIdeals

# Making sure the ideals are unique.
orderIdeal = ""
moralIdeal = ""
while orderIdeal == moralIdeal:
    if playerAlignment == "Lawful Good" or playerAlignment == "Lawful Neutral" or playerAlignment == "Lawful Evil":
        orderIdeal = random.choice(lawfulIdeals)
    if playerAlignment == "Chaotic Good" or playerAlignment == "Chaotic Neutral" or playerAlignment == "Chaotic Evil":
        orderIdeal = random.choice(chaoticIdeals)
    if playerAlignment == "True Neutral" or playerAlignment == "Lawful Neutral" or playerAlignment == "Chaotic Neutral":
        orderIdeal = random.choice(neutralIdeals)
    if playerAlignment == "Lawful Good" or playerAlignment == "Neutral Good" or playerAlignment == "Chaotic Good":
        moralIdeal = random.choice(goodIdeals)
    if playerAlignment == "Lawful Evil" or playerAlignment == "Neutral Evil" or playerAlignment == "Chaotic Evil":
        moralIdeal = random.choice(evilIdeals)
    if playerAlignment == "True Neutral" or playerAlignment == "Neutral Good" or playerAlignment == "Neutral Evil":
        moralIdeal = random.choice(neutralIdeals)

# Concatination
ideals = [orderIdeal, moralIdeal]

# Bonds
bonds = ["I would die to recover an ancient artifact of my faith that was lost long ago.",
         "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.",
         "I owe me life to the priest who took me in when my parents died.",
         "Everything I do is for the common people.",
         "I will do anything to protect the temple where I served.",
         "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy.",
         "I fleeced the wrong person and must work to ensure that this individual never crosses paths with me "
         "or those I care about.",
         "I owe everything to my mentor--a horrible person who's probably rotting in jail somewhere.",
         "Somewhere out there I have a child who doesn't know me.", "I'm making the world better for him or her.",
         "I come from a noble family, and one day I'll reclaim my lands and title from those who stole them from me.",
         "A powerful person killed someone I love", "Some day soon, I'll have my revenge.",
         "I swindled and ruined a person who didn't deserve it. I seek to atone for my misdeeds but might never b"
         "e able to forgive myself.", "I'm trying to pay off an old debt I owe to a generous benefactor.",
         "My ill-gotten gains go to support my family.",
         "Something important was taken from me, and I aim to steal it back.",
         "I will become the greatest thief that ever lived.",
         "I'm guilty of a terrible crime. I hope I can redeem myself for it.",
         "Someone I loved died because of a mistake I made. That will never happen again.",
         "My instrument is my most treasured possession, and it reminds me of someone I love.",
         "Someone stole my precious instrument, and someday I'll get it back.",
         "I want to be famous, whatever it takes.",
         "I idolize a hero of the old tales and measure my deeds against that person's.",
         "I will do anything to prove myself superior to me hated rival.",
         "I would do anything for the other members of my old troupe.",
         "I have a family, but I have no idea where they are. One day, I hope to see them again.",
         "I worked the land, I love the land, and I will protect the land.",
         "A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.",
         "My tools are symbols of my past life, and I carry them so that I will never forget my roots.",
         "I protect those who cannot protect themselves"
         "I wish my childhood sweetheart had come with me to pursue my destiny.",
         "The workshop where I learned my trade is the most important place in the world to me.",
         "I created a great work for someone, and then found them unworthy to receive it. I'm still looking for som"
         "eone worthy.", "I owe my guild a great debt for forging me into the person I am today.",
         "I pursue wealth to secure someone's love.",
         "One day I will return to my guild and prove that I am the greatest artisan of them all.",
         "I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood.",
         "Nothing is more important than the other members of my hermitage, order, or association.",
         "I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them.",
         "I'm still seeking the enlightenment I pursued in my seclusion, and it still eludes me.",
         "I entered seclusion because I loved someone I could not have.",
         "Should my discovery come to light, it could bring ruin to the world.",
         "My isolation gave me great insight into a great evil that only I can destroy.",
         "I will face any challenge to win the approval of my family.",
         "My house's alliance with another noble family must be sustained at all costs.",
         "Nothing is more important that the other members of my family.",
         "I am in love with the heir of a family that my family despises.",
         "My loyalty to my sovereign is unwavering.",
         "The common folk must see me as a hero of the people.",
         "My family, clan, or tribe is the most important thing in my life, even when they are far from me.",
         "An injury to the unspoiled wilderness of my home is an injury to me.",
         "I will bring terrible wrath down on the evildoers who destroyed my homeland.",
         "I am the last of my tribe, and it is up to me to ensure their names enter legend.",
         "I suffer awful visions of a coming disaster and will do anything to prevent it.",
         "It is my duty to provide children to sustain my tribe.",
         "It is my duty to protect my students.",
         "I have an ancient text that holds terrible secrets that must not fall into the wrong hands.",
         "I work to preserve a library, university, scriptorium, or monastery.",
         "My life's work is a series of tomes related to a specific field of lore.",
         "I've been searching my whole life for the answer to a certain question.",
         "I sold my soul for knowledge. I hope to do great deeds and win it back.",
         "I'm loyal to my captain first, everything else second.",
         "The ship is most important--crewmates and captains come and go"
         "I'll always remember my first ship.",
         "In a harbor town, I have a paramour whose eyes nearly stole me from the sea.",
         "I was cheated of my fair share of the profits, and I want to get my due.",
         "Ruthless pirates murdered my captain and crewmates, plundered our ship, and left me to die. Vengeance wi"
         "ll be mine.", "I would lay down my life for the people I served with.",
         "Someone saved my life on the battlefield. To this day, I will never leave a friend behind.",
         "My honor is my life.",
         "I'll never forget the crushing defeat my company suffered or the enemies who dealt it.",
         "Those who fight beside me are those worth dying for.",
         "I fight for those who cannot fight for themselves.",
         "My town or city is my home, and I'll fight to defend it.",
         "I sponsor an orphanage to keep others from enduring what I was forced to endure.",
         "I owe my survival to another urchin who taught me to live on the streets.",
         "I owe a debt I can never repay to the person who took pity on me.",
         "I escaped my life of poverty by robbing an important person, and I'm wanted for it.",
         "No one else is going to have to endure the hardships I've been through."]
bonds = random.sample(bonds, 2)

# Flaws
flaws = ["I judge others harshly, and myself even more severely.",
         "I put too much trust in those who wield power within my temple's hierarchy.",
         "My piety sometimes leads me to blindly trust those that profess faith in my god.",
         "I am inflexible in my thinking.", "I am suspicious of strangers and suspect the worst of them.",
         "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life.",
         "I can't resist a pretty face.",
         "I'm always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.",
         "I'm convinced that no one could ever fool me in the way I fool others.",
         "I'm too greedy for my own good. I can't resist taking a risk if there's money involved.",
         "I can't resist swindling people who are more powerful than me.",
         "I hate to admit it and will hate myself for it, but I'll run and preserve my own hide if the going "
         "gets tough.", "When I see something valuable, I can't think about anything but how to steal it.",
         "When faced with a choice between money and my friends, I usually choose the money.",
         "If there's a plan, I'll forget it. If I don't forget it, I'll ignore it.",
         "I have a 'tell' that reveals when I'm lying.", "I turn tail and run when things go bad.",
         "An innocent person is in prison for a crime that I committed. I'm okay with that.",
         "I'll do anything to win fame and renown.", "I'm a sucker for a pretty face.",
         "A scandal prevents me from ever going home again. That kind of trouble seems to follow me around.",
         "I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.",
         "I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.",
         "Despite my best efforts, I am unreliable to my friends.",
         "The tyrant who rules my land will stop at nothing to see me killed.",
         "I'm convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.",
         "The people who knew me when I was young know my shameful secret, so I can never go home again.",
         "I have a weakness for the vices of the city, especially hard drink.",
         "Secretly, I believe that things would be better if I were a tyrant lording over the land.",
         "I have trouble trusting in my allies.", "I'll do anything to get my hands on something rare or priceless.",
         "I'm quick to assume that someone is trying to cheat me.",
         "No one must ever learn that I once stole money from guild coffers.",
         "I'm never satisfied with what I have--I always want more.", "I would kill to acquire a noble title.",
         "I'm horribly jealous of anyone who outshines my handiwork. Everywhere I go, I'm surrounded by rivals.",
         "Now that I've returned to the world, I enjoy its delights a little too much.",
         "I harbor dark bloodthirsty thoughts that my isolation failed to quell.",
         "I am dogmatic in my thoughts and philosophy.",
         "I let my need to win arguments overshadow friendships and harmony.",
         "I'd risk too much to uncover a lost bit of knowledge.",
         "I like keeping secrets and won't share them with anyone.",
         "I secretly believe that everyone is beneath me.",
         "I hide a truly scandalous secret that could ruin my family forever.",
         "I too often hear veiled insults and threats in every word addressed to me, and I'm quick to anger.",
         "I have an insatiable desire for carnal pleasures.", "In fact, the world does revolve around me.",
         "By my words and actions, I often bring shame to my family.",
         "I am too enamored of ale, wine, and other intoxicants.",
         "There's no room for caution in a life lived to the fullest.",
         "I remember every insult I've received and nurse a silent resentment toward anyone who's ever wronged me.",
         "I am slow to trust members of other races.", "Violence is my answer to almost any challenge.",
         "Don't expect me to save those who can't save themselves. It is nature's way that the strong thrive and "
         "the weak perish.", "I am easily distracted by the promise of information.",
         "Most people scream and run when they see a demon. I stop and take notes on its anatomy.",
         "Unlocking an ancient mystery is worth the price of a civilization.",
         "I overlook obvious solutions in favor of complicated ones.",
         "I speak without really thinking through my words, invariably insulting others.",
         "I can't keep a secret to save my life, or anyone else's.",
         "I follow orders, even if I think they're wrong.", "I'll say anything to avoid having to do extra work.",
         "Once someone questions my courage, I never back down no matter how dangerous the situation.",
         "Once I start drinking, it's hard for me to stop.",
         "I can't help but pocket loose coins and other trinkets I come across.",
         "My pride will probably lead to my destruction.",
         "The monstrous enemy we faced in battle still leaves me quivering with fear.",
         "I have little respect for anyone who is not a proven warrior.",
         "I made a terrible mistake in battle that cost many lives--and I would do anything to keep that mistake "
         "secret.", "My hatred of my enemies is blind and unreasoning.",
         "I obey the law, even if the law causes misery.", "I'd rather eat my armor than admit when I'm wrong.",
         "If I'm outnumbered, I always run away from a fight.",
         "Gold seems like a lot of money to me, and I'll do just about anything for more of it.",
         "I will never fully trust anyone other than myself.",
         "I'd rather kill someone in their sleep than fight fair.",
         "It's not stealing if I need it more than someone else.",
         "People who don't take care of themselves get what they deserve."]
flaws = random.sample(flaws, 2)

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

"""
Printing
"""

# Race, Subrace, Class, Subclass
print(f"Race: \t\t\t{playerRace} \nSubrace:\t\t{playerSubRace}\nClass: \t\t\t{playerClass}")

# Optional Cleric Level 1 Domain
if playerClass == "Cleric":
    print(f"Domain: \t\t{clericDomain}")

# Optional Sorcerer Level 1 Origin
if playerClass == "Sorcerer":
    print(f"Origin: \t\t{sorcerousOrigin}")

# Optional Warlock Level 1 Patron
if playerClass == "Warlock":
    print(f"Patron: \t\t{playerPatron}")
# Player Level

print(f"Player Level:\t{playerLevel}")
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
for x in range(len(bonusPerks)):
    print(bonusPerks[x])

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

# Spellcasting
if cantripsKnown >= 1:
    print(f"Cantrips Known:\t\t{numberOfCantrips}")
for x in range(len(cantrips)):
    print(f"\t{cantrips[x]}")

if numberOfSpells >= 1:
    if preparedSpellcasting is False:
        print(f"Spells Known:\t\t{numberOfSpells}")
        if sorcerousOrigin == "Divine Soul":
            print(f"Origin Spells:\t\t1")
        if playerClass == "Warlock" and playerLevel >= 11:
            print(f"Arcanum Spells:\t\t{len(arcanumSpells)}")

    if preparedSpellcasting is True:
        print(f"Spells Prepared:\t{numberOfSpells}")
        if len(circleSpells) >= 1:
            print(f"Circle Spells:\t\t{len(circleSpells)}")
        if len(domainSpells) >= 1:
            print(f"Domain Spells:\t\t{len(domainSpells)}")
        if len(oathSpells) >= 1:
            print(f"Oath Spells: \t\t{len(oathSpells)}")
        if len(conclaveSpells) >= 1:
            print(f"Conclave Spells:\t{len(conclaveSpells)}")

for x in range(len(spells)):
    print(f"\t{spells[x]}")
if playerClass == "Wizard":
    print(f"Spells in Spellbook:\t{len(spellsKnown)}")
    for x in range(len(spellsKnown)):
        print(f"\t{spellsKnown[x]}")



# Equipment
print(f"\nEquipment:")
for x in range(len(equipment)):
    print(equipment[x])

# Characteristics
print(f"\nCharacteristics:")
print("Personality Traits:")
for x in range(len(personalityTraits)):
    print(personalityTraits[x])
print("Ideals:")
for x in range(len(ideals)):
    print(ideals[x])
print("Bonds:")
for x in range(len(bonds)):
    print(bonds[x])
print("Flaws:")
for x in range(len(flaws)):
    print(flaws[x])
