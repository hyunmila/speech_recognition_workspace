#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist




def talker():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    # rospy.init_node('talker')
    rate = rospy.Rate(0.5) # 10hz
    i=0
    
    # while not rospy.is_shutdown():
    while i<2:
        msg = Twist()
        msg.linear.x=0.0
        rospy.loginfo(msg)
        # print("i", i)
        pub.publish(msg)
        rate.sleep()
        i+=1
    
# if __name__ == '__main__':
def node_start():
    print("starting the node")
    rospy.init_node('talker')
    talker()
    print("ass")

# if __name__ == '__main__':
#     try:
#         talker()
#     except rospy.ROSInterruptException:
#         pass