#!/usr/bin/env python

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
# from std_msgs.msg import String
from geometry_msgs.msg import Twist


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.linear)

def listener():

    """
    hyunmila@rosvm:~$ rostopic info /cmd_vel 
    Type: geometry_msgs/Twist

    Publishers: 
    * /turtlebot3_teleop_keyboard (http://rosvm:37985/)

    Subscribers: 
    * /gazebo (http://rosvm:43751/)
    * /listener_4704_1702230458668 (http://rosvm:45463/)

    """

    rospy.init_node('listener', anonymous=True)

    # rospy.Subscriber('chatter', String, callback)
    rospy.Subscriber('cmd_vel', Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
