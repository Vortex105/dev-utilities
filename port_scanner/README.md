# Port Scanner

`port_scanner` is a Python utility for checking which TCP ports are open on a target host. It is intended as a compact, readable example of network scanning and a practical tool for quick connectivity checks.

## Overview

The repository focuses on one core task: attempting TCP connections to a range of ports and reporting which ones accept connections. This is the standard foundation for many simple port-scanning tools.

The project is useful for:

- learning how Python sockets work
- checking whether a service is listening on a port
- validating local network access
- understanding basic network error handling

## What the scanner does

The scanner typically follows these steps:

1. Accept a host name or IP address.
2. Accept a start and end port, or another port selection method.
3. Loop through the selected ports.
4. Open a socket connection attempt for each port.
5. Use a timeout so the scan does not stall on unresponsive ports.
6. Print or collect the ports that respond successfully.

If the connection attempt succeeds, the port is open. If it fails, times out, or is refused, the port is treated as closed or filtered.

## Code purpose and design

The code in a port scanner like this usually has three responsibilities:

### Input handling

This part reads the host and port range from the user or command line, then validates that the values are usable.

### Scanning logic

This is the core implementation. It creates sockets, attempts connections, and decides whether a port should be reported as open.

### Output formatting

This part presents the results in a clear way, often printing each open port and sometimes showing a summary at the end.

Keeping these responsibilities separate makes the code easier to read, test, and extend.

## Python concepts used

### Socket programming

The scanner uses Python's built-in `socket` module. A socket is the standard interface for network communication. For TCP scanning, the code usually creates an `AF_INET` / `SOCK_STREAM` socket and attempts to connect to a host and port.

### Timeouts

Timeouts are important because some ports do not respond quickly. Without a timeout, the scanner could pause too long on each failed connection attempt. A small timeout keeps scans efficient.

### Exception handling

Connection attempts can fail for many normal reasons, so the scanner should catch network-related exceptions and continue scanning instead of stopping at the first failure.

### Loops and range iteration

Scanning a port range requires iterating over a sequence of port numbers and repeating the same connection test for each one.

## Example usage

The exact interface depends on the implementation, but a typical command may look like this:

```bash
python port_scanner.py 192.168.1.10 1 1024
```

This scans ports 1 through 1024 on the specified host.

Another example:

```bash
python port_scanner.py example.com 80 443
```

This checks a small set of common web-related ports.

## Example output

A simple run might produce output like:

```text
Scanning target: 192.168.1.10
Open port: 22
Open port: 80
Open port: 443
Scan complete.
```

Depending on the code, the script may also print closed ports, skipped ports, or a summary count.

## Extending the project

This repository can be expanded in several useful ways:

- add `argparse` for cleaner command-line options
- support scanning multiple hosts
- use threads or async code for faster scans
- add banner grabbing to identify running services
- save results to a file
- colorize terminal output
- add subnet scanning support

## Responsible use

Only scan systems you own or are explicitly authorized to test. Port scanning on third-party systems without permission can violate policies or laws. This tool should be used in controlled, legitimate environments.

## Development notes

When reading or modifying the code, the most important implementation details are usually:

- how the socket timeout is configured
- how open ports are detected
- how exceptions are handled
- whether the scan is sequential or concurrent
- how results are displayed

If the scanner is small, it may be implemented as one main function plus a simple entry point. If it is more structured, it may include helper functions or a class to organize scan behavior.

## Summary

`port_scanner` is a lightweight Python network utility for identifying open TCP ports on a target host. It demonstrates practical socket usage, timeout handling, and scan reporting while remaining straightforward enough to understand and modify.
```
