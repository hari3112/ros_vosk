#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

class Voice_goal_publisher:
    def __init__(self):
        rospy.init_node('voice_goal_publisher',anonymous=True)
        self.goal_pub=rospy.Publisher('/move_base_simple/goal',PoseStamped,queue_size=10)
        rospy.Subscriber('/speech_recognition/final_result',String,self.voice_callback)

    def voice_callback(self,msg):
        rospy.loginfo(f"Received voice command: {msg.data}")
        if msg.data=="hello":
            self.publish_goal1()
        elif msg.data=="right":
            self.publish_goal2()
        elif msg.data=="back":
            self.publish_goal3() 
        else:
            print("____________________________improper command______________________________\n")   

    def publish_goal1(self):
        goal=PoseStamped()
        goal.header.frame_id="map"
        goal.header.stamp = rospy.Time.now()

        goal.pose.position.x=4.865048408508301
        goal.pose.position.y=-0.6560588479042053
        goal.pose.position.z=0.0
        goal.pose.orientation.x=0.0
        goal.pose.orientation.y=0.0
        goal.pose.orientation.z=0.6851957657052036
        goal.pose.orientation.w=0.7283589517948275

        rospy.loginfo("Publishing goal to move_base_simple/goal")
        self.goal_pub.publish(goal)
    

    def publish_goal2(self):
        goal=PoseStamped()
        goal.header.frame_id="map"
        goal.header.stamp = rospy.Time.now()

        goal.pose.position.x=-4.9145355224609375
        goal.pose.position.y=3.915374755859375
        goal.pose.position.z=0.0
        goal.pose.orientation.x=0.0
        goal.pose.orientation.y=0.0
        goal.pose.orientation.z=-0.7888192169449699
        goal.pose.orientation.w=0.6146252866408316

        rospy.loginfo("Publishing goal to move_base_simple/goal")
        self.goal_pub.publish(goal)


    def publish_goal3(self):
        goal=PoseStamped()
        goal.header.frame_id="map"
        goal.header.stamp = rospy.Time.now()

        goal.pose.position.x=-5.480107307434082
        goal.pose.position.y=-3.145580291748047
        goal.pose.position.z=0.0
        goal.pose.orientation.x=0.0
        goal.pose.orientation.y=0.0
        goal.pose.orientation.z= -0.5262328970258251
        goal.pose.orientation.w=0.8503404836227706

        rospy.loginfo("Publishing goal to move_base_simple/goal")
        self.goal_pub.publish(goal)    



    def run(self):
        rospy.spin()



if __name__=='__main__':
    try:
        node=Voice_goal_publisher()
        node.run()
    except rospy.ROSInterruptException:
        pass