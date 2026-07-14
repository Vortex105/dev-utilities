import datetime as dt
import os
import time

import psutil

CLEAR_COMMAND = "cls" if os.name == "nt" else "clear"
BAR_WIDTH = 28

RESET = "\033[0m"
DIM = "\033[2m"
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[97m"


def get_cpu():
    return psutil.cpu_percent(interval=None)


def get_ram():
    return psutil.virtual_memory().percent


def get_disk_usage(path="C:/"):
    return psutil.disk_usage(path).percent


def get_battery_percent():
    battery = psutil.sensors_battery()
    return battery.percent if battery else None


def get_uptime():
    seconds = int(time.time() - psutil.boot_time())
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    parts = []
    if days:
        parts.append(f"{days}d")
    if hours or days:
        parts.append(f"{hours}h")
    parts.append(f"{minutes}m")
    parts.append(f"{seconds}s")
    return " ".join(parts)


def color_for_percent(percent):
    if percent < 50:
        return GREEN
    if percent < 80:
        return YELLOW
    return RED


def build_bar(percent):
    filled = int((percent / 100) * BAR_WIDTH)
    filled = max(0, min(BAR_WIDTH, filled))
    bar_color = color_for_percent(percent)
    bar = f"{bar_color}{'█' * filled}{DIM}{'░' * (BAR_WIDTH - filled)}{RESET}"
    return bar


def format_metric(label, percent):
    if percent is None:
        return f"{WHITE}{label:<8}{RESET} unavailable"
    return f"{WHITE}{label:<8}{RESET} [{build_bar(percent)}] {color_for_percent(percent)}{percent:5.1f}%{RESET}"


def read_key():
    if os.name != "nt":
        return None

    try:
        import msvcrt
    except ImportError:
        return None

    if msvcrt.kbhit():
        return msvcrt.getwch().lower()
    return None


def main():
    paused = False
    refresh_delay = 1.0

    while True:
        key = read_key()
        if key == "q":
            break
        if key == "p":
            paused = not paused
        if key == "+":
            refresh_delay = max(0.2, refresh_delay - 0.2)
        if key == "-":
            refresh_delay = min(3.0, refresh_delay + 0.2)

        if not paused:
            cpu_usage = get_cpu()
            ram_usage = get_ram()
            disk_usage = get_disk_usage()
            battery_usage = get_battery_percent()

            os.system(CLEAR_COMMAND)
            print(f"{BOLD}{CYAN}SYSTEM MONITOR{RESET}")
            print(
                f"{DIM}Press p to pause, q to quit, + / - to change refresh speed{RESET}\n"
            )
            print(format_metric("CPU", cpu_usage))
            print(format_metric("RAM", ram_usage))
            print(format_metric("Disk", disk_usage))
            print(format_metric("Battery", battery_usage))
            print(f"\n{WHITE}Uptime  {RESET}{get_uptime()}")
            print(f"{DIM}Refresh: {refresh_delay:.1f}s{RESET}")

        time.sleep(refresh_delay)


if __name__ == "__main__":
    main()
