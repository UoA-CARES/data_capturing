# data_capturing
Package for capturing data of canopies moving sensor manually

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Base package dependencies

```
1) Ubuntu 20.04 - ROS Noetic - requires python 3 support

2) Pull master version of cares_lib_ros
   a) cd ~/catkin_ws/src
   b) git clone https://github.com/UoA-CARES/cares_lib_ros.git

3) Pull master version of the sensor, for example here is pylon_cameras
   a) cd ~/catkin_ws/src
   b) git clone https://github.com/UoA-CARES/pylon_camera.git

```

### Installing
A step by step series of examples that tell you how to get a development env running

Clone the package into the catkin directory you are using, presumed here to be "~/catkin_ws"

```
cd ~/catkin_ws/src
git clone https://github.com/UoA-CARES/data_capturing.git
```

Build the package with catkin_make in the source directory

```
cd ~/catkin_src/
catkin_make
```

## Preparing to Run
The capturing code will record all the sensor data at ~/canopy_scans/date-format-directory. You need to move the sensors manually.


## How to Run
1. Run the sensors, for example using Basler cameras:
```
roslaunch pylon_camera pylon_camera_node.launch
```
2. Run the capturing code:

Once the platform you are using is setup we can run the capturing code.
```
roslaunch data_capturing scan.launch
```
