from devices.device import Device


class Camera(Device):

    def __init__(self, device_id, name, room):
        super().init(device_id, name, room)
        self.recording = False

    def start_recording(self):
        self.recording = True

    def stop_recording(self):
        self.recording = False

    def get_details(self):
        return (
            f"Camera: {self._name} | "
            f"Room: {self._room} | "
            f"Recording: {self.recording}"
        )