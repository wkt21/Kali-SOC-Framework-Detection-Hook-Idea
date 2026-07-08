These are the foundational libraries for most HID projects:
•  Keyboard.h — Emulates a keyboard (press, release, write strings, modifiers).
•  Mouse.h — Emulates a mouse (move, click, scroll).
•  HID.h — Base library for raw HID reports (advanced use).
Supported Boards:
•  ATmega32U4-based: Arduino Leonardo, Pro Micro, Micro — best native support.
•  ESP32-S2/S3: Excellent USB OTG support via TinyUSB.
•  RP2040 (Pico): Good support.
•  SAMD21 (e.g., Arduino Zero): Works with some tweaks.
