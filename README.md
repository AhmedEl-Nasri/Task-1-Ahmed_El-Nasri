Markdown
# Project 1: 6-DOF Industrial Manipulator Kinematics & Path Planning
**Industrial Training Kit | Powered by DecodeLabs**

An industrial-grade ROS 2 package designed to program a simulated 6-axis robotic manipulator arm to execute smooth, coordinate-accurate trajectories from Point A to Point B within a dynamic 3D workspace environment while maintaining rigid safety parameters.

## Features
- **Kinematic Logic:** Analytical Inverse Kinematics (IK) matrix solver translating raw Cartesian 3D space targets (XYZ) into joint angle states ($\theta_1$ through $\theta_6$).
- **Obstacle Deflection Field:** Look-ahead distance monitoring pipeline to dynamically evaluate collision zones and safely reject invalid trajectories.
- **Physics Simulation Ready:** Designed to communicate structural constraints through ROS 2 topics to visualization tools like RViz and Gazebo.
- **Modular Compilation:** Built following the `ament_python` specifications to ensure seamless workspace builds using `colcon`.

## Tech Stack
- **Core Runtime:** ROS 2 Humble Hawksbill / Python 3.10+
- **Mathematical Libraries:** `math`, `numpy`
- **Middleware Interfaces:** `rclpy` (ROS 2 Client Library)
- **Data Communication Messages:** `sensor_msgs/msg/JointState`, `geometry_msgs/msg/Point`

## Quick Start

### Prerequisites
- ROS 2 Humble Desktop installation
- Python setuptools & colcon build tools

### Setup and Compilation
1. **Clone the Repository** into your ROS 2 workspace src folder:
   ```bash
   cd ~/ros2_ws/src
   git clone [https://github.com/your-username/decode-labs-robotics-project1.git](https://github.com/your-username/decode-labs-robotics-project1.git)

### Install Dependencies:

```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
Build the Package:

```bash
colcon build --packages-select my_robot_arm_package
source install/setup.bash
Launch the Controller Node:

```bash
ros2 run my_robot_arm_package ik_controller
Repository Structure
Plaintext
my_robot_arm_package/
├── package.xml                 # ROS 2 XML structural package dependencies
├── setup.py                    # Build script and console entry point mapping
├── urdf/
│   └── industrial_arm.urdf     # Structural 3D robot model properties & joint parameters
└── my_robot_arm_package/
    ├── __init__.py
    └── ik_trajectory_node.py   # Core analytical kinematics and math engine script

### Architecture Overview
The URDF Structure (urdf/): Contains the physical parameters of the industrial arm, including link cylinder/box properties, fixed anchor transforms, joint rotation axes limits, and specific tool center flange frames.

The Kinematics Node (my_robot_arm_package/): Listens for inputs on the /arm_target_pose topic, applies trigonometry and inverse trigonometric functions to find appropriate joint limits, and outputs the calculated joint vectors over /joint_states.

Data Pipeline Parameters
Targeted Input Topic
Topic: /arm_target_pose

Message Type: geometry_msgs/msg/Point

Example Payload Structure:

JSON
{
  "x": 0.45,
  "y": 0.20,
  "z": 0.55
}
Calculated Outgoing Matrix
Topic: /joint_states

Message Type: sensor_msgs/msg/JointState

Output Array Map: Returns positions for ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6'] in radians.

#### Developer Checklist
[ ] The .urdf geometry configuration is verified free of syntax errors.

[ ] Kinematics equation handling intercepts math domain exceptions to prevent node crashes.

[ ] Target coordinates falling within the defined obstacle radius trigger safety warnings.

[ ] The setup.py console script entry point matches node path locations perfectly.
