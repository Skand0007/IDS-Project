# download_dataset.py
# Purpose: Downloads the NSL-KDD dataset for training the IDS
# Author: SKAND SHARMA


# Import libraries
import urllib.request   # For downloading files from internet
import os               # For creating folders


# Create data folder to store the dataset
# If folder already exists, this does nothing
if not os.path.exists('data'):
    os.makedirs('data')
    print("Created data folder")


# These are the URLs where dataset files are stored on GitHub
# NSL-KDD is a popular dataset for intrusion detection
train_url = "https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain%2B.txt"
test_url = "https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTest%2B.txt"


# Download the training data file
# This file has 125,973 network connection records
print("Downloading training data...")
urllib.request.urlretrieve(train_url, 'data/KDDTrain.txt')
print("Training data downloaded successfully")


# Download the testing data file
# This file has 22,544 network connection records
print("Downloading testing data...")
urllib.request.urlretrieve(test_url, 'data/KDDTest.txt')
print("Testing data downloaded successfully")


# Print final message
print("\nAll downloads complete!")
print("Files saved in data folder")