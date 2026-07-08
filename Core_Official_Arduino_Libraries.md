These are the foundational libraries for most HID projects:
•  Keyboard.h — Emulates a keyboard (press, release, write strings, modifiers).
•  Mouse.h — Emulates a mouse (move, click, scroll).
•  HID.h — Base library for raw HID reports (advanced use).
Supported Boards:
•  ATmega32U4-based: Arduino Leonardo, Pro Micro, Micro — best native support.
•  ESP32-S2/S3: Excellent USB OTG support via TinyUSB.
•  RP2040 (Pico): Good support.
•  SAMD21 (e.g., Arduino Zero): Works with some tweaks.

---
# c++
#include <Keyboard.h>

void setup() {
  Keyboard.begin();
  delay(1000);  // Wait for enumeration
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  Keyboard.releaseAll();
  delay(500);
  Keyboard.print("notepad");
  Keyboard.press(KEY_RETURN);
  Keyboard.releaseAll();
}

void loop() {}
---
1.  For Quick PoC Prototyping — Use Pro Micro (cheap, ~$5–10) + official 2.Keyboard.h / Mouse.h.
3.  For Advanced / Wireless — ESP32-S3 boards (LilyGo T-Dongle, etc.) + HIDForge or EvilDuck.
4.  For Maximum Compatibility — Stick with ATmega32U4 boards and NicoHood’s library for extended features.
5.  DuckyScript Support — Several projects (EvilDuck, custom parsers) let you run your existing DuckyScript payloads directly on Arduino hardware.
Integration Ideas for Your SOC Framework
•  Build a custom Arduino-based test device that runs your native-command payload.
•  Add layout support (US, ES, DE, etc.) using adapted libraries like ArduIgnoES.
•  Create detection test variants with randomized delays or mouse movements to test behavioral analytics.
