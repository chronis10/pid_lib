# Description
A simple PID controller library in Python, suitable for robotics applications. 

Instructions
===
Place the PID_lib.py in the same directory with your main script.
```python
 Import PID_lib()
 # PID(KP,KI,KD) parameters
 motor1_pid = PID(1,0.5,0.2,0.1)
 
while True:
  .... 
  sensor_readings = .....
  # desired_value,actual_value
  motor_speed = motor1_pid.pid_calc(90,sensor_readings)
  set_motor(motor_speed)
  ....
```
