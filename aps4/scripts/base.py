#!/usr/bin/env python3

from robot import Robot
import rospy
from geometry_msgs.msg import Twist, PointStamped
import numpy as np
import util

class Control():
    def __init__(self):
        self.rate = rospy.Rate(250) # 250 Hz

        # Subscribers

        # Publishers
    
    def control(self):
        '''
        This function is called every time the robot receives a new image.
        '''
        
        self.rate.sleep()

def main():
    rospy.init_node('Controler')
    control = Control()
    rospy.sleep(1)

    while not rospy.is_shutdown():
        control.control()

if __name__=="__main__":
    main()

"""
roslaunch my_simulation novas_formas.launch
"""

