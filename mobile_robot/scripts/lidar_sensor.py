#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan 

class sensor_checking:
    def __init__(self):
        sub_topic_name="/scan"
        self.lidar_subscriber=rospy.Subscriber(sub_topic_name,LaserScan,self.lidar_cb)

    def lidar_cb(self,data):
        print(min(data.ranges))

if __name__=='__main__':
    node_name="lidar_check"
    rospy.init_node(node_name)
    sensor_checking()
    rospy.spin()
