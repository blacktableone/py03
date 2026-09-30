#!/usr/bin/env python3

import random
from typing import Generator


players = ["alice", "bob", "charlie", "dylan"]
actions = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
    "use",
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield name, action


def consume_event(
    events: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield event


print("=== Game Data Stream Processor ===")

event_generator = gen_event()

i = 0
while i < 1000:
    event = next(event_generator)
    print(f"Event {i}: Player {event[0]} did action {event[1]}")
    i += 1

event_list: list[tuple[str, str]] = []

i = 0
while i < 10:
    event_list.append(next(event_generator))
    i += 1

print(f"Built list of 10 events: {event_list}")

for event in consume_event(event_list):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {event_list}")
