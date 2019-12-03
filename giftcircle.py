#!/usr/bin/python
import random

"""
Gift exchange randomizer in Python.
Step through a list of people and, for each member of that list,
select someone else to be a recipient of their gift. Randomization
can result in self-giving -- keep running until we get a full distribution.
"""

givers = [
    "Jamie",
    "John",
    "Avis",
    "Jim",
    "Amy",
    "Scot",
    "Miles",
    "Scarlett",
    "Tanner",
]

recipients = givers.copy()
report = []


def give():
    """
    Ensure no giver is identical to the recipient (no self-giving).
    Reset report and reshuffle recipients on each attempt.
    """

    random.shuffle(recipients)
    report = []

    for giver, recipient in zip(givers, recipients):
        if giver == recipient:
            return False
        else:
            line = f"{giver} -> {recipient}"
            report.append(line)

    return report


results = give()
while not results:
    results = give()

for elem in results:
    print(elem)
