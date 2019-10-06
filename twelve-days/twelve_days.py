def recite(start_verse, end_verse):
    giftList = ["partridge in a pear tree",
            "turtle doves",
            "french hens",
            "calling birds",
            "gold rings",
            "geese a laying",
            "swans a swimming",
            "maids a milking",
            "ladies dancing",
            "lords of leaping",
            "pipers piping",
            "drummers drumming"]

    for day in range(start_verse,end_verse+1):
        if day == 1:
            verse = "On the " + str(day) + "st"
        elif day == 2:
            verse = "On the " + str(day) + "nd"
        else:
            verse = "On the " + str(day) + "th"

    verse = verse + " day of Christmas my true love sent to me"
    
    for giftNumber in range(day-1,-1,-1): #Looping through the list of gifts, in reverse order
        if giftNumber==0:
            if day==1:
                verse += " a " + giftList[giftNumber] + "."
            else:
                verse = verse[:-1] # remove the last comma
                verse += " and a " + giftList[giftNumber] + "."
        else:
            verse += " " + str(giftNumber+1) + " " + giftList[giftNumber] + ","
    
    return verse_list