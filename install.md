# HID Injection Detection PoC

**A safe, benign Proof of Concept payload for testing HID (Human Interface Device) injection detection in SOC, EDR, and HIDS environments.**

This payload simulates realistic Rubber Ducky / BadUSB-style keyboard injection attacks across Windows, macOS, and Linux — without performing any destructive, exfiltrating, or persistent actions.

## Purpose

- Trigger behavioral and HID-injection detection logic in your security stack.
- Validate that your SOC pipeline can detect rapid keystroke injection and suspicious shell activity.
- Provide a reliable, repeatable test case with a clear, greppable marker for easy verification.

## Features

- **Cross-platform support**: Windows 11, macOS, and Debian-based Linux (Ubuntu/Kali).
- **Completely benign**: Only writes a single timestamped marker file to a temporary directory.
- **Realistic behavior**: Mimics real attack patterns (device enumeration → shell launch → command execution).
- **Built-in detection guidance**: Includes recommended detection hooks for your SIEM/EDR rules.
- **Well-documented**: Clear comments and safety boundaries.

## Installation Instructions

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/yourusername/hid-injection-poc.git
   cd hid-injection-poc
   -----

   2.  Choose your payload format
	•  Copy the content from payload.txt (or the README) into your HID device’s scripting tool.
	•  Supported tools:
		•  Hak5 Rubber Ducky → Use Duckyscript
		•  Flipper Zero → Use BadUSB mode
		•  Other programmable HID devices (Bash Bunny, etc.)
3.  Load the payload
	•  For Hak5 Rubber Ducky: python3 -m ducky payload.txt (or use the official web encoder).
	•  For Flipper Zero: Paste into the BadUSB script editor.
4.  Test safely
	•  Use a dedicated test virtual machine or isolated physical machine.
	•  Plug in the device and observe your EDR/SOC console for alerts.
	•  Check for the marker file after execution.
5.  Optional: Customize
	•  Edit delays in the payload for your target environment.
	•  Modify the marker string if you want unique test IDs.
What It Does (and Doesn’t)
Does:
•  Opens the native run/terminal interface (Win+R, Spotlight, Ctrl+Alt+T).
•  Executes a harmless command that creates a marker file containing HID_INJECTION_POC_DETECTED.
•  Uses realistic timing and keystroke behavior to test behavioral analytics.
Does NOT:
•  Delete, modify, or encrypt any files.
•  Escalate privileges or trigger UAC/sudo prompts.
•  Exfiltrate data or make network connections.
•  Create persistence (no scheduled tasks, cron jobs, etc.).
