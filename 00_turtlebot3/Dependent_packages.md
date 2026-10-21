
#### 원격 PC
##### 1. Install Dependent ROS2 Packages
```c
1. Install Gazebo
$ sudo apt install ros-humble-gazebo-*
2. Install Cartographer
$ sudo apt install ros-humble-cartographer
$ sudo apt install ros-humble-cartographer-ros
3. Install Nabiigation2
$ sudo apt install ros-humble-navigation2
$ sudo apt install ros-humble-nav2-bringup

```
##### 2. Install TurtleBot3 Packages
```c
$ source /opt/ros/humble/setup.bash
$ mkdir -p ~/turtlebot3_ws/src
$ cd ~/turtlebot3_ws/src/
$ git clone -b humble https://github.com/ROBOTIS-GIT/DynamixelSDK.git
$ git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
$ git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3.git
$ sudo apt install python3-colcon-common-extensions
$ cd ~/turtlebot3_ws
$ colcon build --symlink-install
$ echo 'source ~/turtlebot3_ws/install/setup.bash' >> ~/.bashrc
$ source ~/.bashrc
```
##### 3. Environment Configuration
```c
$ echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
$ echo 'source /usr/share/gazebo/setup.sh' >> ~/.bashrc
$ echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
$ source ~/.bashrc
```
