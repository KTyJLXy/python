"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.

YACHT = lambda x: 50 if len(set(x))==1 else 0
ONES = lambda x: sum(i for i in x if i==1)
TWOS = lambda x: sum(i for i in x if i==2)
THREES = lambda x: sum(i for i in x if i==3)
FOURS = lambda x: sum(i for i in x if i==4)
FIVES = lambda x: sum(i for i in x if i==5)
SIXES = lambda x: sum(i for i in x if i==6)

FULL_HOUSE = lambda x: sum(x) if len(set(x))==2 and any(x.count(i)==3 for i in set(x)) else 0

FOUR_OF_A_KIND = lambda x : sum(4*i for i in set(x) if x.count(i)>=4) 

LITTLE_STRAIGHT = lambda x: 30 if set(x)==set([1,2,3,4,5]) else 0

BIG_STRAIGHT = lambda x: 30 if set(x)==set([2,3,4,5,6]) else 0

CHOICE = lambda x: sum(x)

def score(dice, category):
    return category(dice)