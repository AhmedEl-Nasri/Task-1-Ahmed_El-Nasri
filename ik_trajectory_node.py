import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Point
import math

class IndustrialIkTrajectoryNode(Node):

    def __init__(self):
        super().__init__('ik_trajectory_node')
        self.joint_pub = self.create_publisher(JointState, '/joint_states', 10)
        self.target_sub = self.create_subscription(Point, '/arm_target_pose', self.target_callback, 10)
        
        self.L1 = 0.2
        self.L2 = 0.4
        self.L3 = 0.5
        
        self.obstacle_center = [0.3, 0.3, 0.4]
        self.obstacle_radius = 0.15

        self.get_logger().info("Industrial Kinematics & Trajectory Controller Activated.")

    def target_callback(self, msg):
        target_x = msg.x
        target_y = msg.y
        target_z = msg.z

        distance_to_obstacle = math.sqrt(
            (target_x - self.obstacle_center[0])**2 + 
            (target_y - self.obstacle_center[1])**2 + 
            (target_z - self.obstacle_center[2])**2
        )
        
        if distance_to_obstacle < self.obstacle_radius:
            self.get_logger().warn("TARGET DENIED: Trajectory path violates environmental obstacle safety boundaries!")
            return

        try:
            theta_1 = math.atan2(target_y, target_x)
            
            r = math.sqrt(target_x**2 + target_y**2)
            z_prime = target_z - self.L1
            
            D = math.sqrt(r**2 + z_prime**2)
            
            cos_theta_3 = (D**2 - self.L2**2 - self.L3**2) / (2 * self.L2 * self.L3)
            cos_theta_3 = max(-1.0, min(1.0, cos_theta_3))
            
            theta_3 = math.acos(cos_theta_3)
            theta_2 = math.atan2(z_prime, r) - math.atan2(self.L3 * math.sin(theta_3), self.L2 + self.L3 * math.cos(theta_3))

            theta_4 = 0.0
            theta_5 = 0.0
            theta_6 = 0.0

            joint_state_msg = JointState()
            joint_state_msg.header.stamp = self.get_clock().now().to_msg()
            joint_state_msg.name = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']
            joint_state_msg.position = [theta_1, theta_2, theta_3, theta_4, theta_5, theta_6]
            
            self.joint_pub.publish(joint_state_msg)
            self.get_logger().info(f"Trajectory calculated successfully. Moving to Target Point: X={target_x:.2f}, Y={target_y:.2f}, Z={target_z:.2f}")

        except ValueError:
            self.get_logger().error("Target execution failed: Coordinate is completely outside physical workspace limits.")

def main(args=None):
    rclpy.init(args=args)
    node = IndustrialIkTrajectoryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()