# realtime_detector.py
# Purpose: Captures live network packets and detects attacks using ML model
# Author: SKAND SHARMA


# Import libraries
import pandas as pd                                          # For data handling
import pickle                                                # To load model
import csv                                                   # To save logs
import os                                                    # For folders
from datetime import datetime                                # For timestamps
from scapy.all import sniff, IP, TCP, UDP, ICMP             # For packet capture


# Step 1: Load the trained model
# This is the model we trained in train_model.py
print("Loading model...")
with open('models/ids_model.pkl', 'rb') as f:
    model = pickle.load(f)


# Step 2: Load the scaler
# We need the same scaler used during training
# This makes sure new data is scaled the same way
print("Loading scaler...")
with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


# Step 3: Define feature names
# These are the 41 features our model was trained on
# Order must match training data order
feature_names = [
    'duration', 'protocol_type', 'service', 'flag',
    'src_bytes', 'dst_bytes', 'land', 'wrong_fragment',
    'urgent', 'hot', 'num_failed_logins', 'logged_in',
    'num_compromised', 'root_shell', 'su_attempted', 'num_root',
    'num_file_creations', 'num_shells', 'num_access_files',
    'num_outbound_cmds', 'is_host_login', 'is_guest_login',
    'count', 'srv_count', 'serror_rate', 'srv_serror_rate',
    'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
    'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
    'dst_host_srv_count', 'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
    'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate'
]


# Step 4: Create logs folder
# This is where we save all detections
if not os.path.exists('logs'):
    os.makedirs('logs')


# Step 5: Create log file with column headers
# CSV file to store all detections
log_file = 'logs/detections.csv'

if not os.path.exists(log_file):
    with open(log_file, 'w', newline='') as f:
        writer = csv.writer(f)
        # Write column names as first row
        writer.writerow(['time', 'source_ip', 'dest_ip', 'protocol', 'prediction', 'confidence'])


# Function to extract features from a packet
# Live packets don't have all 41 features
# We use what we can get and put 0 for the rest
def get_features(packet):
    
    # Start with all features as 0
    features = {name: 0 for name in feature_names}
    
    # If packet has IP layer (most packets do)
    if IP in packet:
        # Get packet size
        features['src_bytes'] = len(packet[IP])
        features['dst_bytes'] = len(packet[IP])
        
        # Set protocol type as number
        # TCP=2, UDP=1, ICMP=0 (same as in training data)
        if packet[IP].proto == 6:    # TCP
            features['protocol_type'] = 2
        elif packet[IP].proto == 17: # UDP
            features['protocol_type'] = 1
        else:                        # Others (like ICMP)
            features['protocol_type'] = 0
        
        # Set count to 1 (this is single packet)
        features['count'] = 1
        features['same_srv_rate'] = 1.0
    
    return features


# Function to save detection to CSV file
def save_log(src_ip, dst_ip, protocol, prediction, confidence):
    
    # Get current time
    time_now = datetime.now().strftime("%H:%M:%S")
    
    # Open file in append mode (adds to existing file)
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([time_now, src_ip, dst_ip, protocol, prediction, confidence])


# Function called for each captured packet
def check_packet(packet):
    
    # Skip packets without IP layer
    if IP not in packet:
        return
    
    # Get source and destination IPs
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    
    # Get protocol name for display
    if packet[IP].proto == 6:
        protocol = "TCP"
    elif packet[IP].proto == 17:
        protocol = "UDP"
    elif packet[IP].proto == 1:
        protocol = "ICMP"
    else:
        protocol = "OTHER"
    
    # Get features from packet
    features = get_features(packet)
    
    # Convert features to DataFrame (needed by sklearn)
    df = pd.DataFrame([features])
    df = df[feature_names]  # Make sure columns are in right order
    
    # Scale features same way as training data
    df_scaled = scaler.transform(df)
    
    # Use model to predict
    # Returns 0 for normal, 1 for attack
    prediction = model.predict(df_scaled)[0]
    
    # Get probability of each class
    # This tells us how confident model is
    probability = model.predict_proba(df_scaled)[0]
    confidence = round(max(probability) * 100, 2)
    
    # Convert prediction to text
    if prediction == 1:
        result = "ATTACK"
    else:
        result = "Normal"
    
    # Print result on screen
    time_now = datetime.now().strftime("%H:%M:%S")
    print(f"[{time_now}] {protocol} | {src_ip} -> {dst_ip} | {result} ({confidence}%)")
    
    # Save to log file
    save_log(src_ip, dst_ip, protocol, result, confidence)


# Main code starts here
print("\n" + "=" * 60)
print("INTRUSION DETECTION SYSTEM")
print("=" * 60)
print("Capturing 100 packets... Press Ctrl+C to stop early\n")


# Start sniffing packets
# prn=check_packet means call check_packet for each packet
# count=100 means stop after 100 packets
try:
    sniff(prn=check_packet, count=100)
except KeyboardInterrupt:
    print("\nStopped by user")


# Show completion message
print("\nDetection complete!")
print("Check logs/detections.csv to see all results")