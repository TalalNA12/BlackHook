# BlackHook

**BlackHook** is a defensive cybersecurity lab project that safely simulates keylogger-like behavior and detects suspicious process and filesystem activity using Python.

This project was built for **Keylogger Simulation Analysis**, focusing on safe malware-behavior analysis, detection logic, and MITRE ATT&CK mapping.

---

## Project Objective

The objective of BlackHook is to analyze simulated input-capture behavior and build a Python-based detector that can identify suspicious keylogger-like indicators.

The project demonstrates:

- Static analysis of a simulated keylogger behavior script
- Dynamic analysis using Process Monitor and Process Explorer
- Buffer accumulation and log file writing behavior
- Python-based detection of suspicious process and file activity
- MITRE ATT&CK mapping to **T1056: Input Capture**

---

## Important Safety Notice

BlackHook is **not a real keylogger**.

The simulator does **not**:

- Capture real keyboard input
- Use keyboard hooks
- Use `pynput`
- Use the `keyboard` library
- Use `GetAsyncKeyState`
- Use `SetWindowsHookEx`
- Send data over the network
- Steal credentials or personal information

The simulator only writes predefined fake strings to a local log file for safe academic testing.

This project is for defensive cybersecurity education only.

---

## Project Structure

```text
BlackHook/
│
├── blackhook_detector.py
├── blackhook_simulator.py
├── requirements.txt
├── blackhook_trace.log
└── README.md

Recommended lab folder structure:

C:\BlackHookLab
│
├── logs
│   └── blackhook_trace.log
│
└── repo
    └── BlackHook
        ├── blackhook_detector.py
        ├── blackhook_simulator.py
        └── requirements.txt
Components
1. BlackHook Simulator

The simulator generates safe keylogger-like behavior by:

Selecting predefined fake input strings
Adding them to a temporary buffer
Flushing the buffer into a log file
Creating repeated suspicious-looking file write activity

Default log file path on Windows:

C:\BlackHookLab\logs\blackhook_trace.log

Example fake strings:

admin
test_login
student_portal
fake_credentials
comsats_demo
analysis_input
security_lab
hello_world
this_is_fake_data

These are hardcoded test strings and are not collected from the keyboard.

2. BlackHook Detector

The detector scans for suspicious indicators using:

Running process inspection
Process command-line analysis
Recently modified file detection
Suspicious filename keyword matching
Controlled lab directory scanning

It looks for indicators such as:

blackhook
hook
keylogger
keystroke
trace
log
capture

The detector scans the controlled lab directory:

C:\BlackHookLab

This helps reduce false positives and avoids scanning personal folders.

Requirements

Install dependencies using:

pip install -r requirements.txt

Required Python packages:

psutil
colorama
watchdog
tabulate
How to Run
Step 1: Clone the repository
git clone https://github.com/YOUR_USERNAME/BlackHook.git
cd BlackHook

Replace YOUR_USERNAME with your GitHub username.

Step 2: Install requirements
pip install -r requirements.txt
Step 3: Create the lab directory

On Windows, create:

C:\BlackHookLab\logs

The simulator writes its fake trace file here.

Step 4: Run the simulator
python blackhook_simulator.py

The simulator will generate fake input activity and write it to:

C:\BlackHookLab\logs\blackhook_trace.log
Step 5: Run the detector
python blackhook_detector.py

The detector will scan running processes and recently modified files, then print any suspicious indicators.

Dynamic Analysis

Dynamic analysis was performed using Process Monitor.

Recommended ProcMon filters:

Process Name is python.exe → Include
Path contains C:\BlackHookLab → Include

Important operations to observe:

CreateFile
WriteFile
ReadFile
CloseFile

These events show the simulator creating and writing to the trace log.

Static Analysis

Since BlackHook is Python-based, static analysis was performed at source-code level.

The analysis focused on:

Fake input list
Log file path
Buffer storage
Buffer flush function
File-writing behavior
Absence of real keyboard capture

Important simulator behavior:

Fake input generation → Buffer accumulation → File write → Log storage
MITRE ATT&CK Mapping

BlackHook maps to:

MITRE ATT&CK Technique: T1056 - Input Capture

The project simulates the behavior pattern of input capture by modeling:

Input-like data generation
Temporary buffer storage
Local log file writing
Repeated flush behavior

However, BlackHook does not perform actual input capture. It only uses predefined fake data for safe academic testing.

Results

BlackHook successfully demonstrated:

Safe keylogger-like behavior simulation
Log file creation
Buffer accumulation
File write and flush behavior
Process and filesystem monitoring
Python-based detection of suspicious indicators
MITRE mapping to T1056

The detector successfully identified the generated trace file:

C:\BlackHookLab\logs\blackhook_trace.log
Limitations

BlackHook is a basic academic detector and has some limitations:

It uses keyword-based detection, which can create false positives.
It does not inspect low-level Windows APIs.
It does not detect real keyboard hooks.
It does not perform deep file-content analysis.
It does not continuously monitor in real time unless extended later.

A future version could improve detection using:

Real-time filesystem monitoring with watchdog
Better scoring-based detection
File entropy/content analysis
Windows Event Log or Sysmon integration
YARA-style signature matching
Disclaimer

This project is for educational and defensive cybersecurity purposes only.

Do not use this project to capture real keystrokes, collect credentials, monitor users, or perform unauthorized activity.

BlackHook is designed only to simulate and detect keylogger-like behavior in a safe, controlled lab environment.

Portfolio Line

Analyzed simulated input-capture behavior using a safe Python-based keylogger simulation and built BlackHook, a detector for suspicious process and filesystem indicators mapped to MITRE ATT&CK T1056.
