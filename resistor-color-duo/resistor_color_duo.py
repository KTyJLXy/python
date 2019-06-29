def value(colors):
    ClrLst = colors_rst()
    resist = ''
    for color in colors:
        if color in ClrLst:
            resist += str(ClrLst.index(color))
    return int(resist)

def color_code(color):
    ClrLst = colors()
    return ClrLst.index(color)

def colors_rst():
    return [
            'black',
            'brown',
            'red',
            'orange',
            'yellow',
            'green',
            'blue',
            'violet',
            'grey',
            'white'
           ]