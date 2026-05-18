file_path = input("Enter CSV file path: ")
 
with open(file_path, "r") as file:
    lines = file.readlines();

for line in lines:
    line = line.strip()

    if not line:
        continue

    parts = line.split(",")

    if len(parts) < 3:
        print(f"Skipping invalid line: {line}")
        continue

    name, age, role = parts[:3]

    print(f"Name: {name} | Age: {age} | Role: {role}")