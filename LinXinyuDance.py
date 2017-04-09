#Finch dancing project // Jeffrey Jin, Xinyu Lin

from finch import Finch             #imports the finch module
from time import sleep              #imports the sleep function from the time module

def Connect():                      #a function that connects the finch to the python methods
    for i in range (2):             #loop of two
        try:                        #first attempt
            newFinch=Finch()        #sets a variable equal to connection
            return newFinch
        except:                              
            if i==0:  
                print "Failed to connect to Finch on the first try"    #prints a statement that the finch failed to connect the first time
                Quit(newFinch)
    newFinch=0                      #resets newFinch variable to 0
    print "Failed to connect to Finch on the second try"               #prints a statement that the finch failed to connect the second time
    return newFinch                 #returns the value of newFinch

def Quit(myFinch):                  #a function that tells the finch to quit
    myFinch.close()                 #closes the connection to the finch

def drawcircle(myfinch,repetition): #function to draw a circle (uses the value of the connect function and number of repetitions as a parameter)
    for i in range(repetition):     #repeats the code "repetition" amount of times
        myfinch.led(255,255,0)      #changes the color 
        myfinch.wheels(1,0)         #moves the finch forward
        sleep(.5)                   #the duration of the previous method was .5 seconds
        myfinch.led(255,0,0)        
        myfinch.wheels(1,0)         #turns the finch left
        sleep(.5) 

def drawreversecircle(myfinch,repetition):   #function to move the circle in reverse (uses the value of the connect function and number of repetitions as a parameter)
    for i in range(repetition):     #repeats the code "repetition" amount of times
        myfinch.led(255,255,0)      #changes the color
        myfinch.wheels(0,1)         #finch turns to the right
        sleep(.5)                   #the duration of the previous method was .5 seconds
        myfinch.led(255,0,255)
        myfinch.wheels(0,1)
        sleep(.5)

def drawtriangle(myfinch,repetition):        #function to draw a triangle (uses the value of the connect function and number of repetitions as a parameter)
    for i in range(repetition):     #repeats the code "repetition" amount of times
        myfinch.led(0,0,255)        #changes the color
        myfinch.led(0,255,0)
        sleep(1)                    #the duration of the previous method was 1 seconds
        myfinch.wheels(1,1)         #the finch movies forward
        sleep(1)                   
        myfinch.led(255,0,255) 
        myfinch.wheels(0.6666666666666666666,0) #the finch makes a 60 degree turn
        sleep(1)                    
 
def drawsquare(myfinch,repetition):          #function to draw a square (uses the value of the connect function and number of repetitions as a parameter)
    for i in range(repetition):    #repeats the code "repetition" amount of times     
        myfinch.led(255,255,0)     #changes color
        myfinch.wheels(1,1)        #moves the finch forward
        sleep(1)                   #the duration of the previous method was 1 seconds
        myfinch.led(255,0,0)
        myfinch.wheels(.60,0)       #the finch makes a 90 degree turn
        myfinch.buzzer(1,600)      #the finch produces a buzzing sound
        sleep(1)      

def forwardandback(myfinch,repetition):     #function to make the finch go forward and back (uses the value of the connect function and number of repetitions as a parameter)
    for i in range(repetition):    #repeats the code "repetition" amount of times
        myfinch.led(255,0,255)     #changes the color
        myfinch.wheels(1,1)        #finch moves forward
        sleep(1)                   #the duration of the previous method was 1 seconds
        myfinch.led(255,255,0)
        myfinch.wheels(-1,-1)      #the finch moves in reverse
        sleep(1)
        myfinch.led(255,0,0)       #color of the finch changes  
        myfinch.wheels(1,1)      
        sleep(1)                   #the duration of the previous method was 1 seconds
        myfinch.led(0,0,255)
        myfinch.wheels(2,0)        #the finch goes in reverse
        sleep(1)        
        myfinch.led(255,0,255)
        myfinch.wheels(1,1)        #wheels move forward
        sleep(1)                   #the duration of the previous method was 1 seconds

def main():                        #the function that controls all the other functions
    finch1=Connect()               #connects the finch
    forwardandback(finch1,1)       #calls the forwardandback function with a finch parameter and repetition parameter
    drawsquare(finch1,8)           #calls the drawsquare function with a finch parameter and repetition parameter
    drawcircle(finch1,5)           #calls the drawcircle function with a finch parameter and repetition parameter
    drawreversecircle(finch1,7)    #calls the drawreversecircle function with a finch parameter and repetition parameter
    forwardandback(finch1,1)       #calls the forwardandback function with a finch parameter and repetition parameter
    drawtriangle(finch1,8)         #calls the drawtriangle function with a finch parameter and repetition parameter
    forwardandback(finch1,1)       #calls the forwardandback function with a finch parameter and repetition parameter
    Quit(finch1)                   #ends the connection to the finch

main()                             #calls the main function
