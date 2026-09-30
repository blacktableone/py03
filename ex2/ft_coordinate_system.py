#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z':")

        values = coordinates.split(",")
        if len(values) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(values[0])
        except ValueError as error:
            print(f"Error on parameter '{values[0]}': {error}")
            continue

        try:
            y = float(values[1])
        except ValueError as error:
            print(f"Error on parameter '{values[0]}': {error}")
            continue

        try:
            z = float(values[2])
        except ValueError as error:
            print(f"Error on parameter '{values[0]}': {error}")
            continue

        return (x, y, z)


print("=== Game Coordinate System ===")

print("\nGet a first set of coordinates")

first = get_player_pos()
print(f"Got a first tuple: {first}")
print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
distance_center = math.sqrt(
    first[0] ** 2
    + first[1] ** 2
    + first[2] ** 2
)
print(f"Distance to center: {distance_center:.4f}")

print("\nGet a second set of coordinates")

second = get_player_pos()
distance = math.sqrt(
    (first[0] - second[0]) ** 2
    + (first[1] - second[1]) ** 2
    + (first[2] - second[2]) ** 2
)
print(f"Distance between the 2 sets of coordinates: {distance:.4f}")
