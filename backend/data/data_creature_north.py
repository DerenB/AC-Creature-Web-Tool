import sys
import os

from models.Creature import Creature

# File Path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

data_creature_north = [
    Creature(id=1, name="Abalone", price=2000, size="Medium", speed="Moderate consistent movement", month_start=6, month_end=1, time_start=1600, time_end=900),
    Creature(id=2, name="Acorn Barnacle", price=600, size="Tiny", speed="Stationary", month_start=1, month_end=12, time_start=0, time_end=2359),
    Creature(id=3, name="Chambered Nautilus", price=1800, size="Medium", speed="Slow", month_start=3, month_end=6, time_start=1600, time_end=900),
    Creature(id=4, name="Chambered Nautilus", price=1800, size="Medium", speed="Slow", month_start=9, month_end=11, time_start=1600, time_end=900),
    Creature(id=5, name="Dungeness Crab", price=1900, size="Medium", speed="Moderate consistent movement", month_start=11, month_end=5, time_start=0, time_end=2359),
    Creature(id=6, name="Firefly Squid", price=1400, size="Tiny", speed="Slow", month_start=3, month_end=6, time_start=2100, time_end=400),
    Creature(id=7, name="Flatworm", price=700, size="Tiny", speed="Slow short movement", month_start=8, month_end=9, time_start=1600, time_end=900),
    Creature(id=8, name="Gazami Crab", price=2200, size="Medium", speed="Moderate long lunges", month_start=6, month_end=11, time_start=0, time_end=2359),
    Creature(id=9, name="Giant Isopod", price=12000, size="Medium", speed="Quick long lunges", month_start=7, month_end=10, time_start=900, time_end=1600),
    Creature(id=10, name="Giant Isopod", price=12000, size="Medium", speed="Quick long lunges", month_start=7, month_end=10, time_start=2100, time_end=400),
    Creature(id=11, name="Gigas Giant Clam", price=15000, size="Huge", speed="Quick long lunges", month_start=5, month_end=9, time_start=0, time_end=2359),
    Creature(id=12, name="Horseshoe Crab", price=2500, size="Medium", speed="Quick short lunges", month_start=7, month_end=9, time_start=2100, time_end=400),
    Creature(id=13, name="Lobster", price=4500, size="Large", speed="Quick", month_start=12, month_end=1, time_start=0, time_end=2359),
    Creature(id=14, name="Lobster", price=4500, size="Large", speed="Quick", month_start=4, month_end=6, time_start=0, time_end=2359),
    Creature(id=15, name="Mantis Shrimp", price=2500, size="Small", speed="Quick short lunges", month_start=1, month_end=12, time_start=1600, time_end=900),
    Creature(id=16, name="Moon Jellyfish", price=600, size="Small", speed="Slow consistent movement", month_start=7, month_end=9, time_start=0, time_end=2359),
    Creature(id=17, name="Mussel", price=1500, size="Small", speed="Slow consistent movement", month_start=6, month_end=12, time_start=0, time_end=2359),
    Creature(id=18, name="Octopus", price=1200, size="Medium", speed="Moderate long lunges", month_start=1, month_end=12, time_start=0, time_end=2359),
    Creature(id=19, name="Oyster", price=1100, size="Small", speed="Moderate short lunges", month_start=9, month_end=2, time_start=0, time_end=2359),
    Creature(id=20, name="Pearl Oyster", price=2800, size="Medium", speed="Moderate long lunges", month_start=1, month_end=12, time_start=0, time_end=2359),
    Creature(id=21, name="Red King Crab", price=8000, size="Large", speed="Quick", month_start=11, month_end=3, time_start=0, time_end=2359),
    Creature(id=22, name="Scallop", price=1200, size="Medium", speed="Slow long lunges", month_start=1, month_end=12, time_start=0, time_end=2359),
    Creature(id=23, name="Sea Anemone", price=500, size="Large", speed="Stationary", month_start=1, month_end=12, time_start=0, time_end=2359),
    Creature(id=24, name="Sea Cucumber", price=500, size="Medium", speed="Slow consistent movement", month_start=11, month_end=4, time_start=0, time_end=2359),
    Creature(id=25, name="Sea Grapes", price=900, size="Small", speed="Stationary", month_start=6, month_end=9, time_start=0, time_end=2359),
    Creature(id=26, name="Sea Pig", price=10000, size="Small", speed="Quick long lunges", month_start=11, month_end=2, time_start=1600, time_end=900),
    Creature(id=27, name="Sea Pineapple", price=1500, size="Small", speed="Slow long lunges", month_start=4, month_end=8, time_start=0, time_end=2359),
    Creature(id=28, name="Sea Slug", price=600, size="Tiny", speed="Slow consistent movement", month_start=1, month_end=12, time_start=0, time_end=2359),
    Creature(id=29, name="Sea Star", price=500, size="Small", speed="Slow short lunges", month_start=1, month_end=12, time_start=0, time_end=2359),
    Creature(id=30, name="Sea Urchin", price=1700, size="Small", speed="Slow consistent movement", month_start=5, month_end=9, time_start=0, time_end=2359),
    Creature(id=31, name="Seaweed", price=600, size="Large", speed="Stationary", month_start=10, month_end=7, time_start=0, time_end=2359),
    Creature(id=32, name="Slate Pencil Urchin", price=2000, size="Medium", speed="Moderate consistent movement", month_start=5, month_end=9, time_start=1600, time_end=900),
    Creature(id=33, name="Snow Crab", price=6000, size="Large", speed="Quick short lunges", month_start=11, month_end=4, time_start=0, time_end=2359),
    Creature(id=34, name="Spider Crab", price=12000, size="Huge", speed="Quick", month_start=3, month_end=4, time_start=0, time_end=2359),
    Creature(id=35, name="Spiny Lobster", price=5000, size="Large", speed="Fast", month_start=10, month_end=12, time_start=2100, time_end=400),
    Creature(id=36, name="Spotted Garden Eel", price=1100, size="Small", speed="Slow consistent movement", month_start=5, month_end=10, time_start=400, time_end=2100),
    Creature(id=37, name="Sweet Shrimp", price=1400, size="Small", speed="Slow", month_start=9, month_end=2, time_start=1600, time_end=900),
    Creature(id=38, name="Tiger Prawn", price=3000, size="Small", speed="Moderate consistent movement", month_start=6, month_end=9, time_start=1600, time_end=900),
    Creature(id=39, name="Turban Shell", price=1000, size="Small", speed="Slow", month_start=3, month_end=5, time_start=0, time_end=2359),
    Creature(id=40, name="Turban Shell", price=1000, size="Small", speed="Slow", month_start=9, month_end=12, time_start=0, time_end=2359),
    Creature(id=41, name="Umbrella Octopus", price=6000, size="Small", speed="Quick long lunges", month_start=3, month_end=5, time_start=0, time_end=2359),
    Creature(id=42, name="Umbrella Octopus", price=6000, size="Small", speed="Quick long lunges", month_start=9, month_end=11, time_start=0, time_end=2359),
    Creature(id=43, name="Vampire Squid", price=10000, size="Medium", speed="Moderate long lunges", month_start=5, month_end=8, time_start=1600, time_end=900),
    Creature(id=44, name="Venus' Flower Basket", price=5000, size="Medium", speed="Quick long lunges", month_start=10, month_end=2, time_start=0, time_end=2359),
    Creature(id=45, name="Whelk", price=1000, size="Small", speed="Slow consistent movement", month_start=1, month_end=12, time_start=0, time_end=2359)
]