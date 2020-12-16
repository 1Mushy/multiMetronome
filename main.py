#This is used to generate the tone
import pysine

#Used for delay
import time

#Used for testing
import datetime

#Probability
from random import seed
from random import randint
seed(1)

def acceldecel():
    #Starting tempo input
    while True:
        try:
            startTempo = int(input('Starting tempo: '))
            break
        except ValueError:
            print('Please input a number')

    #Ending tempo input
    while True:
        try:
            endTempo = int(input('Ending tempo: '))
            break
        except ValueError:
            print('Please input a number')

    #Rate input
    while True:
        try:
            rate = int(input('How often would you like the tempo to change? '))
            break
        except ValueError:
            print('Please input a number')

    #Figuring out how many times to loop the code
    loopAmount = (endTempo - startTempo) * rate
    loopAmount = abs(loopAmount)

    #Looping the metronome
    while loopAmount >= 0:

        #Generating the tone
        pysine.sine(frequency=440.0, duration=0.1)

        #For testing
        print(str(datetime.datetime.now()) + "      " + str((60/startTempo)))

        #The delay inbetween beeps
        time.sleep((60/startTempo)-0.1)

        #Checking to see if the startTempo should go up or down
        if endTempo > startTempo:
            startTempo = startTempo + (rate)
        
        if startTempo > endTempo:
            startTempo = startTempo - (rate)

        #Reducing the loop
        loopAmount -= 1
    

    #Keeps playing the slowed/sped up tempo
    while True:
        pysine.sine(frequency=440.0, duration=0.1)
        time.sleep((60/startTempo)-0.1)

def steady():
    while True:
        try:
            tempo = int(input('What tempo would you like the metronome to play at? '))
            break
        except ValueError:
            print('Please input an integer')

    while True:
        pysine.sine(frequency=440.0, duration=0.1)
        time.sleep((60/tempo)-0.1)
    
def randomBeat():
    while True:
        try:
            tempo = int(input('What would you like the tempo to be? '))
            break
        except ValueError:
            print('Please input a number')

    while True:
        try:
            percentageChance = int(input('What should be the percentage chance of skipping a beat. Please use only a number? '))
            break
        except ValueError:
            print('Please input a number')

    #percentageChance = percentageChance/100
    

    while True:
        willBeatPlay = randint(1, int(100/percentageChance))
        print(willBeatPlay)
        print(int(100/percentageChance))
        if willBeatPlay == 1:
            time.sleep(60/tempo)
        else:
            pysine.sine(frequency=440.0, duration=0.1)
            time.sleep((60/tempo)-0.1)

def beatPhasing():
    while True:
        try:
            tempo = int(input('What would you like the tempo to be? '))
            break
        except ValueError:
            print('Please input a number')


    while True:
        try:
            phase = int(input('How many beats would you like to disappear? '))
            break
        except ValueError:
            print('Please input a number')

    while True:
        try:
            beatAmount = int(input('How many beats before the pause? '))
            break
        except ValueError:
            print('Please input a number')

    phaseLoop = phase
    beatLoop = beatAmount

    while True:

        while beatLoop > 0:
            pysine.sine(frequency=440.0, duration=0.1)
            time.sleep((60/tempo)-0.1)
            beatLoop -= 1

        beatLoop = beatAmount

        while phaseLoop > 0:
            # print('waiting')
            time.sleep(60/tempo)
            phaseLoop -= 1
        
        phaseLoop = phase

def Agogic():
    while True:
        try:
            timeSig = int(input('How many beats are in a measure? '))
            break
        except ValueError:
            print('Please input a number')

    while True:
        try:
            tempo = int(input('What would you like the tempo to be? '))
            break
        except ValueError:
            print('Please input a number')

    percentageDelay = 2
    loop = timeSig - 1

    while True:
        
        pysine.sine(frequency=440.0, duration=0.15)
        time.sleep((60/tempo)-0.15)
 

        while loop > 0:
            pysine.sine(frequency=440.0, duration=0.1)
            time.sleep((60/tempo)- 0.1)
            loop -= 1
        
        loop = timeSig - 1

def randomUpDown():
    while True:
        try:
            lowEndRange = int(input('What would you like the lowest possible tempo to be? '))
            break
        except ValueError:
            print('Please input a number')

    while True:
        try:
            highEndRange = int(input('What would you like the highest possible tempo to be? '))
            break
        except ValueError:
            print('Please input a number')

    tempo = randint(lowEndRange, highEndRange)

    

    while True:
        #1 - tempo go down
        #2 - tempo go up
        tempoPlusMinus = randint(1,2)
        
        if tempoPlusMinus == 1:
            print('-')
            loop = randint(16,30)
            while loop > 0:
                if tempo < highEndRange:
                    if tempo > lowEndRange:
                        pysine.sine(frequency=440.0, duration=0.1)
                        print((60/tempo)-0.1)
                        print(tempo)
                        time.sleep((60/tempo)-0.1)
                        tempo -= 0.5
                        loop -= 1
                    else:
                        tempo -= 1
                        break
                else:
                    tempo += 1
                    break
        
        if tempoPlusMinus == 2:
            print("+")
            loop = randint(16,30)
            while loop > 0:
                if tempo > lowEndRange:
                    if tempo < highEndRange:
                        pysine.sine(frequency=440.0, duration=0.1)
                        print((60/tempo)-0.1)
                        print(tempo)
                        time.sleep((60/tempo)-0.1)
                        tempo += 0.5
                        loop -= 1
                    else:
                        tempo -= 1
                        break
                
                
                else:
                    tempo += 1
                    break
        
        
        






while True:
    try:
        metronomeType = int(input('1 - Steady Metronome\n2 - Accelecerating/Decelerating Metronome\n3 - Disappearing Beats\n4 - Phasing Beats\n5 - Agogic\n6 - Random Up and Down\nWhat type of metronome would you like to use? '))
        break
    except ValueError:
        print('Please input a number')

if metronomeType == 1:
    steady()

if metronomeType == 2:
    acceldecel()

if metronomeType == 3:
    randomBeat()

if metronomeType == 4:
    beatPhasing()

if metronomeType ==5:
    Agogic()

if metronomeType == 6:
    randomUpDown()





