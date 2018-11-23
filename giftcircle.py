#!/usr/bin/python
import random

'''
Gift exchange randomizer in Python.
Step through a list of people and, for each member of that list,
select someone else to be a recipient of their gift. That recipient:

    A) Must not be themselves (no self-gifting)
    B) Must not already have been assigned as a recipient

Due to randomization, we can't prevent the possibility that 7/8 of people
will all give to each other, leaving the 8th to give to themselves. Therefore
we keep running the function until we get full distribution.
'''


def give():
    str = ''

    givers = ['Leslie', 'Jamie', 'Avis', 'Jim', 'Amy', 'Scot', 'Mike', 'Miles', 'Buford', 'Momo', ]
    recipients = givers.copy()  # Make a copy

    for idx, giver in enumerate(givers):

        # Grab random person from the recipients
        recipient = random.choice(recipients)

        # Make sure we haven't either randomly chosen the same recipient and giver OR
        # ended up with only one un-gifted person in the list.
        if recipient == giver:
            return False
        else:
            # Remove this recipient from the pool and build the results string
            recipients.remove(recipient)
            str = str + f"{idx+1}: {giver} gives to {recipient}\n"
    return str


# Keep trying until we get through the set with no failures
results = give()
while not results:
    results = give()

print(results)
