# First run main code - It subscribes to " led_color " topic.
python3 led_ros_v2.py 

# Second - Publish a msg to 'led_color' topic with data "white", "red", "green", "blink".

 ros2 topic pub /led_color std_msgs/msg/String "data: 'white'"
 
 ros2 topic pub /led_color std_msgs/msg/String "data: 'red'"
 
 ros2 topic pub /led_color std_msgs/msg/String "data: 'green'"
 
 ros2 topic pub /led_color std_msgs/msg/String "data: 'blink'"


