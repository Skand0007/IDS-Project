# preprocess_data.py
# Purpose: Cleans and prepares the dataset for machine learning
# Author: SKAND SHARMA


# Import required libraries
import pandas as pd                              # For data handling
import pickle                                    # For saving objects
import os                                        # For creating folders
from sklearn.preprocessing import LabelEncoder   # Convert text to numbers
from sklearn.preprocessing import StandardScaler # Scale numbers
from sklearn.model_selection import train_test_split  # Split data


# Column names for NSL-KDD dataset
# We need these because dataset has no headers
columns = [
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
    'dst_host_srv_rerror_rate', 'label', 'difficulty'
]


# Step 1: Load the data
print("Step 1: Loading data...")
data = pd.read_csv('data/KDDTrain.txt', names=columns)


# Step 2: Remove difficulty column
# This column is not useful for prediction, so we remove it
print("Step 2: Removing unused columns...")
data = data.drop('difficulty', axis=1)


# Step 3: Convert labels to binary
# Machine Learning works better with numbers
# normal traffic = 0, any attack = 1
print("Step 3: Converting labels to numbers...")
data['label'] = data['label'].apply(lambda x: 0 if x == 'normal' else 1)


# Step 4: Convert text columns to numbers
# Columns like protocol_type have values 'tcp', 'udp', 'icmp'
# ML model only understands numbers, so we convert them
# LabelEncoder gives each unique text a unique number
# Example: tcp=0, udp=1, icmp=2
print("Step 4: Encoding text columns to numbers...")
encoders = {}  # Store encoders to use later for new data

for column in ['protocol_type', 'service', 'flag']:
    encoder = LabelEncoder()
    data[column] = encoder.fit_transform(data[column])
    encoders[column] = encoder


# Step 5: Separate features and labels
# X = all columns except 'label' (these are inputs)
# y = only 'label' column (this is what we want to predict)
print("Step 5: Separating features and labels...")
X = data.drop('label', axis=1)
y = data['label']


# Step 6: Scale the features
# Different columns have different ranges
# Example: duration is 0-100, src_bytes is 0-1,000,000
# StandardScaler makes all columns have similar range
# This helps ML model learn better
print("Step 6: Scaling features...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)


# Step 7: Split data into training and testing sets
# 80% data is used to train the model
# 20% data is used to test how well model learned
# random_state=42 makes split same every time we run
print("Step 7: Splitting data into train and test sets...")
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y,
    test_size=0.2,
    random_state=42
)


# Step 8: Create folders to save files
print("Step 8: Creating folders...")
if not os.path.exists('data/processed'):
    os.makedirs('data/processed')

if not os.path.exists('models'):
    os.makedirs('models')


# Step 9: Save processed data to CSV files
# We will use these files in next step for training
print("Step 9: Saving processed data...")
X_train.to_csv('data/processed/X_train.csv', index=False)
X_test.to_csv('data/processed/X_test.csv', index=False)
y_train.to_csv('data/processed/y_train.csv', index=False)
y_test.to_csv('data/processed/y_test.csv', index=False)


# Step 10: Save encoders and scaler
# We need these later to process new data the same way
# Without these, model predictions will be wrong
print("Step 10: Saving encoders and scaler...")
with open('models/encoders.pkl', 'wb') as f:
    pickle.dump(encoders, f)

with open('models/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)


# Show final summary
print("\nPreprocessing complete!")
print("Training data:", len(X_train), "rows")
print("Testing data:", len(X_test), "rows")
print("Total features:", X_train.shape[1])