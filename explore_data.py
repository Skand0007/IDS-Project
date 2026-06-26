# explore_data.py
# Purpose: Loads the dataset and shows basic information about it
# Author: SKAND SHARMA


# Import pandas for working with data
import pandas as pd


# NSL-KDD dataset has 43 columns but no headers
# We need to provide column names manually
# These names tell us what each column represents
columns = [
    'duration',                      # How long connection lasted
    'protocol_type',                 # TCP, UDP, or ICMP
    'service',                       # http, ftp, ssh, etc
    'flag',                          # Connection status
    'src_bytes',                     # Bytes sent from source
    'dst_bytes',                     # Bytes sent to destination
    'land',                          # 1 if same host/port
    'wrong_fragment',                # Number of wrong fragments
    'urgent',                        # Number of urgent packets
    'hot',                           # Number of hot indicators
    'num_failed_logins',             # Failed login attempts
    'logged_in',                     # 1 if logged in successfully
    'num_compromised',               # Compromised conditions
    'root_shell',                    # 1 if root shell obtained
    'su_attempted',                  # 1 if su attempted
    'num_root',                      # Number of root accesses
    'num_file_creations',            # Number of file creation operations
    'num_shells',                    # Number of shell prompts
    'num_access_files',              # Access control files
    'num_outbound_cmds',             # Outbound commands
    'is_host_login',                 # 1 if login is host
    'is_guest_login',                # 1 if login is guest
    'count',                         # Connections to same host
    'srv_count',                     # Connections to same service
    'serror_rate',                   # SYN error rate
    'srv_serror_rate',               # Service SYN error rate
    'rerror_rate',                   # REJ error rate
    'srv_rerror_rate',               # Service REJ error rate
    'same_srv_rate',                 # Same service rate
    'diff_srv_rate',                 # Different service rate
    'srv_diff_host_rate',            # Service different host rate
    'dst_host_count',                # Destination host count
    'dst_host_srv_count',            # Destination host service count
    'dst_host_same_srv_rate',        # Same service rate to dest host
    'dst_host_diff_srv_rate',        # Different service rate to dest host
    'dst_host_same_src_port_rate',   # Same source port rate
    'dst_host_srv_diff_host_rate',   # Service different host rate
    'dst_host_serror_rate',          # Destination SYN error rate
    'dst_host_srv_serror_rate',      # Destination service SYN error rate
    'dst_host_rerror_rate',          # Destination REJ error rate
    'dst_host_srv_rerror_rate',      # Destination service REJ error rate
    'label',                         # Attack type or normal
    'difficulty'                     # Difficulty score (not used)
]


# Load the data from CSV file
# pd.read_csv reads the file and creates a DataFrame
# names parameter assigns our column names
print("Loading dataset...")
data = pd.read_csv('data/KDDTrain.txt', names=columns)


# Show how many rows and columns we have
print("Total rows:", len(data))
print("Total columns:", len(data.columns))


# Show first 5 rows to see what data looks like
print("\nFirst 5 rows of data:")
print(data.head())


# Show all different attack types in the dataset
# value_counts() counts how many times each value appears
print("\nAttack types and their counts:")
print(data['label'].value_counts())


# Count normal vs attack traffic
# Normal traffic has label 'normal', everything else is attack
normal = len(data[data['label'] == 'normal'])
attack = len(data) - normal

print("\nNormal traffic:", normal)
print("Attack traffic:", attack)

print("\nExploration complete!")