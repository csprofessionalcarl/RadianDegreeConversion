#Converting Radians into Degrees
#Given a number input(Radians), provide an output(Degrees)
import math, numbers

#Prompt user for input
sass = 0
print('(Radian > Degrees Conversion)')
rad = input('Please provide a Radian Value to be converted\n')

try:
    rad = float(rad)
except:
    #Ensure input is only numerical
    while(isinstance(rad,numbers.Number) == False):
        #Output error and reprompt if nonnumerical
        rad = input('Value Needs to be numerical...\n')
        try:
            rad = float(rad)
        except:
            sass = 1
            print("That's still not a number...")
    

if(sass == 1):
    print("Finally...\n")

#Apply formula
#Degrees = (Radians *180)/(pi)
deg = (rad*180)/(math.pi)



#Output
print("Radian: {}" .format(rad))
print("Degrees: {}".format(deg))
