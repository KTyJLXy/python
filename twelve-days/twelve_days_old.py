numbers = {
    1: ["first", "and"],
    2: ["second", "two"],
    3: ["third", "three"],
    4: ["fourth", "four"],
    5: ["fifth", "five"],
    6: ["sixth", "six"],
    7: ["seventh", "seven"],
    8: ["eighth", "eight"],
    9: ["ninth", "nine"],
    10: ["tenth", "ten"],
    11: ["eleventh", "eleven"],
    12: ["twelfth", "twelve"]
}

gift_list = [
    "Drummers Drumming",
    "Pipers Piping",
    "Lords-a-Leaping",
    "Ladies Dancing",
    "Maids-a-Milking",
    "Swans-a-Swimming",
    "Geese-a-Laying",
    "Gold Rings",
    "Calling Birds",
    "French Hens",
    "Turtle Doves",
    "a Partridge in a Pear Tree"
]

def recite(start_verse, end_verse):
    return [recite_verse(verse) for verse in range(start_verse, end_verse + 1)]

def recite_verse(verse):
    return f"On the {numbers[verse][0]} day of Christmas my true love gave to me:" + gifts(verse)

def gifts(verse):
    gifts_list = []
    rev_list = gift_list
    rev_list.reverse()
    for gift in range(0, verse):
        if verse == 1:
            return f" " + rev_list[0] + "."
        else:
            gifts_list += [f"{numbers[gift + 1][1]} " + rev_list[gift]]
    gifts_list.reverse()
    return ", ".join(gifts_list) + "."
    
