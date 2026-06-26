# generate_report.py
# Purpose: Reads detection logs and creates a summary report
# Author:SKAND SHARMA


# Import libraries
import pandas as pd            # For data handling
import os                       # For folders and files
from datetime import datetime   # For timestamps


# Step 1: Check if log file exists
# Can't generate report without logs
if not os.path.exists('logs/detections.csv'):
    print("ERROR: No log file found!")
    print("Please run realtime_detector.py first to capture some packets")
    exit()


# Step 2: Load the log file
print("Loading logs...")
data = pd.read_csv('logs/detections.csv')


# Step 3: Show report header
print("\n" + "=" * 50)
print("INTRUSION DETECTION REPORT")
print("=" * 50)
print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("=" * 50)


# Step 4: Show total detections
total = len(data)
print("\nTotal detections:", total)


# Step 5: Count normal vs attack traffic
normal = len(data[data['prediction'] == 'Normal'])
attacks = len(data[data['prediction'] == 'ATTACK'])

print("Normal traffic:", normal)
print("Attacks detected:", attacks)


# Step 6: Calculate attack percentage
# Only if there are detections (avoid divide by zero)
if total > 0:
    rate = (attacks / total) * 100
    print("Attack rate:", round(rate, 2), "%")


# Step 7: Show protocol breakdown
# value_counts() counts how many of each protocol
print("\nProtocols used:")
print(data['protocol'].value_counts())


# Step 8: Show top 5 source IPs
# These are IPs that sent most packets
print("\nTop 5 source IPs:")
print(data['source_ip'].value_counts().head(5))


# Step 9: Show top attackers (only if attacks detected)
if attacks > 0:
    print("\nTop 5 attacker IPs:")
    # Filter only attack records
    attack_data = data[data['prediction'] == 'ATTACK']
    print(attack_data['source_ip'].value_counts().head(5))


# Step 10: Save report to text file
# Create reports folder if not exists
if not os.path.exists('reports'):
    os.makedirs('reports')


# Create filename with current date and time
filename = "reports/report_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"


# Write report to file
with open(filename, 'w') as f:
    f.write("INTRUSION DETECTION REPORT\n")
    f.write("Generated: " + str(datetime.now()) + "\n\n")
    f.write("Total detections: " + str(total) + "\n")
    f.write("Normal traffic: " + str(normal) + "\n")
    f.write("Attacks detected: " + str(attacks) + "\n")


print("\nReport saved to:", filename)
print("Done!")