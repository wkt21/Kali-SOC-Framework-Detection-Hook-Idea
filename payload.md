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

## What It Does (and Doesn't)

**Does:**
- Opens the native run/terminal interface (Win+R, Spotlight, Ctrl+Alt+T).
- Executes a harmless command that creates a marker file containing `HID_INJECTION_POC_DETECTED`.
- Uses realistic timing and keystroke behavior to test behavioral analytics.

**Does NOT:**
- Delete, modify, or encrypt any files.
- Escalate privileges or trigger UAC/sudo prompts.
- Exfiltrate data or make network connections.
- Create persistence (no scheduled tasks, cron jobs, etc.).

## Payload (DuckyScript / Hak5-style)

```duckyscript
REM ################################################################
REM PAYLOAD NAME: Benign HID Injection Detection PoC
REM PURPOSE: Trigger behavioral/HID-injection detection logic only.
REM TARGETS: Windows 11, macOS, Debian Linux
REM ################################################################

DELAY 1000

REM ----------------------------------------------------------------
REM WINDOWS 11
REM ----------------------------------------------------------------
IF ($_OS == WINDOWS) THEN
    GUI r
    DELAY 300
    STRING powershell -NoProfile -Command "Set-Content -Path \"$env:TEMP\hid_poc_marker.txt\" -Value ('HID_INJECTION_POC_DETECTED ' + (Get-Date -Format o))"
    ENTER
END_IF

REM ----------------------------------------------------------------
REM MACOS
REM ----------------------------------------------------------------
IF ($_OS == OSX) THEN
    GUI SPACE
    DELAY 300
    STRING Terminal
    ENTER
    DELAY 500
    STRING echo "HID_INJECTION_POC_DETECTED $(date -u +%Y-%m-%dT%H:%M:%SZ)" > /tmp/hid_poc_marker.txt
    ENTER
END_IF

REM ----------------------------------------------------------------
REM DEBIAN LINUX
REM ----------------------------------------------------------------
IF ($_OS == LINUX) THEN
    CTRL ALT t
    DELAY 500
    STRING echo "HID_INJECTION_POC_DETECTED $(date -u +%Y-%m-%dT%H:%M:%SZ)" > /tmp/hid_poc_marker.txt
    ENTER
END_IF
