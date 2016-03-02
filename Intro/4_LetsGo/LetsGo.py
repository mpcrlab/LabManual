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
from rover import Rover20
import time


def main():  # create a function called "main()"


    rover = Rover20()  # create rover

    # The parenthesis is set up as (Left Tread, Right Tread). 1 is forwards, 0 is off, and -1 is backwards.
    rover.setTreads(1, 1)  # forwards
    time.sleep(1)  # wait 1 second

    rover.setTreads(0, 0)  # stop
    time.sleep(1)

    rover.setTreads(-1, -1)  # backwards
    time.sleep(1)

    rover.setTreads(0, 0)
    time.sleep(1)
    

    rover.close()  # close rover


main()  # Run the function we just defined. The rover will move forward for 1 second, stop for 1 second, 
        # move backward for 1 second, stop for 1 second, and then the program will end.
