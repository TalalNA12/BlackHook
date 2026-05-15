import psutil
from pathlib import Path
import os
import time
from datetime import datetime, timedelta
from colorama import Fore, Style, init

init(autoreset=True)

import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def slow_print(text, color=Fore.WHITE, delay=0.04, newline=True):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)

    if newline:
        sys.stdout.write("\n")
        sys.stdout.flush()


def loading_bar(label, color=Fore.RED, total=25, delay=0.07):
    sys.stdout.write(color + f"{label:<34} [" + Style.RESET_ALL)
    sys.stdout.flush()

    for _ in range(total):
        sys.stdout.write(color + "█" + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write(color + "] DONE\n" + Style.RESET_ALL)
    sys.stdout.flush()
    time.sleep(0.35)


def boot_sequence():
    clear_screen()

    slow_print(">> BLACKHOOK BOOT SEQUENCE STARTED", Fore.RED, 0.04)
    time.sleep(0.4)

    slow_print(">> Initializing defensive analysis core...", Fore.WHITE, 0.035)
    time.sleep(0.25)

    slow_print(">> Loading local process scanner...", Fore.WHITE, 0.035)
    time.sleep(0.25)

    slow_print(">> Loading filesystem trace module...", Fore.WHITE, 0.035)
    time.sleep(0.25)

    slow_print(">> Capture module: DISABLED", Fore.GREEN, 0.035)
    time.sleep(0.4)

    print()
    loading_bar("Process scanner", Fore.RED)
    loading_bar("Filesystem scanner", Fore.RED)
    loading_bar("Detection signatures", Fore.RED)
    loading_bar("Report generator", Fore.RED)

    time.sleep(0.8)


BANNER = r"""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝ ███████║██║   ██║██║   ██║█████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██╔══██║██║   ██║██║   ██║██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
"""


def display_banner():
    clear_screen()

    type_text("[BLACKHOOK] Initializing defensive analysis engine...", Fore.RED, 0.025)
    time.sleep(0.3)

    loading_bar("Loading process scanner      ", Fore.RED)
    loading_bar("Loading filesystem monitor   ", Fore.RED)
    loading_bar("Loading detection signatures ", Fore.RED)

    time.sleep(0.4)
    clear_screen()

    print(Fore.RED + BANNER + Style.RESET_ALL)

    print(Fore.WHITE + "╔══════════════════════════════════════════════════════════════════════════════╗")
    print(Fore.WHITE + "║                         BLACKHOOK DETECTOR                                   ║")
    print(Fore.WHITE + "║              Simulated Keylogger Behavior Analysis Engine                    ║")
    print(Fore.WHITE + "╠══════════════════════════════════════════════════════════════════════════════╣")
    print(Fore.WHITE + "║  Mode       : Defensive Lab Simulation                                       ║")
    print(Fore.WHITE + "║  Target     : Process + Filesystem Indicators                                ║")
    print(Fore.WHITE + "║  Capture    : Disabled. No real keystrokes are collected.                    ║")
    print(Fore.WHITE + "║  Objective  : Detect suspicious keylogger-like behavior.                     ║")
    print(Fore.WHITE + "╚══════════════════════════════════════════════════════════════════════════════╝")
    print()

    type_text(">> BlackHook is armed. Beginning scan sequence...", Fore.RED, 0.025)
    print()

def display_banner():
    print(BANNER)

SUSPICIOUS_PROCESS_KEYWORDS = [
    "keylogger",
    "keyboard",
    "hook",
    "keystroke",
    "pynput",
    "keys.log",
    "blackhook"
]

SUSPICIOUS_FILE_KEYWORDS = [
    "key",
    "keys",
    "log",
    "keystroke",
    "capture",
    "blackhook",
    "trace"
]

WATCH_DIRS = [
    Path.home() / "Desktop",
    Path.home() / "Documents",
    Path.home() / "Downloads",
    Path("C:/Users/Public"),
    Path("C:/Temp"),
    Path("C:/ProgramData")
]

WATCH_EXTENSIONS = [".txt", ".log", ".dat", ".json", ".cache"]


def scan_processes():
    findings = []

    for proc in psutil.process_iter(["pid", "name", "exe", "cmdline"]):
        try:
            name = proc.info.get("name") or ""
            exe = proc.info.get("exe") or ""
            cmdline = " ".join(proc.info.get("cmdline") or [])

            combined_text = f"{name} {exe} {cmdline}".lower()

            for keyword in SUSPICIOUS_PROCESS_KEYWORDS:
                if keyword in combined_text:
                    findings.append({
                        "type": "Suspicious Process",
                        "pid": proc.info["pid"],
                        "name": name,
                        "indicator": keyword,
                        "cmdline": cmdline
                    })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return findings


def scan_recent_files(minutes=15):
    findings = []
    cutoff_time = datetime.now() - timedelta(minutes=minutes)

    for directory in WATCH_DIRS:
        if not directory.exists():
            continue

        try:
            for file_path in directory.rglob("*"):
                if not file_path.is_file():
                    continue

                if file_path.suffix.lower() not in WATCH_EXTENSIONS:
                    continue

                modified_time = datetime.fromtimestamp(file_path.stat().st_mtime)

                if modified_time < cutoff_time:
                    continue

                filename = file_path.name.lower()

                for keyword in SUSPICIOUS_FILE_KEYWORDS:
                    if keyword in filename:
                        findings.append({
                            "type": "Recent Suspicious File",
                            "path": str(file_path),
                            "indicator": keyword,
                            "modified": modified_time.strftime("%Y-%m-%d %H:%M:%S"),
                            "size_bytes": file_path.stat().st_size
                        })
                        break

        except PermissionError:
            continue

    return findings


def print_results(findings):
    if not findings:
        print("[+] No obvious keylogger-like indicators found.")
        return

    print("[!] Possible keylogger-like indicators found:\n")

    for finding in findings:
        print(f"Type: {finding['type']}")

        for key, value in finding.items():
            if key != "type":
                print(f"{key}: {value}")

        print("-" * 60)


def main():
    boot_sequence()
    display_banner()

    print(Fore.LIGHTBLUE_EX + "[PHASE 1] Scanning running processes...")
    process_findings = scan_processes()
    time.sleep(0.7)

    print(Fore.LIGHTBLUE_EX + "[PHASE 2] Scanning recently modified suspicious files...")
    file_findings = scan_recent_files(minutes=15)
    time.sleep(0.7)

    all_findings = process_findings + file_findings

    print()
    print(Fore.RED + "[PHASE 3] Generating detection report...")
    time.sleep(0.7)

    print_results(all_findings)


if __name__ == "__main__":
    main()