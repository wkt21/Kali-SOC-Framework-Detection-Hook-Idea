# Kali-SOC-Framework-Detection-Hook-Idea
Test The Kali CLI Framework 
---
<img width="1536" height="1024" alt="IMG_1983" src="https://github.com/user-attachments/assets/a19d8d23-fa90-4d7c-92ca-5b133b82b0d7" />

---

**A safe, benign HID Injection Proof of Concept for SOC, EDR, and HIDS testing.**

# This project simulates realistic Rubber Ducky / BadUSB-style keyboard injection attacks across Windows, macOS, and Linux — without any destructive, exfiltration, or persistence actions.

---

## Purpose

- Trigger behavioral HID-injection detection logic in your security stack.
- Help SOC teams tune and validate detection rules for keystroke injection attacks.
- Provide a reliable, repeatable test case with a clear greppable marker.

## Features

- Cross-platform: **Windows 11**, **macOS**, **Debian Linux** (Ubuntu/Kali).
- Uses only native OS commands (no PowerShell on Windows).
- Includes DuckyScript → Arduino converter (DuckyScript 3.0 support).
- Detailed detection rules and hunting queries.
- Benign by design — creates one small timestamped marker file.
---
# Detection Rules & Hunting
Key Hooks:
•  Abnormally fast keystroke injection (near-zero inter-key latency).
•  New HID device enumeration + immediate Win+R / Spotlight / Ctrl+Alt+T.
•  File creation in temp directories containing HID_INJECTION_POC_DETECTED.
•  Rapid shell execution after USB HID activity.
---
# See full rules in Detection-Rules.md (add this file if needed).
Supported Hardware

•  Hak5 USB Rubber Ducky
•  Flipper Zero (BadUSB)
•  O.MG Cable
•  Arduino Leonardo / Pro Micro / ESP32-S3
•  Custom boards via converter
---
# Safety & Legal
For authorized testing only. Use exclusively on systems you own or have explicit permission to test. Follow your organization’s policies.
Contributing
Welcome! Ideas: more OS variants, enhanced converter, randomized payloads, additional detection rules.
---
# Made for SOC teams, Purple Teams, Detection Engineers, and Red Teamers.
⭐ Star this repo if it helps your detection engineering efforts!
---
## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/wkt21/Kali-SOC-Framework-Detection-Hook-Idea.git
   cd Kali-SOC-Framework-Detection-Hook-Idea
