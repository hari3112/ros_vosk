#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class camera:
    def __init__(self) :
        self.camera_subscriber=rospy.Subscriber('/camera/rgb/image_raw',Image,self.camera_callback)
        self.out=cv2.VideoWriter('/home/haris/Videos/output.avi',cv2.VideoWriter_fourcc('M','J','P','G'),10,(640,480))
        self.bridge=CvBridge()
    def camera_callback(self,data):
        frame=self.bridge.imgmsg_to_cv2(data)
        print(frame.shape)
        #edge_frame=cv2.Canny(frame,100,200)
        #self.out.write(frame)
        #self.out.write(edge_frame)
        cv2.imshow("output",frame)
        #cv2.imshow("output2",edge_frame)
        cv2.waitKey(1)


if __name__=='__main__':
    node_name="camera_check"
    rospy.init_node(node_name)
    camera()
    rospy.spin()      