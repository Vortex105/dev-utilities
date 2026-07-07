import speedtest
import csv
import datetime
import os

FAILED_SPEED_TEST_VALUE = 0.0


def run_speed_test():
    try:
        test = speedtest.Speedtest()
        download_speed = test.download() / 1_000_000
        upload_speed = test.upload() / 1_000_000
        ping_rate = test.results.ping

        return {
            "success": True,
            "download_speed": download_speed,
            "upload_speed": upload_speed,
            "ping_rate": ping_rate,
            "error": "",
        }
    except Exception as error:
        return {
            "success": False,
            "download_speed": FAILED_SPEED_TEST_VALUE,
            "upload_speed": FAILED_SPEED_TEST_VALUE,
            "ping_rate": FAILED_SPEED_TEST_VALUE,
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
                    test_result["error"],
                ],
            )


if __name__ == "__main__":
    main()
