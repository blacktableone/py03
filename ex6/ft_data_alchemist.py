#!/usr/bin/env python3

import random


print("=== Game Data Alchemist ===")

players = [
    "Alice", "bob", "Charlie", "dylan", "Emma",
    "Gregory", "john", "kevin", "Liam"
]

print(f"Initial list of players: {players}")

capitalized_players = [name.capitalize() for name in players]
print(f"New list with all names capitalized: {capitalized_players}")

capitalized_only = [name for name in players if name[0].isupper()]
print(f"New list of capitalized names only: {capitalized_only}")

scores = {name: random.randint(1, 1000) for name in capitalized_players}
print(f"Score dict: {scores}")

average = round(sum(scores.values()) / len(scores), 2)
print(f"Score average is {average}")

high_scores = {
    name: score for name, score in scores.items() if score > average
}
print(f"High scores: {high_scores}")
