from launch import LaunchDescription
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution 

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare, FindPackagePrefix


def generate_launch_description():
    
    record_path = PathJoinSubstitution(
        [
            FindPackagePrefix("imu_utils"),
            "..",
            "src",
            "imu_utils",
            "data"
        ]
    )
    
    return LaunchDescription([
        Node(
            package='imu_utils',
            executable='imu_an',
            name='imu_an',
            output='screen',
            parameters=[
                {'imu_topic': '/djiros/imu'},
                {'imu_name': 'N3'},
                {'data_save_path': record_path},
                {'max_time_min': 120},
                {'max_cluster': 100},
            ]
        ),
    ])