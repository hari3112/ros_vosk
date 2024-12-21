#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
twist=None
def callback(data):
    command=data.data.lower()
    rospy.loginfo(f"Received command: {command}")
    
    
    if command=='start':
       twist.linear.x=0.3
    elif command=='back':
       twist.linear.x=-0.3
    elif command=='left':
       twist.angular.z=0.3
    elif command=='right':
       twist.angular.z=-0.3
       
    else: 
       twist.linear.x=0
       twist.angular.z=0
    pub.publish(twist)
      
if __name__=='__main__':
    rospy.init_node('speech_to_cmd_velocity')
    pub=rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    rospy.Subscriber('/speech_recognition/final_result',String,callback)
    rate=rospy.Rate(10)
    twist=Twist()
    while not rospy.is_shutdown():
      pub.publish(twist)
      rate.sleep()
    
    
