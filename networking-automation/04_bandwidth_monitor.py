import psutil
import time
import csv
from datetime import datetime

CSV_FILE = "bandwidth_log.csv"

def initialize_csv():
    try:
        with open(CSV_FILE, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(("timestamp", "bytes_sent", "bytes_recv"))
    except FileExistsError:
        pass

def get_stats():
    net = psutil.net_io_counters()
    return net.bytes_sent, net.bytes_recv

def log_stats(sent, recv):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            sent,
            recv
        ])

def monitor():
    initialize_csv()

    print("Starting bandwidth monitoring...")

    while True:
        sent, recv = get_stats()
        log_stats(sent, recv)

        print(f"Logged - Sent: {sent} | Received: {recv}")

        time.sleep(60)

def generate_report():
    total_sent = 0
    total_recv = 0
    count = 0

    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_sent = int(row["bytes_sent"])
            total_recv = int(row["bytes_recv"])
            count += 1

    print("\n--- Bandwidth Report ---")
    print(f"Samples: {count}")
    print(f"Last Sent Value: {total_sent}")
    print(f"Last Received Value: {total_recv}")

if __name__ == "__main__":
    choice = input("1. Monitor\n2. Report\nChoose: ")

    if choice == "1":
        monitor()
    elif choice == "2":
        generate_report()