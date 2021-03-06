#!/usr/bin/env python

import rospy

import message_filters

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

def callback(pos, vel):
    x = pos.pose.pose.position.x
    y = pos.pose.pose.position.y
    z = pos.pose.pose.orientation.z

    dx = vel.linear.x
    dy = vel.linear.y
    dz = vel.angular.z

    rospy.loginfo('x: {}, y: {}, z: {}'.format(x, y, z))
    rospy.loginfo('dx: {}, dy: {}, dz: {}'.format(dx, dy, dz))

def main():
    rospy.init_node('location_monitor', anonymous=True)
    odom_sub =  message_filters.Subscriber("/odom", Odometry)
    vel_sub =  message_filters.Subscriber("/cmd_vel", Twist)

    ats = message_filters.ApproximateTimeSynchronizer([odom_sub, vel_sub], queue_size = 1, slop = 0.1, allow_headerless=True)
    ats.registerCallback(callback)
    rospy.spin()

if __name__== '__main__':
    main()
