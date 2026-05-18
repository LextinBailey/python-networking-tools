# Python Networking Tools

This repository documents my progression from Python fundamentals into network automation through incremental scripting projects.

## 📊 Learning Structure

The project is divided into three stages:

### 1. Fundamentals (Core Python Scripting)

Focus: Learn basic Python syntax, input handling, logic, and simple automation patterns.

These scripts establish the foundation for all later automation work.

1. Tip Calculator
    Takes a bill amount and tip percentage, validates input, and calculates tip and total.
2. Temperature Converter
    Converts between Celsius, Fahrenheit, and Kelvin with user input.
3. CSV Reader
    Reads a CSV file and prints formatted output to the terminal.
4. Password Generator
    Generates source passwords with configurable length and character sets.
5. Number Guessing Game
    Interactive CLI game using random numbers and attempt limits.

### 2. Intermediate (Data Handling & Automation Basics)

Focus: Work with files, APIs, web data, and system-level automation concepts.

1. IP Ping Checker
    Reads a list of IP addresses from a file and reports which are reachable.
2. Log File Parser
    Extracts error lines and timestamps from system logs.
3. Web Scraper (BeatifulSoup)
    Scrapes structured data from public websites.
4. REST API Client
    Uses the `requests` library to fetch and parse JSON data from APIs.
5. Port Scanner
    Scans a target IP over a port range and identifies open ports.

### 3. Network Automation (Real-World Infrastructure Tools)

Focus: Automate real network and system administration tasks.

1. SSH Remote Executor (Paramiko)
    Connects to a remote server and executes commands via SSH.
2. Network Inventory Scanner
    Scans a local network and reports connected devices and details.
3. System Monitoring Alert Tool
    Monitors CPU and memory usage and sends alerts when thresholds are exceeded.
4. Bandwidth Logger
    Tracks network usage over time and exports data to CSV reports.
5. Router Backup Automation
    Automatically backs up configuration files from a pfSense router via SSH.

## 🚀 How to Use This Repo

Each script is standalone and can be run individually:

```bash
python3 fundamentals/01_tip_calculator.py
```

## 📈 Progression Notes

Progress insights are tracked in `progress-log.md`