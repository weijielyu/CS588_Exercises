import rospy 
from pacmod_msgs.msg import PacmodCmd

pub = rospy.Publisher('/pacmod/as_rx/turn_cmd', PacmodCmd, queue_size = 1)
rospy.init_node('SOS')
rate = rospy.Rate(2)
signal_list = [2,1,2,1,2,1,0,1,0,1,0,1,2,1,2,1,2,1,1,1]
i=0
while not rospy.is_shutdown():
    signal = signal_list[i]
    # sig = PacmodCmd()
    pub.publish(ui16_cmd=signal)
    i += 1
    if i == 20:
        i = 0
    rate.sleep()