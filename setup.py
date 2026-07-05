from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_robot_arm_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ahmed El-Nasri',
    maintainer_email='student@university.edu',
    description='Industrial 6-DOF Robot Arm Kinematics and Trajectory Simulation Package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ik_controller = my_robot_arm_package.ik_trajectory_node:main'
        ],
    },
)