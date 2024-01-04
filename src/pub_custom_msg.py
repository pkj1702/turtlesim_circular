#!/usr/bin/env python3
import rospy
from turtlesim_circular.msg import circular

custom_msg_pub = rospy.Publisher('turtlesim_circular_motion', circular, queue_size=10)
rospy.init_node('pub_custom_msg', anonymous=True)
rate = rospy.Rate(10)
msg = circular()
while not rospy.is_shutdown(): 
    print("Put your radius")
    msg.radius = int(input())

    print("Put your velocity")
    msg.velocity = int(input())

    print("Put your direction")
    msg.direction = input()

    custom_msg_pub.publish(msg)
    rate.sleep()

    










