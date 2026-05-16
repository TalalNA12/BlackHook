import time
from pathlib import Path
from datetime import datetime
from colorama import Fore, Style, init
import os
import sys
import random

init(autoreset=True)

if os.name == "nt":
    LOG_PATH = Path("C:/Users/Public/blackhook_trace.log")
else:
    LOG_PATH = Path.cwd() / "blackhook_trace.log"

FAKE_KEYSTROKES = [
    "admin",
    "password123",
    "test_login",
    "student_portal",
    "fake_credentials",
    "comsats_demo",
    "analysis_input",
    "security_lab",
    "hello_world",
    "this_is_fake_data"
]

buffer = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def slow_print(text, color=Fore.WHITE, delay=0.025):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)

    print()


def loading_bar(label, color=Fore.RED, total=25, delay=0.05):
    sys.stdout.write(color + f"{label:<34} [" + Style.RESET_ALL)
    sys.stdout.flush()

    for _ in range(total):
        sys.stdout.write(color + "█" + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write(color + "] DONE\n" + Style.RESET_ALL)
    sys.stdout.flush()
    time.sleep(0.2)


BANNER = r"""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝ ███████║██║   ██║██║   ██║█████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██╔══██║██║   ██║██║   ██║██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
"""


def boot_sequence():
    clear_screen()

    slow_print(">> BLACKHOOK SIMULATION ENGINE INITIALIZING", Fore.RED)
    time.sleep(0.4)

    slow_print(">> Loading simulated behavior modules...", Fore.WHITE)
    time.sleep(0.3)

    slow_print(">> Keyboard capture module: DISABLED", Fore.GREEN)
    time.sleep(0.3)

    slow_print(">> Real keystroke collection: DISABLED", Fore.GREEN)
    time.sleep(0.3)

    slow_print(">> Educational simulation mode: ENABLED", Fore.GREEN)
    time.sleep(0.5)

    print()

    loading_bar("Initializing fake buffer engine", Fore.RED)
    loading_bar("Preparing filesystem trace", Fore.RED)
    loading_bar("Generating simulated activity", Fore.RED)

    time.sleep(0.6)

    clear_screen()

    print(Fore.RED + BANNER + Style.RESET_ALL)

    print(Fore.WHITE + "╔══════════════════════════════════════════════════════════════════════════════╗")
    print(Fore.WHITE + "║                         BLACKHOOK SIMULATOR                                  ║")
    print(Fore.WHITE + "║                 Simulated Keylogger Behavior Generator                       ║")
    print(Fore.WHITE + "╠══════════════════════════════════════════════════════════════════════════════╣")
    print(Fore.WHITE + "║  Mode       : Defensive Academic Simulation                                  ║")
    print(Fore.WHITE + "║  Capture    : DISABLED                                                       ║")
    print(Fore.WHITE + "║  Objective  : Generate detectable suspicious-like behavior                   ║")
    print(Fore.WHITE + "║  Safety     : No real keyboard input is captured                             ║")
    print(Fore.WHITE + "╚══════════════════════════════════════════════════════════════════════════════╝")
    print()

    slow_print(">> Starting simulated logging activity...\n", Fore.RED)


def flush_buffer():
    if not buffer:
        return

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(LOG_PATH, "a", encoding="utf-8") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_file.write(f"\n[{timestamp}] ")
        log_file.write(" ".join(buffer))

    print(
        Fore.YELLOW
        + f"[BUFFER FLUSH] Wrote {len(buffer)} fake entries to {LOG_PATH}"
    )

    buffer.clear()


def simulate_activity():
    print(Fore.CYAN + f"[INFO] Log file target: {LOG_PATH}")
    print(Fore.CYAN + "[INFO] Simulation running...\n")

    for _ in range(12):
        fake_input = random.choice(FAKE_KEYSTROKES)

        print(
            Fore.WHITE
            + f"[BUFFER] Adding simulated input -> "
            + Fore.RED
            + fake_input
        )

        buffer.append(fake_input)

        time.sleep(random.uniform(1.0, 2.5))

        if len(buffer) >= 4:
            flush_buffer()

    flush_buffer()

    print()
    slow_print("[+] Simulation complete.", Fore.GREEN)
    slow_print("[+] Fake trace data generated successfully.", Fore.GREEN)
    slow_print("[+] No real keyboard input was collected.", Fore.GREEN)


def main():
    boot_sequence()
    simulate_activity()


if __name__ == "__main__":
    main()