import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise   
    if int(math.sqrt(sq))**2 == sq:
        sqnext = math.sqrt(sq) + 1
        return sqnext * sqnext
    else:
        return -1
