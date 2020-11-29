from random import randint

MAX_ROW_IN_HEAP = 3
MAX_STONES_IN_ROW = 20
_heap = []

def set_heap():
    global _heap
    _heap = []
    for _ in range( MAX_ROW_IN_HEAP ):
        _heap.append( randint( 1, MAX_STONES_IN_ROW ) )

def get_heap():
    return _heap

def remove_from_heap( position, quantity ):
    if 0 <= position <= MAX_STONES_IN_ROW:
        _heap[ position ] -= quantity
        if _heap[ position ] < 0: _heap[ position ] = 0

def is_gameover():
    return not any( _heap )