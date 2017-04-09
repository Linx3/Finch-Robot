# A simple Finch dance in Python
from finch import Finch
from time import sleep
from random import randint

def Connect():
    newFinch=Finch()
    return newFinch

def Quit(myFinch):
    myFinch.close

def dancingfinch(snakyFinch, repetition):
    for i in range (repetition):
        snakyFinch.wheels(1,1)

def main():
    afinch=Connect()
    random=randint(1,10)
    print random 
    dancingfinch(afinch,random)
    Quit(afinch)
main()

