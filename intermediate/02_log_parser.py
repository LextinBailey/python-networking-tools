file_path = input("Enter log file path: ")

with open(file_path, "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()

    if "ERROR" in line:
        parts = line.split(" ")

        timestamp = parts[0] + " " + parts[1]
        message = " ".join(parts[3:])

        print(f"[{timestamp}] {message}")