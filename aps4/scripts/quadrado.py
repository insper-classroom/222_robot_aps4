#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist, Vector3
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
        self.cmd_vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size=3)
        self.duration = 5.0

        self.cmd_vel_pub.publish(Twist(Vector3(0,0,0), Vector3(0,0,0)))
    
    def forward(self, distance: float = 0.5):
        vel = Twist(Vector3(distance / self.duration,0,0), Vector3(0,0,0))
        self.cmd_vel_pub.publish(vel)
        rospy.sleep(self.duration)

    def rotate(self, angle: float = np.pi/2):
        vel = Twist(Vector3(0,0,0), Vector3(0,0,angle / self.duration))
        self.cmd_vel_pub.publish(vel)
        rospy.sleep(self.duration)

    def control(self):
        '''
        This function is called every time the robot receives a new image.
        '''
        
        print("forward")
        self.forward(0.5)
        print("rotate")
        self.rotate(np.pi/2)
        print("forward")
        self.forward(0.5)
        print("rotate")
        self.rotate(np.pi/2)
        print("forward")
        self.forward(0.5)
        print("rotate")
        self.rotate(np.pi/2)
        print("forward")
        self.forward(0.5)
        print("rotate")
        self.rotate(np.pi/2)
        
def main():
    rospy.init_node('Controler')
    control = Control()
    rospy.sleep(2)

    while not rospy.is_shutdown():
        control.control()

if __name__=="__main__":
    main()