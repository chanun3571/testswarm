ROS1 Noetic
#launch gazebo with 3 robot
roslaunch arobota2 gazebo_multi.launch
#launch robot navigation/movebase/amcl
roslaunch navigation_gazebo_multi.launch
#launch formation control algorithm+joystick input
roslaunch formation_control_auto.launch
