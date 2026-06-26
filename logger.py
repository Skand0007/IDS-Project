# logger.py
# Purpose: Tests if the log file is working correctly
# Note: Main logging happens in realtime_detector.py
# Author: SKAND SHARMA


# Import libraries
import csv  # To work with CSV files
import os   # To check folders


# Create logs folder if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')
    print("Created logs folder")


# Path to log file
log_file = 'logs/detections.csv'


# Create log file with headers if it doesn't exist
if not os.path.exists(log_file):
    with open(log_file, 'w', newline='') as f:
        writer = csv.writer(f)
        # First row is column names
        writer.writerow(['time', 'source_ip', 'dest_ip', 'protocol', 'prediction', 'confidence'])
    print("Created new log file:", log_file)
else:
    print("Log file already exists:", log_file)


# Read and show all logs
print("\nShowing all logs:")
print("-" * 60)

with open(log_file, 'r') as f:
    reader = csv.reader(f)
    
    # Print each row in the file
    for row in reader:
        print(row)

print("-" * 60)
print("Done!")