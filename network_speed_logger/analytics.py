import csv
from pathlib import Path

CSV_PATH = Path("speedtest_results.csv")


def to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def show_stats():
    if not CSV_PATH.exists():
        print("No speed test data found.")
        return

    with CSV_PATH.open("r", newline="") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    if not data:
        print("No speed test data found.")
        return

    total_tests = len(data)
    successful_tests = sum(1 for info in data if info["Status"] == "Success")
    failed_tests = total_tests - successful_tests

    total_download_speed = sum(to_float(info["Download Speed (Mbps)"]) for info in data)
    total_upload_speed = sum(to_float(info["Upload Speed (Mbps)"]) for info in data)
    total_ping = sum(to_float(info["Ping Rate (ms)"]) for info in data)

    avg_download_speed = total_download_speed / total_tests
    avg_upload_speed = total_upload_speed / total_tests
    avg_ping = total_ping / total_tests

    highest_download = max(
        data, key=lambda info: to_float(info["Download Speed (Mbps)"])
    )
    lowest_download = min(
        data, key=lambda info: to_float(info["Download Speed (Mbps)"])
    )
    print(
        f"====== Your Internet Statistics =======\n"
        f"Note: Data is based on tests in speedtest_results.csv\n"
        f"Total tests: {total_tests}\n"
        f"Successful Tests: {successful_tests}\n"
        f"Failed tests: {failed_tests}\n\n"
        f"Average Download: {avg_download_speed:.2f} Mbps\n"
        f"Average Upload: {avg_upload_speed:.2f} Mbps\n"
        f"Highest Download: {to_float(highest_download['Download Speed (Mbps)']):.2f} Mbps\n"
        f"Lowest Download: {to_float(lowest_download['Download Speed (Mbps)']):.2f} Mbps\n"
        f"Average Ping: {avg_ping:.1f} ms"
    )


if __name__ == "__main__":
    show_stats()
