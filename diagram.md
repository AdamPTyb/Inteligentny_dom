## Diagram UML

```mermaid
classDiagram

class Device {
    -__device_id
    -__name
    -__room
    -__status
    +get_status()
    +change_status()
    +get_details()
}

class Switchable {
    <<interface>>
    +turn_on()
    +turn_off()
}

class Adjustable {
    <<interface>>
    +set_value()
}

class SmartSocket {
    -power_usage
    +turn_on()
    +turn_off()
    +get_details()
}

class AirConditioner {
    -temperature
    +turn_on()
    +turn_off()
    +set_value()
    +get_details()
}

class Camera {
    -recording
    +start_recording()
    +stop_recording()
    +get_details()
}

class SmartHome {
    -devices
    +add_device()
    +remove_device()
    +find_device()
    +show_all_devices()
}

Device <|-- SmartSocket
Device <|-- AirConditioner
Device <|-- Camera

Switchable <|.. SmartSocket
Switchable <|.. AirConditioner

Adjustable <|.. AirConditioner