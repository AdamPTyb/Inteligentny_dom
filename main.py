from devices.smart_home import SmartHome
from devices.smart_socket import SmartSocket
from devices.air_conditioner import AirConditioner
from devices.camera import Camera

from services.file_manager import FileManager


def main():

    home = SmartHome("Inteligentny Dom")

    socket = SmartSocket(
        "1",
        "Kitchen Socket",
        "Kitchen",
        120
    )

    air = AirConditioner(
        "2",
        "Bedroom AC",
        "Bedroom",
        21
    )

    camera = Camera(
        "3",
        "Front Door Camera",
        "Hall"
    )

    home.add_device(socket)
    home.add_device(air)
    home.add_device(camera)

    print("INITIAL STATUS:")
    home.show_all_devices()

    print("\nTurning on switchable devices...")
    home.turn_on_all_switchable()

    print("\nChanging temperature...")
    air.set_value(18)

    print("\nStarting camera...")
    camera.start_recording()

    print("\nFINAL STATUS:")
    home.show_all_devices()

    print("\nSaving devices to file...")

    FileManager.save_devices(
        home.devices,
        "devices.json"
    )

    print("Device saved.")

if __name__ == "__main__":
    main()