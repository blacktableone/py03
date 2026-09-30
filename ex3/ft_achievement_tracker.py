#!/usr/bin/env python3

import random

ACHIEVEMENTS = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "Hidden Path Finder",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
]


def gen_player_achievements() -> set[str]:
    number = random.randint(3, 9)
    achievements: set[str] = set()

    while len(achievements) < number:
        achievement = random.choice(ACHIEVEMENTS)
        achievements.add(achievement)

    return achievements


print("=== Achievement Tracker System ===\n")

players = {
    "Alice": gen_player_achievements(),
    "Bob": gen_player_achievements(),
    "Charlie": gen_player_achievements(),
    "Dylan": gen_player_achievements(),
}

# print the dictionary
for name, achievements in players.items():
    print(f"Player {name}: {achievements}")

# get distinct achievements
all_achievements: set[str] = set()
for achievements in players.values():
    all_achievements = all_achievements.union(achievements)
print(f"\nAll distinct achievements: {all_achievements}\n")

# get common achievements
common_achievements = None
for achievements in players.values():
    if common_achievements is None:
        common_achievements = achievements
    else:
        common_achievements = common_achievements.intersection(achievements)
print(f"Common achievements: {common_achievements}\n")

# for each player, spot the achievements no one else has
for name, achievements in players.items():
    other_achievements: set[str] = set()
    for other_name, other_player_achievements in players.items():
        if name != other_name:
            other_achievements = (
                other_achievements.union(other_player_achievements)
            )
    only_this_player = achievements.union(other_achievements)
    print(f"Only {name} has: {only_this_player}")
print()

# For each player, list the missing achievements to have them all
for name, achievements in players.items():
    miss = all_achievements.difference(achievements)
    print(f"{name} is missing {miss}")
