#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import time

twist = None
command_time = 0
command_type = None

def callback(data):
    global twist, command_time, command_type
    command = data.data.lower()
    rospy.loginfo(f"Received command: {command}")
    
    if command == 'start':
        twist.linear.x = 0.3
        twist.angular.z = 0
        command_type = 'start'
    elif command == 'back':
        twist.linear.x = -0.3
        twist.angular.z = 0
        command_type = 'back'
    elif command in ['left', 'right']:
        if command == 'left':
            twist.angular.z = 0.3
        elif command == 'right':
            twist.angular.z = -0.3
        twist.linear.x = 0
        command_time = time.time()  # Record the time of command
        command_type = command
    else:
        twist.linear.x = 0
        twist.angular.z = 0
        command_type = 'stop'
    
    pub.publish(twist)

if __name__ == '__main__':
    rospy.init_node('speech_to_cmd_velocity')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/speech_recognition/final_result', String, callback)
    rate = rospy.Rate(10)
    twist = Twist()

    while not rospy.is_shutdown():
        if command_type in ['left', 'right']:
            # If the command is 'left' or 'right', stop after 2 seconds
            if time.time() - command_time >= 2:
                twist.linear.x = 0
                twist.angular.z = 0
                pub.publish(twist)
                command_type = 'stop'  # Reset to avoid continuous stop command
        pub.publish(twist)
        rate.sleep()
