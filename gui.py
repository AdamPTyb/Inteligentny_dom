import tkinter as tk

from devices.smart_home import SmartHome
from devices.smart_socket import SmartSocket
from devices.air_conditioner import AirConditioner
from devices.camera import Camera

from services.file_manager import FileManager

# Dom i urządzenia

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

# Funkcje

def update_display(status_message="Ready"):

    text = ""

    for device in home.devices:
        text += device.get_details()
        text += "\n\n"

    text += "----------------------------------\n\n"
    text += "STATUS:\n\n"
    text += status_message
    text += "\n\n"
    text += "----------------------------------\n\n"

    result_label.config(text=text)


def show_devices():

    update_display("Devices displayed successfully.")


def save_devices():

    FileManager.save_devices(
        home.devices,
        "devices.json"
    )

    update_display("Devices saved successfully.")


def load_devices():

    home.devices = FileManager.load_devices(
        "devices.json"
    )

    update_display("Devices loaded successfully.")


def turn_on_devices():

    home.turn_on_all_switchable()

    update_display("All switchable devices turned ON.")

def camera_recording():

    for device in home.devices:

        if isinstance(device, Camera):

            if device.recording:

                device.stop_recording()
                update_display("Camera recording stopped.")

            else:

                device.start_recording()
                update_display("Camera recording started.")

            break


def test_exception():

    try:
        air.set_value(50)

    except ValueError as e:

        update_display(f"ERROR:\n{e}")

# GUI

root = tk.Tk()

root.title("Smart Home")
root.geometry("700x800")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Smart Home Management System",
    font = ("Helvetica", 18, "bold")
)

title_label.pack(pady=20)

show_button = tk.Button(
    root,
    text="Show Devices",
    command=show_devices,
    width=20
)

show_button.pack(pady=5)

save_button = tk.Button(
    root,
    text="Save Devices",
    command=save_devices,
    width=20
)

save_button.pack(pady=5)

load_button = tk.Button(
    root,
    text="Load Devices",
    command=load_devices,
    width=20
)

load_button.pack(pady=5)

turn_on_button = tk.Button(
    root,
    text="Turn On All",
    command=turn_on_devices,
    width=20
)

turn_on_button.pack(pady=5)

camera_button = tk.Button(
    root,
    text="Camera",
    command=camera_recording,
    width=20
)

camera_button.pack(pady=5)

error_button = tk.Button(
    root,
    text="Test Exception",
    command=test_exception,
    width=20
)

error_button.pack(pady=5)

# Wyświetlacz

display_title = tk.Label(
    root,
    text="Device Monitor",
    font=("Helvetica", 12, "bold")
)

display_title.pack(pady=(20, 5))

result_frame = tk.Frame(
    root,
    bg="#1e1e1e",
    bd=3,
    relief="sunken"
)

result_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

result_label = tk.Label(
    result_frame,
    text="Click 'Show Devices' to display devices.",
    bg="#1e1e1e",
    fg="lightgreen",
    font=("Consolas", 11),
    justify="center",
    anchor="center"
)

result_label.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=15
)

root.mainloop()