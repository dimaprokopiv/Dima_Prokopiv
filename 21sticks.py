# 21 Sticks
# The Game:
# In this game, there are 21 sticks lying in a pile. 
# Players take turns taking 1, 2, or 3 sticks. The last person to take a stick wins.

def make_move(sticks):
    amount = sticks%4
    return amount