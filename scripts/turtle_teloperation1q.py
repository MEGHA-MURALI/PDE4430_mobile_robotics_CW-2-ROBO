#!/usr/bin/env python3

#import necessary libraries
import rospy             
import getch
from geometry_msgs.msg import Twist

#The topic "/turtle1/cmd vel" will be published by the publisher

pub = rospy.Publisher('rover/base_controller/cmd_vel', Twist, queue_size=10)

#'turtle teleoperator' is the name of the newly created node, 
#and anonymous=False is used to ensure that the node exists with same name

node = rospy.init_node('turtle_teleoperator',anonymous=False) 

#ROS Rate will dynamically select the appropriate sleep duration 
#in order to adhere to the specified frequency.
rate = rospy.Rate(50) 

#funcion that help to assign keyboard keys for turtle movement and speed changes
def key_move():

    #assigning initial values to linear and angular velocity variables
    linear=0.4          
    angular=0.4

    while not rospy.is_shutdown():
        k=ord(getch.getch())
        #press'u' to move the turtle straight 
        if k==117:
            rospy.loginfo("Up")
            move_turtle(linear,0.0)
        #press 'd' to move the turtle back
        elif k==100:
            rospy.loginfo("Down")
            move_turtle(-linear,0.0)
        #press 'r' to move the turtle right
        elif k==114:
            rospy.loginfo("Right")
            move_turtle(0.0,-angular)
        #press 'l' to move the turtle left
        elif k==108:
            rospy.loginfo("Left")
            move_turtle(0.0,angular)
        #press 's' to stop the turtle
        elif k==115:
            rospy.loginfo("Stop")
            move_turtle(0.0,0.0)
        #press 'up arrow' to increase linear speed
        elif k==65:
            rospy.loginfo("Increase linear speed")
            linear+=0.2
        #press 'down arrow' to decrease linear speed
        elif k==66:
            rospy.loginfo("Decrease linear speed")
            linear-=0.2
        #press 'right arrow' to increase angular speed
        elif k==67:
            rospy.loginfo("Increase angular speed")
            angular+=0.2
        #press 'left arrow' to decrease angular speed
        elif k==68:
            rospy.loginfo("Decrease angular speed")
            angular-=0.2
       

#function to move the turtle according to the keyboard interface
def move_turtle(linear,angular):
    move_cmd = Twist()
    move_cmd.linear.x = linear
    move_cmd.angular.z = angular
    pub.publish(move_cmd)
    rate.sleep()

if __name__ == '__main__':
        key_move()
   


