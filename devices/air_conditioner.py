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

        if value < 16 or value > 30:
            raise ValueError(
                "Temperature change rejected."
                "\nCurrent temperature: 21°C"
                "\nAllowed range: 16-30°C"
            )

        self.temperature = value

    def get_details(self):
        return (
            f"AirConditioner: {self._name} | "
            f"Room: {self._room} | "
            f"Temperature: {self.temperature}°C | "
            f"Status: {self._status}"
        )