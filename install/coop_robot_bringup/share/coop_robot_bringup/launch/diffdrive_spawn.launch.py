from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command,PathJoinSubstitution,LaunchConfiguration,PythonExpression
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription,DeclareLaunchArgument
from ament_index_python.packages import get_package_share_path
from launch.conditions import IfCondition
import xacro

def generate_launch_description():

    xacro_diff=os.path.join(get_package_share_path('my_robot_description'),
                           'urdf','diffdrive.xacro')

    rviz_config_path=os.path.join(get_package_share_path('my_robot_description'),
                           'rviz','urdf_config.rviz')

    diff_description=xacro.process_file(xacro_diff).toxml()
    
    diff_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description':diff_description} , {'use_sim_time': True}],
        namespace="diffdrive",
        output='screen',
    )
 
    rviz2 = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', rviz_config_path]
    )

    spawn_diffdrive= Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic", "/diffdrive/robot_description",
            "-entity", "diffdrive",
            "-x", "1.25",   # Example: Set x-coordinate to 1.0
            "-y", "2.0",   # Example: Set y-coordinate to 2.0
            "-z", "0.0",   # Example: Set z-coordinate to 0.0
            "-Y","-1.57",
        ],
        namespace="diffdrive",
        output='screen'
    )

    spawn_follow_diffdrive= Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic", "/diffdrive/robot_description",
            "-entity", "diffdrive",
            "-x", "1.25",   # Example: Set x-coordinate to 1.0
            "-y", "0.1",   # Example: Set y-coordinate to 2.0
            "-z", "0.0",   # Example: Set z-coordinate to 0.0
            "-Y","1.57",
        ],
        namespace="diffdrive",
        output='screen'
    )


    return LaunchDescription([
        spawn_follow_diffdrive,
        # spawn_diffdrive,
        diff_state_publisher,
    ])