#! /usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

rospy.init_node('application', anonymous=True)
client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
client.wait_for_server()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"
goal.target_pose.header.stamp = rospy.Time.now()
goal.target_pose.pose.position.x = 1.0
goal.target_pose.pose.orientation.w = 1.0


client.send_goal(goal)
client.wait_for_result()

goal.target_pose.header.frame_id = "map"
goal.target_pose.header.stamp = rospy.Time.now()
goal.target_pose.pose.position.x = 7.0
goal.target_pose.pose.position.y = -7.0

goal.target_pose.pose.orientation.z = -0.1
goal.target_pose.pose.orientation.w = 0.1

client.send_goal(goal)
client.wait_for_result()

goal.target_pose.header.frame_id = "map"
goal.target_pose.header.stamp = rospy.Time.now()
goal.target_pose.pose.position.x = 3.0
goal.target_pose.pose.position.y = 20.0

goal.target_pose.pose.orientation.z = -0.1
goal.target_pose.pose.orientation.w = 0.1

client.send_goal(goal)
client.wait_for_result()