import rospy 
from pacmod_msgs.msg import PacmodCmd
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
import time
import torch

class DetectorManager:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_topic =  '/mako_1/mako_1/image_raw'
        # define subscriber
        self.image_sub = rospy.Subscriber(self.image_topic, Image, self.imageCb, queue_size = 1)
        # define publisher
        self.brake_pub = rospy.Publisher('/pacmod/as_rx/brake_cmd', PacmodCmd, queue_size = 1)
        self.forward_pub = rospy.Publisher('/pacmod/as_rx/accel_cmd', PacmodCmd, queue_size = 1)
    
        
        # Spin
        rospy.spin()
        

    def imageCb(self, data):
        try:
            
            self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
            self.model.conf = 0.5  # confidence threshold (0-1)
            self.cv_image = self.bridge.imgmsg_to_cv2(data, "rgb8")
            results = self.model(self.cv_image[:,:,::-1], size=640).xyxy[0]
            # print(results)
            person_exists = results[:,-1].tolist()
            if 0 in person_exists:
                print("Person detected, cause the vehicle to brake")
                self.brake_pub.publish(f64_cmd=1, enable=True)
            else:
                self.forward_pub.publish(f64_cmd=0.35, enable=True)
            # else:
            #     self.signal_pub.publish(f64_cmd=0.0, enable=True)
            #     print("No person detected, continue driving")
        except CvBridgeError as e:
            print(e)
            

if __name__=="__main__":
    # Initialize node
    rospy.init_node("detector_manager_node")
    # Define detector object
    dm = DetectorManager()