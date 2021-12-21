# Challenge 4: GPS Scribbling

Use the codebase for GPS and waypoints which Hang Cui has kindly let us use ( gzipped tarfile) and your skill and judgement to cause the vehicle to follow a figure 8 path on the outdoor track.
Xiaoming Zhao will write a brief intro to this codebase (to be posted) which uses a PID controller to move to a sequence of waypoints.

## Usage

Launch joystick controller in the first terminal

```
source devel/setup.bash
roslaunch basic_launch dbw_joystick.launch
```

Launch basic sensor in the second terminal
```
source devel/setup.bash
roslaunch basic_launch gnss_sensor_init.launch
```

Run `gem_gnss_pp_tracker_pid.py` in another terminal. You need to `catkin_make` the workspace.

```
source devel/setup.bash
rosrun gem_gnss gem_gnss_pp_tracker_pid.py
```

You will see the car following a prerecorded track.

## Demo


[![Exercise3](https://img.youtube.com/vi/iHDAfXnXQkk/0.jpg)](https://www.youtube.com/watch?v=iHDAfXnXQkk)
