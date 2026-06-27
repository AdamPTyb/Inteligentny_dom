import json

from devices.smart_socket import SmartSocket
from devices.air_conditioner import AirConditioner
from devices.camera import Camera

class FileManager:

    @staticmethod
    def save_devices(devices, filename):

        data = []

        for device in devices:

            data.append({
                "type": device.__class__.__name__,
                "name": device._name,
                "room": device._room,
                "status": device._status,
                "power_usage": getattr(device, "power_usage", None),
                "temperature": getattr(device, "temperature", None),
                "recording": getattr(device, "recording", None)
            })

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)


    @staticmethod
    def load_devices(filename):

        devices = []

        with open(filename, "r") as file:
            data = json.load(file)

            for item in data:

                if item["type"] == "SmartSocket":
                    device = SmartSocket(
                        "loaded",
                        item["name"],
                        item["room"],
                        item["power_usage"]
                    )

                elif item["type"] == "AirConditioner":
                    device = AirConditioner(
                        "loaded",
                        item["name"],
                        item["room"],
                        item["temperature"]
                    )

                elif item["type"] == "Camera":
                    device = Camera(
                        "loaded",
                        item["name"],
                        item["room"]
                    )

                    device.recording = item["recording"]

                else:
                    continue

                device.change_status(item["status"])

                devices.append(device)

            return devices




