#!/usr//bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from turtlesim.msg import Pose
class NewPub(Node):
    def __init__(self):
        super().__init__("Publisher_node")
        self.pub = self.create_publisher(Pose,"/turtle1/pose", 10)
        self.time = self.create_timer(1,self.callback)
        self.get_logger().info("new publisher has been created")

    def callback(self):
        cord = Pose()
        self.pub.publish(cord)

def main(args= None):
    rclpy.init(args=args)
    node = NewPub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()