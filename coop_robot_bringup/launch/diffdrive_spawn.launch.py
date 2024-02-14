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

    diff_description = ParameterValue(Command(['xacro ',xacro_diff]),value_type=str)
    
    gazebo_launch_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py'])
        ])
    )

    gazebo_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('gazebo_ros'),
                'launch',
                'gzserver.launch.py'
            ])
        ]),
        launch_arguments={'world': get_package_share_directory('my_robot_description') + '/urdf/workshop_test.world','verbose': 'false'}.items(),
    )   

    gazebo_client = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('gazebo_ros'),
                'launch',
                'gzclient.launch.py'
            ])
        ]),
    )

    diff_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description':diff_description} , {'use_sim_time': True}]
    )

    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    rviz2 = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', rviz_config_path]
    )

    static_transform_publisher = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="tf_footprint_base",
        output="screen",
        arguments=["0", "0", "0", "0", "0", "0", "base_link", "base_footprint"]
    )

    spawn_diffdrive= Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic", "robot_description",
            "-entity", "diffdrive",
            "-x", "1.25",   # Example: Set x-coordinate to 1.0
            "-y", "0.0",   # Example: Set y-coordinate to 2.0
            "-z", "0.0",   # Example: Set z-coordinate to 0.0
            "-Y","1.57",
        ]
    )


    return LaunchDescription([
        
        gazebo_server,
        gazebo_client,
        diff_state_publisher,
        spawn_diffdrive,
        rviz2,
    ])