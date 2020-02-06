#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback(msg):
  position_m = msg.pose.pose.position
  orientation_m = msg.pose.pose.orientation

  position_list = [position_m.x-4.43377590179, position_m.y+0.42563393712, position_m.z]
  orientation_list = [orientation_m.x, orientation_m.y, orientation_m.z+0.998427995068, orientation_m.w+0.0560494305371]  
  
  print "Position", position_list
  print "Orientation", orientation_list

rospy.init_node('camera_odometry')
odom_sub = rospy.Subscriber('/t265/odom/sample', Odometry, callback)

rospy.spin()


