import rclpy
from rclpy.node import Node

import cv2
import numpy as np
from cv_bridge import CvBridge

from sensor_msgs.msg import Image

class LaneDetect(Node):
    def __init__(self):
        super().__init__('lane_detect')

        self.sub_ = self.create_subscription(
            Image,
            '/camera/color/image_raw',
            self.image_callback,
            10
        )
        self.sub_

        self.br = CvBridge()
    def image_callback(self,msg):
        cv_image = self.br.imgmsg_to_cv2(msg, 'bgr8')
        roi_image = cv_image(400: 480, 0: 320)

        cv2.imshow('orig_imgae',cv_image)
        cv2.imshow('roi_img', roi_image)

        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
    lane_detect = LaneDetect()

    rclpy.spin(lane_detect)
    
    lane_detect.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()