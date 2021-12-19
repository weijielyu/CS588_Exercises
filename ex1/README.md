# Challenge 1: Distressed Flashing

Under control of the computer, cause the vehicle to flash the SOS pattern on its turn indicator lights.
SOS in morse code is dot-dot-dot-dash-dash-dash-dot-dot-dot.
Map dot to the left turn indicator and dash to the right, and make the vehicle flash: left-left-left-right-right-right-left-left-left followed by a wait, then repeat.

## Usage

Open two terminals. In the first terminal, launch the joystick controller

```
source devel/setup.bash
roslaunch basic_launch dbw_joystick.launch
```

In the second terminal, directly run `SOS.py`

```
python SOS.py
```

## Demo


[![Exercise1](https://img.youtube.com/vi/Op26Rukw6bQ/0.jpg)](https://www.youtube.com/watch?v=Op26Rukw6bQ)
