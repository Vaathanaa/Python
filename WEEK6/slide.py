# import csv

# # Open (or create) a CSV file in write mode
# with open("students.csv", "w", newline="") as file:
#     writer = csv.writer(file)
    
#     # Write header row
#     writer.writerow(["Name", "Age", "City"])
    
#     # Write data rows
#     writer.writerow(["Alice", 20, "Phnom Penh"])
#     writer.writerow(["Bob", 22, "Siem Reap"])
#     writer.writerow(["Charlie", 21, "Battambang"])
    
    
    
import csv
from datetime import datetime

def generate_security_report(logins, filename="security_report.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "IP", "Status"])  # header
        for ip, status in logins:
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ip, status])
    print(f"Report saved to {filename}")

# Example usage
suspicious_logins = [
    ("192.168.1.10", "Failed"),
    ("10.0.0.5", "Failed"),
    ("172.16.0.2", "Multiple Failed")
]

generate_security_report(suspicious_logins)