#!/usr/bin/env python3

import sys

print("=== Inventory System Analysis ===")

inventory: dict[str, int] = {}

# get the dictionary
i = 1
while i < len(sys.argv):
    parameter = sys.argv[i]  # get sword:1
    parts = parameter.split(":")  # get list like['sword', '1']

    # check valid paraments has
    if len(parts) != 2:
        print(f"Error - invalid parameter '{parameter}'")
    else:
        item = parts[0]

        # check redundant parament
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")

        # check value is int
        else:
            try:
                quantity = int(parts[1])
                inventory[item] = quantity
            except ValueError as error:
                print(f"Quantity error for '{item}': {error}")
    i += 1


# print the dictionary
print(f"Got inventory: {inventory}")

# print items
items = list(inventory.keys())
print(f"Item list: {items}")

# prints sum of items
total_quantity = sum(inventory.values())
print(f"Total quantity of the {len(items)} items: {total_quantity}")

# print every item's %
if total_quantity > 0:
    i = 0
    while i < len(items):
        item = items[i]
        quantity = inventory[item]
        percentage = round(quantity / total_quantity * 100, 1)
        print(f"Item {item} represents {percentage}%")
        i += 1

# Report the most and least abundant items
if len(items) > 0:
    most_item = items[0]
    least_item = items[0]

    i = 1
    while i < len(items):
        item = items[i]

        if inventory[item] > inventory[most_item]:
            most_item = item

        if inventory[item] < inventory[least_item]:
            least_item = item

        i += 1

    print(
        f"Item most abundant: {most_item} "
        f"with quantity {inventory[most_item]}"
    )

    print(
        f"Item least abundant: {least_item}"
        f"with quantity {inventory[least_item]}"
    )

# add a new item
inventory.update({"magic_item": 1})

# print updated inventory
print(f"Updated inventory: {inventory}")
