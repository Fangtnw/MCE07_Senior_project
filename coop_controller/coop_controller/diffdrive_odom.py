#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3Stamped, TransformStamped
from nav_msgs.msg import Odometry
from std_msgs.msg import Header
from math import sin, cos
import tf2_ros
from tf2_ros import TransformBroadcaster

wheel_distance = 0.55

class OdometryNode(Node):
    def __init__(self):
        super().__init__('odometry_node')

        self.get_logger().info('Differentail-drive Odometry Node is running')

        self.left_encoder_ticks = 0
        self.right_encoder_ticks = 0
        self.left_vel = 0.0
        self.right_vel = 0.0
        self.angular_velocity = 0.0

        # Initialize the robot state variables
        self.Robot_X = 0.0
        self.Robot_Y = 0.0
        self.Robot_Yaw = 0.0
        self.Robot_LinVel = 0.0
        self.Robot_AngVel = 0.0

        self.odom_pub = self.create_publisher(Odometry, 'odom', 100)
        # self.encoder_ticks_sub = self.create_subscription(
        #     Vector3Stamped, 'diff_encoder_ticks', self.encoder_ticks_callback, 100)
        self.encoder_vel_sub = self.create_subscription(
            Vector3Stamped, 'diff_encoder_vel', self.encoder_vel_callback, 1)
        self.imu_sub = self.create_subscription(
            Vector3Stamped, 'diff_imu', self.imu_callback, 1)

        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.05, self.publish_odometry)

    def encoder_ticks_callback(self, msg):
        self.left_encoder_ticks = msg.vector.x
        self.right_encoder_ticks = msg.vector.y

    def encoder_vel_callback(self, msg):
        self.left_vel = msg.vector.x
        self.right_vel = msg.vector.y

    def imu_callback(self, msg):
        self.Robot_Yaw = msg.vector.z
        
    def publish_odometry(self):
        odom_msg = Odometry()

        # Set the frame_id field in the Odometry message
        odom_msg.header.frame_id = 'odom'
        odom_msg.header.stamp = self.get_clock().now().to_msg()

        # Set the child_frame_id to "base_link"
        odom_msg.child_frame_id = "base_link"

        # Perform your odometry calculations here using encoder ticks, velocities, and IMU data
        # Replace the following placeholder values with your calculations
        time_step = 0.05 
        self.forward_kinematic()
        self.odom_compute(time_step)

        odom_msg.pose.pose.position.x = self.Robot_X
        odom_msg.pose.pose.position.y = self.Robot_Y
        odom_msg.pose.pose.position.z = 0.0

        # Assuming IMU provides yaw directly
        odom_msg.pose.pose.orientation.z = sin(self.Robot_Yaw / 2)
        odom_msg.pose.pose.orientation.w = cos(self.Robot_Yaw / 2)

        odom_msg.twist.twist.linear.x = self.Robot_LinVel
        odom_msg.twist.twist.angular.z = self.Robot_AngVel

        # Set covariance matrices
        odom_msg.pose.covariance[0] = 0.1  # Example covariance value for x position
        odom_msg.pose.covariance[7] = 0.1  # Example covariance value for y position
        # ... Set other covariance values as needed

        odom_msg.twist.covariance[0] = 0.1  # Example covariance value for x linear velocity
        odom_msg.twist.covariance[35] = 0.1  # Example covariance value for z angular velocity
        # ... Set other covariance values as needed

        # Publish odometry message
        self.odom_pub.publish(odom_msg)

        # map_to_odom_transform = TransformStamped()
        # map_to_odom_transform.header.stamp = self.get_clock().now().to_msg()
        # map_to_odom_transform.header.frame_id = 'map'
        # map_to_odom_transform.child_frame_id = 'odom'
        # map_to_odom_transform.transform.translation.x = self.Robot_X
        # map_to_odom_transform.transform.translation.y = self.Robot_Y
        # map_to_odom_transform.transform.translation.z = 0.0
        # map_to_odom_transform.transform.rotation.z = sin(self.Robot_Yaw / 2)
        # map_to_odom_transform.transform.rotation.w = cos(self.Robot_Yaw / 2)
        # self.tf_broadcaster.sendTransform(map_to_odom_transform)
        
        # Publish TF transform
        transform = TransformStamped()
        transform.header = Header()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = 'odom'
        transform.child_frame_id = 'base_link'
        transform.transform.translation.x = self.Robot_X
        transform.transform.translation.y = self.Robot_Y
        transform.transform.translation.z = 0.0
        transform.transform.rotation.z = sin(self.Robot_Yaw / 2)
        transform.transform.rotation.w = cos(self.Robot_Yaw / 2)
        self.tf_broadcaster.sendTransform(transform)

        # Publish TF transform from 'base_link' to 'base_footprint'
        transform_base_link_to_base_footprint = TransformStamped()
        transform_base_link_to_base_footprint.header.stamp = self.get_clock().now().to_msg()
        transform_base_link_to_base_footprint.header.frame_id = 'base_link'
        transform_base_link_to_base_footprint.child_frame_id = 'base_footprint'
        transform_base_link_to_base_footprint.transform.translation.x = 0.0  # Adjust as needed
        transform_base_link_to_base_footprint.transform.translation.y = 0.0  # Adjust as needed
        transform_base_link_to_base_footprint.transform.translation.z = 0.0  # Adjust as needed
        transform_base_link_to_base_footprint.transform.rotation.z = 0.0  # Adjust as needed
        transform_base_link_to_base_footprint.transform.rotation.w = 1.0  # Adjust as needed
        self.tf_broadcaster.sendTransform(transform_base_link_to_base_footprint)

    def forward_kinematic(self):
        self.Robot_LinVel = (self.right_vel + self.left_vel) * 0.5
        self.Robot_AngVel = (self.right_vel - self.left_vel) / wheel_distance

    def odom_compute(self, time_step):
        temp_tetra = self.Robot_Yaw + (self.Robot_AngVel * time_step * 0.5)
        self.Robot_X = self.Robot_X + cos(temp_tetra) * self.Robot_LinVel * time_step
        self.Robot_Y = self.Robot_Y + sin(temp_tetra) * self.Robot_LinVel * time_step
        self.Robot_Yaw = self.Robot_Yaw + self.Robot_AngVel * time_step

def main(args=None):
    rclpy.init(args=args)
    odometry_node = OdometryNode()
    rclpy.spin(odometry_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
