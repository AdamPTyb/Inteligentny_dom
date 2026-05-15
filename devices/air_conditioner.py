from devices.device import Device
from interfaces.switchable import Switchable
from interfaces.adjustable import Adjustable


class AirConditioner(Device, Switchable, Adjustable):

    def __init__(self, device_id, name, room, temperature=22):
        super().init(device_id, name, room)
        self.temperature = temperature

    def turn_on(self):
        self._status = "ON"

    def turn_off(self):
        self._status = "OFF"

    def set_value(self, value):
        self.temperature = value

    def get_details(self):
        return (
            f"AirConditioner: {self._name} | "
            f"Room: {self._room} | "
            f"Temperature: {self.temperature}°C | "
            f"Status: {self._status}"
        )