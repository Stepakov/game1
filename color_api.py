
color_list = {
    'red': "\033[31m",
    'yellow': "\033[33m",
    'blue': "\033[34m"
}

def out_color( color, *args ):
    res = ''
    for text in args:
        res += str( text ) + ' '
    print( "{}{}\033[0m".format( color_list[ color ], res ) )