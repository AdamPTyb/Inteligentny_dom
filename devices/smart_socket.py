from devices.device import Device
from interfaces.switchable import Switchable


class SmartSocket(Device, Switchable):

    def __init__(self, device_id, name, room, power_usage=0):
        super().init(device_id, name, room)
        self.power_usage = power_usage

    def turn_on(self):
        self._status = "ON"

    def turn_off(self):
        self._status = "OFF"

    def get_details(self):
        return (
            f"Socket: {self._name} | "
            f"Room: {self._room} | "
            f"Status: {self._status} | "
            f"Power usage: {self.power_usage}W"
        )