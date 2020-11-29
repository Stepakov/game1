from game_api import *
from color_api import *

set_heap()
player = 1


while True:
    out_color( 'yellow', 'This is the heap: ', get_heap() )
    out_color( 'blue', "Player {} can remove stones".format( player ) )
    pos = int( input( "Remove from position: " ) )
    qua = int( input( "Remove number of stones: " ) )
    remove_from_heap( pos - 1, qua )
    if is_gameover():
        break;
    player = 1 if player == 2 else 2

out_color( 'red', "Player {} won.".format( player ) )