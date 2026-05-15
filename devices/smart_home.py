from interfaces.switchable import Switchable


class SmartHome:

    def __init__(self, home_name):
        self.home_name = home_name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device_id):

        self.devices = [
            d for d in self.devices
            if d._device_id != device_id
        ]

    def find_device(self, device_id):

        for d in self.devices:

            if d._device_id == device_id:
                return d

        return None

    def show_all_devices(self):

        print("\n===== DEVICE STATUS =====")

        for device in self.devices:
            print(device.get_details())

    def turn_on_all_switchable(self):

        for device in self.devices:

            if isinstance(device, Switchable):
                device.turn_on()