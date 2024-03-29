#!/usr/bin/env python



import rospy
# from std_msgs.msg import String
from geometry_msgs.msg import Twist


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.linear)

def listener():


    rospy.init_node('listener', anonymous=True)

    # rospy.Subscriber('chatter', String, callback)
    rospy.Subscriber('cmd_vel', Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
