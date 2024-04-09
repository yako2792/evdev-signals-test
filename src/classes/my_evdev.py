import evdev
from tools.colors import *

class periferals:
    def __init__(self):
        self.test_param = None
    
    def list_periferals(self):
        '''
        Show available periferals
        '''
        print(f"\n{cyan}<------ (METHOD){reset} List Periferals - START {cyan}------>{reset}\n")
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        device_num = 1
        for device in devices:
            print()
            print(f">> Device {device_num}")
            print(f"Path: {device.path}")
            print(f"Name: {device.name}")
            print(f"Phys: {device.phys}")
            print()
            device_num+=1

        print(f"\n{cyan}<------ (METHOD){reset} List Periferals - FINISH {cyan}------>{reset}\n")