# Diagram klas - Inteligentny Dom

## Relacje klas

```text
                +-------------------+
                |      Device       |
                +-------------------+
                | - __device_id     |
                | - __name          |
                | - __room          |
                | - __status        |
                +-------------------+
                | + get_status()    |
                | + change_status() |
                | + get_details()   |
                +-------------------+
                          ^
        -----------------------------------------
        |                   |                  |
        |                   |                  |
+----------------+  +----------------+  +----------------+
|  SmartSocket   |  | AirConditioner |  |     Camera     |
+----------------+  +----------------+  +----------------+
| - power_usage  |  | - temperature  |  | - recording    |
+----------------+  +----------------+  +----------------+
| + turn_on()    |  | + turn_on()    |  | + start_record |
| + turn_off()   |  | + turn_off()   |  | + stop_record  |
| + get_details()|  | + set_value()  |  | + get_details()|
+----------------+  | + get_details()|
                    +----------------+

        +----------------+
        |   Switchable   |
        +----------------+
        | + turn_on()    |
        | + turn_off()   |
        +----------------+

        +----------------+
        |   Adjustable   |
        +----------------+
        | + set_value()  |
        +----------------+

                +----------------+
                |   SmartHome    |
                +----------------+
                | - devices      |
                +----------------+
                | + add_device() |
                | + remove_device() |
                | + find_device() |
                | + show_all_devices() |
                +----------------+
```

## Opis diagramu

- `Device` jest klasą bazową abstrakcyjną.
- `SmartSocket`, `AirConditioner` i `Camera` dziedziczą po klasie `Device`.
- `Switchable` jest interfejsem dla urządzeń włączanych i wyłączanych.
- `Adjustable` jest interfejsem dla urządzeń z regulacją wartości.
- `SmartHome` zarządza wszystkimi urządzeniami.