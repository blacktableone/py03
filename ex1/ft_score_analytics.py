#!/usr/bin/env python3
import sys

print("=== Player Score Analytics ===")

scores = []

i = 1

while i < len(sys.argv):
    try:
        score = int(sys.argv[i])
        scores.append(score)
    except ValueError:
        print(f"Invalid parameter: '{sys.argv[i]}'")
    i += 1

if len(scores) == 0:
    print(
        "No scores provided. Usage: "
        "python3 ft_score_analytics.py <score1> <score2> ..."
    )

else:
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")

    total = sum(scores)
    average = total / len(scores)
    h_score = max(scores)
    l_score = min(scores)
    r_score = h_score - l_score

    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {h_score}")
    print(f"Low score: {l_score}")
    print(f"Score range: {r_score}")
