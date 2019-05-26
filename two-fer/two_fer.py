def two_fer(name=None):
    if name is not None:
        string = "One for {}, one for me.".format(name)
    else:
        string = "One for you, one for me."
    return string
    pass
