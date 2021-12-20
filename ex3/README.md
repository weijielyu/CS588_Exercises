# Challenge 3: SLAM or Odometry

Either use an existing visual slam package or an existing visual odometry package to
recover a representation of vehicle movement in the back lot (this is challenging!).

## Usage

We used the [hector slam package](http://wiki.ros.org/hector_slam/Tutorials/MappingUsingLoggedData). You can install it with
```
sudo apt-get install ros-indigo-hector-slam
```
or you can directly clone the github repository
``` 
git clone https://github.com/tu-darmstadt-ros-pkg/hector_slam.git
```
Then compile it in your workspace with `catkin_make`
 
Open two terminals. In the first terminal, launch hector slam

```
source devel/setup.bash
roslaunch hector_slam_launch tutorial.launch
```

In the second terminal, play the prerecorded rosbag (You can download it [here](http://luthuli.cs.uiuc.edu/~daf/courses/MAAV-2019/Mapping/data.bag))

```
rosbag play data.bag /lidar1/scan:=/scan --clock -r 1.8
```

To record your own rosbag, launch basic sensor in one terminal
```
roslaunch basic_launch gnss_sensor_init.launch
```
and record rosbag in another terminal with
```
rosbag record -O data.bag /SELECTED/TOPICS (/lidar1/scan, etc.)
```

## Demo

[![Exercise3](https://img.youtube.com/vi/bpT51nt85EQ/0.jpg)](https://www.youtube.com/watch?v=bpT51nt85EQ)
