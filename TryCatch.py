from finch import Finch
from time import sleep
from random import randint

def Quit(myFinch):
    myFinch.close()

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

def move(finch, left, right, duration, ledList): #moves by activating left and right motors
  """Basic move function"""
  finch.led(ledList[0], ledList[1], ledList[2]) #changes color
  finch.wheels(left,right) #moves
  sleep(float(duration)/1000.00)
  finch.wheels(0,0)
  
def danceFinch(myFinch,repetitions):
    for i in range(repetitions):
        move(myFinch,1,1,1000,[255,0,0])
        move(myFinch,0,1,1000,[0,255,0])
        move(myFinch,1,0,1000,[0,0,255])
        move(myFinch,-1,-1,500,[255,0,255])


def main():
    myFinch = Connect()
    if myFinch == 0:
        print "Connection to Finch could not be established. THE END"
        return
    #repetitions = randint(1,10)
    repetitions = 2
    danceFinch(myFinch,repetitions)
    move(myFinch,1,0,10000,[255,0,0])
    Quit(myFinch)

main()


