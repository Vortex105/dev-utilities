import speedtest
import csv
import datetime
import os
import time

FAILED_SPEED_TEST_VALUE = 0.0


def format_server(server):
    if not server:
        return ""

    host = server.get("host", "")
    sponsor = server.get("sponsor", "")
    name = server.get("name", "")
    country = server.get("country", "")

    parts = [part for part in [sponsor, name, country] if part]
    location = ", ".join(parts)

    if host and location:
        return f"{host} ({location})"
    return host or location


def run_speed_test():
    server = None
    try:
        test = speedtest.Speedtest()
        server = test.get_best_server()
        download_speed = f"{test.download() / 1_000_000:.2f}"
        upload_speed = f"{test.upload() / 1_000_000:.2f}"
        ping_rate = f"{test.results.ping:.1f}"

        return {
            "success": True,
            "download_speed": download_speed,
            "upload_speed": upload_speed,
            "ping_rate": ping_rate,
            "server_used": format_server(server),
            "error": "",
        }
    except Exception as error:
        return {
            "success": False,
            "download_speed": FAILED_SPEED_TEST_VALUE,
            "upload_speed": FAILED_SPEED_TEST_VALUE,
            "ping_rate": FAILED_SPEED_TEST_VALUE,
            "server_used": format_server(server),
            "error": str(error),
        }


def create_csv(test_result):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("speedtest_results.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Timestamp",
                "Download Speed (Mbps)",
                "Upload Speed (Mbps)",
                "Ping Rate (ms)",
                "Status",
                "Server_Used",
                "Error",
            ]
        )
        writer.writerow(
            [
                current_time,
                test_result["download_speed"],
                test_result["upload_speed"],
                test_result["ping_rate"],
                "Success" if test_result["success"] else "Failed",
                test_result["server_used"],
                test_result["error"],
            ],
        )


def main():
    csv_exists = os.path.isfile("speedtest_results.csv")
    test_result = run_speed_test()

    if not csv_exists:
        create_csv(test_result)
    else:
        with open("speedtest_results.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    test_result["download_speed"],
                    test_result["upload_speed"],
                    test_result["ping_rate"],
                    "Success" if test_result["success"] else "Failed",
                    test_result["server_used"],
                    test_result["error"],
                ],
            )


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()

    print(f"Execution time: {end - start:.4f} seconds")
