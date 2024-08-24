import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class Pos_marker(Node):
    def __init__(self):
        super().__init__("Position_marker")
        self.sub = self.create_subscription(Pose,"/turtle1/pose",self.cordinates,10)

    def cordinates(self, msg:Pose):
       if 3.0<msg.x<9.0 and 3.0<msg.y<9.0:

           self.get_logger().info(" turtle is safe and secure ")
       else:
           self.get_logger().warning("turtle get outside the perimeter !!!!")


def main(args=None):
    rclpy.init(args=args)
    node = Pos_marker()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()