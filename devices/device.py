from abc import ABC, abstractmethod


class Device(ABC):

    def init(self, device_id, name, room):

        if not device_id:
            raise ValueError("Device ID cannot be empty")

        if not name:
            raise ValueError("Device name cannot be empty")

        self._device_id = device_id
        self._name = name
        self._room = room
        self._status = "OFF"

    def get_status(self):
        return self._status

    def change_status(self, new_status):
        self._status = new_status

    @abstractmethod
    def get_details(self):
        pass