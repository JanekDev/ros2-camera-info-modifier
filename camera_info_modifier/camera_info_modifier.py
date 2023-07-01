import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CameraInfo

class CameraInfoModifier(Node):
    def __init__(self):
        super().__init__('camera_info_modifier')
        self.subscription = self.create_subscription(
            CameraInfo,
            '/camera/camera_info',  # Replace with your camera info topic name
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(CameraInfo, 'output_camera_info', 10)

        # These are your custom parameters
        self.d = [-0.01670666080688256, 0.02931950598914883, -8.567781365429342e-05, -0.0006453265541211077, 0.0]
        self.k = [699.4761002238013, 0.0, 644.7534032681316, 0.0, 697.3328857022241, 509.9200413013962, 0.0, 0.0, 1.0]
        self.r = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        self.p = [718.5772705078125, 0.0, 642.7066899250713, 0.0, 0.0, 717.213623046875, 509.4021443629026, 0.0, 0.0, 0.0, 1.0, 0.0]
        self.height = 1024
        self.width = 1280

    def listener_callback(self, msg):
        msg.d = self.d
        msg.k = self.k
        msg.r = self.r
        msg.p = self.p
        msg.height = self.height
        msg.width = self.width
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    cam_info_mod = CameraInfoModifier()
    rclpy.spin(cam_info_mod)
    cam_info_mod.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
