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

import numpy as np
import scipy
import scipy.io as sio
import StringIO
import cv2
import matplotlib.pyplot as plt
import time
from string import ascii_lowercase, ascii_uppercase
from datetime import date
from random import choice

from rover import Rover20


class MPCR_Rover_Image(Rover20):
    def __init__(self):
        Rover20.__init__(self)
        self.currentImage = None
        self.quit = False
        self.action_choice = 1
        self.action_labels = ['left', 'forward', 'right', 'backward']
        self.action_vectors = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        self.data = np.ones(240 * 320 + 4)


    def mleft(self):  # create the function that turns the rover left so it can be called later on
        self.setTreads(-1, 1)  # set left tread in reverse and right tread forward. This rotates the rover counterclockwise, like how a tank turns.
        time.sleep(.1)  # continue that rotating movement for 0.1 seconds
        self.setTreads(0, 0)  # stop the rover's movement

    def mforward(self):  # create the function that moves the rover forward
        self.setTreads(1, 1)  # set both treads in the forward direction
        time.sleep(.1)  # continue the forward movement for 0.1 seconds
        self.setTreads(0, 0)  # stop

    def mright(self):  # create the function that turns the rover right
        self.setTreads(1, -1)  # set left tread forward and right tread in reverse
        time.sleep(.1)  # continue that rotating movement for 0.1 seconds
        self.setTreads(0, 0)  # stop

    def mbackward(self):  # create the function that moves the rover backward
        self.setTreads(-1, -1)  # set both treads in the reverse direction
        time.sleep(.1)  # continue the backward movement for 0.1 seconds
        self.setTreads(0, 0)  # stop


    # called by Rover20, acts as main loop
    def processVideo(self, jpegbytes, timestamp_10msec):
        # 240,320

        self.currentImage = cv2.imdecode(np.asarray(bytearray(jpegbytes), dtype=np.uint8), 0)

        self.pattern = np.reshape(self.currentImage, (240 * 320))
        # Ask the user to enter a number for a specific action. The number entered is now equal to self.action_choice
        self.action_choice = input("Enter 1 for left, 2 for forward, 3 for right, 4 for reverse, 5 for save and quit)")
        
        self.action_choice = self.action_choice - 1  # Subtract 1 from the value assigned to self.action_choice
                            # this makes the value entered align with the value required for the operation (seen in lines ~72, 90-100)
        if self.action_choice == 4:
            datasave = {}
            datasave['data'] = self.data
            uniqueKey = ''.join(choice(ascii_lowercase + ascii_uppercase) for _ in range(5))
            uniqueKey = 'test'
            sio.savemat('MPCR_Rover_Images_' + uniqueKey + '.mat', datasave)
            print 'File Saved: MPCR_Rover_Images_' + uniqueKey + '_.mat'
            self.quit = True
            return

        action_pixel = np.zeros(4)

        action_pixel[self.action_choice] = 1

        self.pattern = np.concatenate((self.pattern, action_pixel))

        self.data = np.column_stack((self.data, self.pattern))

        print np.asarray(self.data).shape[1]

        if self.action_choice == 0:    # If self.action_choice equals 0, run self.mleft(). We've already defined what that is,
            self.mleft()               # so the rover turns left. If it doesn't equal 0, check the next "elif"
        elif self.action_choice == 1:  # If self.action_choice equals 1, move the rover forward according 
            self.mforward()            # to the self.mforward() function. If it doesn't, check the next "elif".
        elif self.action_choice == 2:  # If self.action_choice equals 2, turn the rover right.
            self.mright()              # If it doesn't, move on and check the next "elif"
        elif self.action_choice == 3:  # If self.action_choice equals 3, move the rover backward.
            self.mbackward()


def main():
    rover = MPCR_Rover_Image()

    while not rover.quit:
        pass

    rover.close()


if __name__ == '__main__':
    main()

