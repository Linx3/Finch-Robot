from finch import Finch
from time import sleep

def Connect():
    for i in range (2):
        try:
            newFinch = Finch()
            return newFinch
        except:
            if i == 0:
                print "Failed to connect to Finch on the first try"
                Quit(newFinch)
    newFinch = 0
    print "Failed to connect to Finch on the second try"
    return newFinch

def Quit(myFinch):
    myFinch.close()

def dancing(myFinch, repetition): 
    for i in range (repetition):
        myFinch.wheels(1,1)
        myFinch.led(0,0,255)
        sleep(1)
        myFinch.wheels(0,0.5)
        sleep(1)
     
finch1=Connect()
dancing(finch1, 3)
Quit(finch1)


