# Project 1: Robotic Arm Kinematics & Path Planning 🤖

## 🌟 Overview
This project is an advanced control package for a simulated 6-Degree-of-Freedom (6-DOF) industrial manipulator arm. The system bridges the gap between raw mathematical path computations and industrial robotic simulation, enabling precise, coordinate-accurate trajectories from Point A to Point B. By implementing mathematical inverse kinematics engines alongside dynamic spatial boundary checks, the architecture guarantees collision-free path execution inside complex 3D engineering environments.

## 🤖 Components

### 1. 6-DOF Manipulator Robot
A standard multi-axis industrial articulated robot configuration. Its kinematic profile features a heavy base anchor, rotating waist, pivoting shoulder, dynamic elbow, and a multi-axis wrist flange for ultimate tooling flexibility.

### 2. Kinematics Mathematical Node
The core computational engine of the project. It continuously runs analytical mathematical algorithms to convert target points instantly into direct angular parameters for the joint hardware links.

### 3. Obstacle Avoidance Guard
A proximity security routine that maps target vectors against virtual boundary spaces, serving as the system's defensive filter to halt movement prior to physical structural collisions.

### 4. Middleware Communication Loop
The message broker infrastructure built using standard ROS 2 message matrices (`sensor_msgs` and `geometry_msgs`) to stream command fields smoothly to visualization frames.

## ⚙️ Features
* **Planar & Spatial Trajectory Tracking:** Translates 3D workspace destination objectives into direct physical joint rotations ($\theta_1$ through $\theta_6$).
* **Look-Ahead Safety Intervention:** Monitors spatial distance metrics against environmental hazards to deny unsafe movements.
* **Middleware Package Architecture:** Fully integrated build framework designed for seamless ecosystem registration and execution.

## 🖥️ System Requirements

### Hardware / Environment Constraints
* **Industrial 6-Axis Kinematic Model:** Configured with physical workspace limitations and rotational boundary caps.
* **Dynamic Obstacle Array:** Simulated spatial zone representing physical perimeter structures.

### Software
* **ROS 2 Humble Hawksbill:** The primary framework runtime environment.
* **Python 3.10 or higher:** Core language platform for computational scripts.
* **Colcon Build System:** For package compilation and local environment installation.

## 📹 Deployment Output
Watch the simulation pipeline execution log for the trajectory system:

`[INFO] [ik_trajectory_node]: Industrial Kinematics Controller Activated.`  
`[INFO] [ik_trajectory_node]: Trajectory calculated successfully. Moving to Target...`
