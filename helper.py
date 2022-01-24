from os import pipe
import random

def makeSeatData():
    seatPos = open("SeatPos.txt", "a+")
    seatPos.truncate(0)
    n = 10
    for i in range(10):
        for l in range(5):
            seatPos.write(str(n))
            seatPos.write("\n")
            n -= 1
        for l in range(5):
            n += 1
            seatPos.write(str(n))
            seatPos.write("\n")
        # seatPos.write("\n")
    seatPos.close()

def makeRowAccelData():
    PullForce = open("PullForce.txt", "a+")
    PullForce.truncate(0)
    for i in range(10):
        n = 0
        PullForce.write(str(n))
        n = 1
        for l in range(10):
            PullForce.write(str(n))
            PullForce.write("\n")
            n += n**(1.1)
            n = round(n, 3)
        # PullForce.write("\n")
    PullForce.close()

def makeSpeedData():
    Speed = open("Speed.txt", "a+")
    Speed.truncate(0)
    for i in range(100):
        Speed.write(str(random.randint(8,11)))
        Speed.write("\n")
    Speed.close()

makeSeatData()
makeRowAccelData()
makeSpeedData()