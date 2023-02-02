#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist, PointStamped
import numpy as np

""" 
Running
    roslaunch my_simulation novas_formas.launch
    rosrun aps4 quadrado.py

"""

class Control():
    def __init__(self):
        super().__init__()

        # Publishers
        self.cmd_vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)

        self.cmd_vel_pub.publish(Twist())
    
    def forward(self, distance: float = 1.0, vel= Twist()):
        vel.linear.x = distance
        self.cmd_vel_pub.publish(vel)
        rospy.sleep(1.0)

    def rotate(self, angle: float = np.pi/2, vel= Twist()):
        vel.angular.z = angle
        self.cmd_vel_pub.publish(vel)
        rospy.sleep(1.0)

    def control(self):
        '''
        This function is called every time the robot receives a new image.
        '''
        
        self.forward()
        print("forward")
        self.rotate(np.pi/2)
        self.forward()
        self.rotate(np.pi/2)
        self.forward()
        self.rotate(np.pi/2)
        self.forward()
        self.rotate(np.pi/2)
        
def main():
    rospy.init_node('Controler')
    control = Control()
    rospy.sleep(1)

    while not rospy.is_shutdown():
        control.control()

if __name__=="__main__":
    main()