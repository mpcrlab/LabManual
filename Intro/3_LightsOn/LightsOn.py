########################################################
#------------------------------------------------------#
#
# Machine Perception and Cognitive Robotics Laboratory
#
#     Center for Complex Systems and Brain Sciences
#               Florida Atlantic University
#
#------------------------------------------------------#
########################################################
#------------------------------------------------------#
#LabManual


#timer

from rover import Rover20
import time


def main():  # defining the function called "main()"
    rover = Rover20()  # redefine the module Rover20 so we can use "rover" instead. It makes things easier.

    rover.turnLightsOn()  # turn on green lights
    time.sleep(1)  # make the rover wait 1 second in its current state

    rover.turnLightsOff()  # turn off green lights. Duh!
    time.sleep(1)  # make the rover wait 1 second in its current state

    rover.close()  # close rover


main()  # run the function we have just defined
