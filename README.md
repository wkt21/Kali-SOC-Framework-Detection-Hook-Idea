# Kali‑SOC‑Framework‑Detection‑Hook‑Idea  
### Test the Kali CLI Framework  

<img width="1536" height="1024" alt="Kali SOC Framework Banner" src="https://github.com/user-attachments/assets/a19d8d23-fa90-4d7c-92ca-5b133b82b0d7" />

---

## 🔐 Overview

**A safe, benign HID‑Injection Proof of Concept for SOC, EDR, and HIDS testing.**  
This project simulates realistic **Rubber Ducky / BadUSB‑style keyboard injection attacks** across **Windows**, **macOS**, and **Linux** — without any destructive, exfiltration, or persistence actions.

---

## 🎯 Purpose

- Trigger behavioral HID‑injection detection logic in your security stack.  
- Help SOC teams tune and validate detection rules for keystroke injection attacks.  
- Provide a reliable, repeatable test case with a clear greppable marker.

---

## ⚙️ Features

- **Cross‑platform:** Windows 11, macOS, Debian Linux (Ubuntu/Kali).  
- Uses only **native OS commands** (no PowerShell on Windows).  
- Includes **DuckyScript → Arduino converter** (DuckyScript 3.0 support).  
- Detailed **detection rules and hunting queries**.  
- **Benign by design** — creates one small timestamped marker file.

---

# 🧠 Detection Rules & Hunting

**Key Hooks**

- Abnormally fast keystroke injection (near‑zero inter‑key latency).  
- New HID device enumeration followed by immediate **Win+R / Spotlight / Ctrl+Alt+T**.  
- File creation in temp directories containing `HID_INJECTION_POC_DETECTED`.  
- Rapid shell execution after USB HID activity.

> See full rules in `Detection‑Rules.md` (add this file if needed).

---

# 🔵 Visual Detection‑Flow Diagram (SOC Pipeline)

A high‑level view of how a HID‑injection event moves through a SOC detection pipeline:



            [ USB HID Device Plugged In ]
                         │
                         ▼
            [ OS Enumerates New HID Device ]
                         │
                         ▼
    [ Immediate High-Speed Keystroke Injection Detected ]
                         │
                         ▼
    [ Shell / Launcher Opened (Win+R, Spotlight, Terminal) ]
                         │
                         ▼
    [ Marker File Created: HID_INJECTION_POC_DETECTED ]
                         │
                         ▼
    [ EDR Telemetry → Sysmon → OSQuery → Auditd ]
                         │
                         ▼
            [ SIEM Correlation & Rule Matching ]
                         │
                         ▼
                [ Alert Generated for SOC ]
                         │
                         ▼
            [ Analyst Triage & Investigation ]



---

# 🧩 SOC Rule‑Mapping Table

A structured mapping of behaviors → telemetry → detection logic.

| HID Behavior | OS Signal | EDR / HIDS Telemetry | SIEM Fields | Recommended Detection Logic |
|-------------|-----------|-----------------------|-------------|------------------------------|
| New HID device enumerated | USB device add event | DeviceClass=HID | `DeviceType`, `VendorID`, `ProductID` | Alert on HID + immediate shell execution |
| Near‑zero latency keystrokes | Input event burst | Keypress timestamps | `EventLatency`, `InputBurst` | Detect >20 keys in <1 second |
| Win+R / Spotlight / Terminal auto‑launch | Process creation | `ProcessCreate` | `ParentProcess`, `CommandLine` | HID device → launcher within 1s |
| Marker file creation | File write event | `FileCreate` | `FilePath`, `FileName` | Detect file containing `HID_INJECTION_POC_DETECTED` |
| Rapid shell execution | Process chain | `ProcessTree` | `ChildProcess`, `ExecutionChain` | HID device → shell → command execution |
| DuckyScript‑style patterns | Input sequence | `KeystrokePattern` | `InputSequence` | Pattern match common injection sequences |

---

# 🔻 HID Injection Timeline (High‑Level SOC View)



┌──────────────────────────────────────────────────────────────┐ │                     HID INJECTION TIMELINE                    │ └──────────────────────────────────────────────────────────────┘

[ 0.0s ]  USB HID Device Plugged In • OS enumerates new keyboard-class device • VendorID/ProductID logged • EDR/HIDS records device-add event

[ 0.1s ]  HID Device Identified as “Keyboard” • Input subsystem activates • No user presence detected (optional heuristic) • HID → Input pipeline opens

[ 0.2s ]  High-Speed Keystroke Burst Begins • Near-zero latency between key events • >20 keys in <1 second (non-human pattern) • EDR flags anomalous input rate

[ 0.3s ]  Launcher Triggered • Windows: Win+R • macOS: Spotlight (Cmd+Space) • Linux: Ctrl+Alt+T • ProcessCreate telemetry fires

[ 0.4s ]  Shell / Terminal Opens • cmd.exe / powershell.exe / bash / zsh • Parent process = HID input event • EDR logs suspicious parent-child chain

[ 0.5s ]  Payload Execution • Benign marker file created: HID_INJECTION_POC_DETECTED_.txt • FileCreate telemetry fires

[ 0.6s ]  Post-Execution Idle • HID device stops typing • No persistence, no exfiltration • SOC correlation begins

[ 1.0s+ ] SIEM Correlation & Alerting • HID device + high-speed input + shell launch • Marker file creation • Rule match → SOC alert generated

[ Analyst Stage ] Investigation & Triage • Validate HID injection pattern • Confirm benign POC marker • Tune detection rules if needed


---

## 🧩 Supported Hardware

- Hak5 USB Rubber Ducky  
- Flipper Zero (BadUSB)  
- O.MG Cable  
- Arduino Leonardo / Pro Micro / ESP32‑S3  
- Custom boards via converter

---

## ⚠️ Safety & Legal

For **authorized testing only**.  
Use exclusively on systems you own or have explicit permission to test.  
Follow your organization’s security and compliance policies.

---

## 🤝 Contributing

Contributions are welcome!  
Ideas include:
- Additional OS variants  
- Enhanced converter logic  
- Randomized payload generation  
- Expanded detection rule sets

---

## 🧰 Installation & Usage

```bash
git clone https://github.com/wkt21/Kali-SOC-Framework-Detection-Hook-Idea.git
cd Kali-SOC-Framework-Detection-Hook-Idea

---

# Audience

Made for SOC Teams, Purple Teams, Detection Engineers, and Red Teamers.
⭐ Star this repo if it helps your detection engineering efforts!
