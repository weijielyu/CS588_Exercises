# Challenge 2: Detecting and Braking

Cause the vehicle to brake after detecting a person (answers in teams of no more than five, due early Nov; can be done!

## Usage

Open three terminals. In the first terminal, launch the joystick controller

```
source devel/setup.bash
roslaunch basic_launch dbw_joystick.launch
```

In the second terminal, launch the basic sensors 

```
source devel/setup.bash
roslaunch basic_launch gnss_sensor_init.launch
```

In the third terminal, directly run `brake.py`

```
python brake.py
```

## Reference

* Jocher, G., Stoken, A., Borovec, J., NanoCode012, ChristopherSTAN, Changyu, L., Laughing, tkianai, Hogan, A., lorenzomammana, yxNONG, AlexWang1900, Diaconu, L., Marc, wanghaoyang0106, ml5ah, Doug, Ingham, F., Frederik, … Rai, P. (2020). ultralytics/yolov5: v3.1 - Bug Fixes and Performance Improvements (v3.1) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.4154370

## Demo


[![Exercise2](https://img.youtube.com/vi/CsJtzJg5ByQ/0.jpg)](https://www.youtube.com/watch?v=CsJtzJg5ByQ)
