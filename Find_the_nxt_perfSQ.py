"""
You might know some pretty large perfect squares. But what about the NEXT one?
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
 Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.
"""


import math 

def find_next_square(sq):
    # step 1: Take the square root of thte given number 
    sqrt_sq = math.sqrt(sq)

    # step 2: Round Up the square root to the nearest int 
    nxt_potential_sq = math.ceil(sqrt_sq)

    # step 3: Square the rounded-up square root to check if it's a perf sqr
    next_square = nxt_potential_sq **2 

    # step 4: Check if it's a perf sqr and return the result 
    if next_square == sq:
    # increment to the nxt potential square and try again
        nxt_potential_sq += 1
        return nxt_potential_sq **2
    else:
        return -1 

result = find_next_square(16)
print(result)