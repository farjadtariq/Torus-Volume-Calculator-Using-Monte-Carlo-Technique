#main.py
#
#Author:        Farjad Tariq
#Version:       2023/08/9
#
#Purpose:       The purpose of this is to write a complete Python 
#               program that computes the volume of a torus using the 
#               Monte Carlo technique. A torus is similar in shape to a donut or
#               the inner tube for a tire.

from time import ctime
from numpy.random import uniform
from numpy import sum, sqrt, pi

def displayTerminationMessage():
    print(f"""
Programmed by Farjad Tariq
Date: {ctime()}
End of processing.\n""")

def getPositive(prompt):
    #prompt = the prompt to display to the user
    #value = the number entered by the user
    while True:
        value = input(prompt).strip()
        if value != '':
            try:
                value = eval(value,{},{})
            except:
                print(value,'is not valid')
            else:
                if type(value) != int and type(value) != float:
                    print(value,'is not a number')
                else:
                    if value <= 0:
                        print(value, 'is less than 0!')
                    else:
                        break
        else:
            print('Missing input!')

    return(value)
            
            
def monteTorus(R, r, points):
    #limitXY = largest possible X and Y coordinates in the torus
    #R = major radius
    #r = minor radius
    #points = random points
    #xCoords = x coordinates
    #yCoords = y coordinates
    #zCoords = z coordinates
    #C = computed coordinate
    #inTorus = point in torus
    #probability = probability of point being in torus
    #torusVolume = approximate volume of torus
    limitXY = R + r
    xCoords = uniform(-limitXY, limitXY, points)
    yCoords = uniform(-limitXY, limitXY, points)
    zCoords = uniform(-r, r, points)
    C = sqrt(xCoords**2 + yCoords**2) - R
    inTorus = sqrt(C**2 + zCoords**2) <= r
    probability = sum(inTorus) / points
    torusVolume = probability * (2 * limitXY)**2 * (2 * r) 
    return probability, torusVolume


def main():
    #R = major radius
    #r = minor radius
    #points = random points
    #probability = probability of point being in torus
    #torusVolume = approximate volume of torus
    #actualVolume = actual volume of the torus
    print('\n' + '-' * 80)
    R = float(getPositive('Enter the major radius of the torus: '))
    r = float(getPositive('Enter the minor radius of the torus: '))
    if r >= R:
        print('The minor radius must be less than the major radius!')
    else:
        points = int(getPositive('Enter the number of points to create: '))
        probability, torusVolume = monteTorus(R, r, points)
        actualVolume = 2 * r**2 * pi**2 * R

        print('''
The probability of a point being in Torus is %.4f
The approximate volume of the torus is: %.14e
The actual volume of the torus is: %.14e
The error in the approximate volume is: %.6e''' 
              % (probability, torusVolume, actualVolume, abs(torusVolume - actualVolume)))

        displayTerminationMessage()

main()