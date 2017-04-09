import edu.cmu.ri.createlab.terk.robot.finch.Finch as Finch

finch = Finch()
finch.setLED(255,0,0)
print "sup"
while True:
  if finch.isBeakUp():
    finch.saySomething("I'm going to ACE my math test!!!!")
    break
finch.quit()