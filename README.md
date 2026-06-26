# Intrusion Detection System using Machine Learning

A real-time network intrusion detection system that uses Machine Learning to detect cyber attacks with 99% accuracy.

## About the Project

This project captures live network packets, analyzes them using a trained Random Forest model, and identifies whether the traffic is normal or an attack.

## Features

- Real-time packet capture
- Machine learning based detection
- 99.78% accuracy
- Automatic logging
- Summary report generation

## Technologies Used

- Python
- Scapy (packet capture)
- Scikit-learn (machine learning)
- Pandas (data processing)
- NSL-KDD Dataset

## Project Structure
IDS_Project/
├── data/ - Dataset files
├── models/ - Trained ML model
├── logs/ - Detection logs
├── reports/ - Generated reports
├── download_dataset.py - Downloads dataset
├── explore_data.py - Shows data info
├── preprocess_data.py - Cleans data
├── train_model.py - Trains ML model
├── realtime_detector.py - Real-time detection
├── generate_report.py - Creates report
├── logger.py - Logger utility
├── run_all.py - Main menu
├── requirements.txt - Required libraries
└── README.md - This file

## How to Install

   ### 1. Clone this repository
   git clone https://github.com/YOUR_USERNAME/IDS-Project.git
cd IDS-Project

### 2. Create virtual environment
python -m venv ids_env
ids_env\Scripts\activate

### 3. Install required libraries
pip install -r requirements.txt

### 4. Install Npcap (Windows only)
Download from: https://npcap.com/#download

## How to Use

### Step 1: Download dataset
python download_dataset.py

### Step 2: Preprocess data
python preprocess_data.py

### Step 3: Train model
python train_model.py

### Step 4: Start detection (run as Administrator)
python realtime_detector.py

### Step 5: Generate report
python generate_report.py

## Model Performance

- Accuracy: 99.78%
- Precision: 99.84%
- Recall: 99.69%
- F1 Score: 99.76%

## Dataset

NSL-KDD Dataset with 125,973 training records and 22,544 testing records.

## Author

SKAND SHARMA

- GitHub: https://github.com/Skand0007?tab=repositories
- Email:0007skand@gmail.com