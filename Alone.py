def turn_right():
    turn_left()
    turn_left()
    turn_left()

def reihe():
    while front_is_clear():
        move()


for i in range(5):
    #Hinweg
    reihe()
    turn_left()
    if front_is_clear():
        move()
        turn_left()
    
    #Rückweg
    reihe()
    turn_right()
    if front_is_clear():
        move()
        turn_right()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
from library import *

for i in range(0,3):
    move()

turn_left()