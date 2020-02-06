#! /usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

def callback(msg):
  print msg.pose.pose

rospy.init_node('coordinate_initial')
position_sub = rospy.Subscriber('/initialpose', PoseWithCovarianceStamped, callback)

rospy.spin()
