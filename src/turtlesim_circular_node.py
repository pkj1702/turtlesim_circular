#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim_circular.msg import circular
radius, velocity, direction = 0, 0, 0
msg = Twist()
##turtlesim_node has turtle1/cmd_vel topic

def circular_callback(input):
    msg.linear.x = input.velocity
    msg.angular.z = input.velocity / input.radius
    if input.direction =="CW":
        msg.angular.z=-msg.angular.z

if __name__ == '__main__':
    rospy.init_node('turtlesim_circular_node', anonymous=True)
    sub=rospy.Subscriber('turtlesim_circular_motion', circular, circular_callback)
    ## subscribe pub_custom_msg node
    pub= rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()
    rospy.spin()