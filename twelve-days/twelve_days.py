import re

numbers = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
}

gifts = [
    "twelve Drummers Drumming",
    "eleven Pipers Piping",
    "ten Lords-a-Leaping",
    "nine Ladies Dancing",
    "eight Maids-a-Milking",
    "seven Swans-a-Swimming",
    "six Geese-a-Laying",
    "five Gold Rings",
    "four Calling Birds",
    "three French Hens",
    "two Turtle Doves",
    "and a Partridge in a Pear Tree"
]

def recite(start_verse, end_verse):
    return [recite_verse(verse) for verse in range(start_verse, end_verse + 1)]

def recite_verse(verse):
    return f"On the {numbers[verse]} day of Christmas my true love gave to me: " + re.sub("^and ", "", ", ".join(gifts[12 - verse:12])) + "."
    
