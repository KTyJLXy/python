import datetime

def add(moment):
    gigasecond = datetime.timedelta(seconds=1000000000)
    gigasecondday = moment + gigasecond
    return gigasecondday