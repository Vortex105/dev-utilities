# Network Speed Logger

A small Python utility to measure and log network upload/download speeds over time. Useful for tracking connectivity, bandwidth issues, or collecting data for analysis.

Features
- Periodic speed tests (download/upload)
- CSV logging with timestamps
- Simple configuration for interval and output file

Requirements
- Python 3.7+

Installation
1. Clone the repository.
2. Create a virtual environment and activate it:
	python -m venv .venv
	.venv\Scripts\activate  # Windows
3. Install dependencies:
	pip install -r requirements.txt

Usage
- Configure the interval and output path in the project's config or command-line options.
- Run the logger:
  python -m network_speed_logger

Output
- The tool appends rows to a CSV file with columns: timestamp, download_mbps, upload_mbps, ping_ms

Configuration
- Adjust the test interval (seconds) and output CSV path in config.py or via CLI flags.

Contributing
- Open issues or pull requests. Keep changes focused and include tests where appropriate.

License
- MIT

