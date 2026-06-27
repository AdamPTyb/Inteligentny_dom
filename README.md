# Projekt zaliczeniowy z Programowania Obiektowego wykonany w języku Python

## Opis projektu

Aplikacja symuluje system inteligentnego domu umożliwiający zarządzanie urządzeniami.

---

# Zadanie A – Implementacja modelu obiektowego

## Program pozwala:

* dodawać urządzenia,
* wyświetlać ich status,
* włączać urządzenia,
* zmieniać ustawienia,
* symulować działanie inteligentnego domu.

## Zastosowane elementy OOP

W projekcie wykorzystano:

* klasy i obiekty,
* dziedziczenie,
* klasy abstrakcyjne,
* interfejsy,
* enkapsulację,
* polimorfizm.

---

# Zadanie B – Rozszerzenie funkcjonalności projektu

W drugiej części projektu aplikacja została rozbudowana o:

* interfejs graficzny użytkownika (GUI) wykonany z wykorzystaniem biblioteki **Tkinter**,
* monitor urządzeń prezentujący aktualny stan systemu,
* wyświetlanie informacji o urządzeniach w oknie aplikacji,
* możliwość sterowania urządzeniami za pomocą przycisków,
* zapis stanu urządzeń do pliku **JSON**,
* odczyt stanu urządzeń z pliku **JSON**,
* obsługę wyjątków z prezentacją komunikatów o błędach,
* możliwość włączania wszystkich urządzeń obsługujących interfejs **Switchable**,
* możliwość uruchamiania i zatrzymywania nagrywania kamery,
* prezentację statusu wykonywanych operacji na monitorze aplikacji.

---

## Struktura projektu

```text
devices/
│
├── device.py
├── smart_socket.py
├── air_conditioner.py
├── camera.py
└── smart_home.py

interfaces/
│
├── switchable.py
└── adjustable.py

services/
│
└── file_manager.py

gui.py
main.py
devices.json
diagram.md
README.md
```

---

## Technologie

* Python 3.14
* Tkinter
* JSON
* PyCharm
* Git
* GitHub

---

## Autor

**Adam Tyburski**
