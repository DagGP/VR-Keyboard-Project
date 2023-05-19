import random

def get_letter(a=False, b=False):
    if (not a or not b):
        return None
    alphabet = [
        ['e', 'a', 't', 'y', 'b', 'q'], 
        ['r', 'i', 'l', 'd', 'y','j'], 
        ['o', 's', 'n', 'm', 'k',None], 
        ['c', 'u', 'p', 'h', 'x',None], 
        ['g', 'f', 'w', 'v', 'z',None], 
        ['backspace','enter','capsLock','enable','space',None]
    ]
    a = int(a)
    b = int(b)

    if a < 0 or a > len(alphabet) or b < 0 or b > len(alphabet):
        return None  # return None if the input values are not valid
    
    try:
        return alphabet[a][b]
    except IndexError:
        return None  # return None if the index is out of range



