#first download psutil-yourpythonversion.whl
import psutil
battery = psutil.sensors_battery()
plugged_in = battery.power_plugged
charging_percentage = battery.percent
print(plugged_in)
print(charging_percentage)
