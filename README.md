# Kali-SOC-Framework-Detection-Hook-Idea
Test The Kali CLI Framework 
---
<img width="1536" height="1024" alt="IMG_1983" src="https://github.com/user-attachments/assets/a19d8d23-fa90-4d7c-92ca-5b133b82b0d7" />

---
# Detection Hook Ideas
•  Monitor for abnormally fast keystroke injection (near-zero inter-key latency).
•  Correlate new HID device enumeration events with immediate Win+R / Spotlight / Ctrl+Alt+T usage.
•  Watch for file creation in %TEMP% or /tmp/ containing the string HID_INJECTION_POC_DETECTED.
•  Alert on rapid shell execution immediately following USB HID device activity.
Usage

1.  Load the payload onto your HID injection device (e.g., Hak5 Rubber Ducky, Flipper Zero, etc.).
2.  Plug the device into a test system.
3.  Verify the marker file was created:
	•  Windows: %TEMP%\hid_poc_marker.txt
	•  macOS / Linux: /tmp/hid_poc_marker.txt
Compatibility Notes
•  Timing delays may need slight adjustment on very slow or heavily restricted systems.
•  Linux terminal shortcut (Ctrl+Alt+T) is optimized for GNOME-based desktops.
•  macOS Spotlight method works on most modern versions.
---

# Safety & Legal
This payload is intended only for authorized security testing on systems you own or have explicit permission to test. Always follow your organization’s red/purple team policies.
Contributing
Suggestions for additional OS variants, improved timing logic, randomized markers, or integration into larger testing frameworks are welcome.
---

# Made for SOC teams, purple teams, and detection engineers.
