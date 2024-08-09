import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mobot/ROS2/workspace/src/ps5_controller/install/ps5_controller'
