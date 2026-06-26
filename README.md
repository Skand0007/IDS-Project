# 🛡️ Intrusion Detection System using Machine Learning

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/Status-Complete-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

A real-time network intrusion detection system that uses Machine Learning 
to detect cyber attacks with **99% accuracy**.

Built with Python, Scapy, and Scikit-learn.

---

## 📖 About the Project

This project captures live network packets, analyses them using a trained 
**Random Forest** model, and identifies whether the traffic is **normal** 
or an **attack**.

---

## ✨ Features

- ✅ Real-time packet capture
- ✅ Machine learning based detection
- ✅ 99.78% accuracy
- ✅ Automatic logging of detections
- ✅ Summary report generation
- ✅ Easy-to-use menu system

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core language |
| Scapy | Live packet capture |
| Scikit-learn | Machine learning |
| Pandas | Data processing |
| Random Forest | Classification model |
| NSL-KDD Dataset | Training data |

---

## 🗂️ Project Structure

```
IDS_Project/
│
├── data/                    # Dataset files
├── models/                  # Trained ML model
├── logs/                    # Detection logs
├── reports/                 # Generated reports
│
├── download_dataset.py      # Downloads dataset
├── explore_data.py          # Shows data info
├── preprocess_data.py       # Cleans data
├── train_model.py           # Trains ML model
├── realtime_detector.py     # Real-time detection
├── generate_report.py       # Creates report
├── logger.py                # Logger utility
├── run_all.py               # Main menu
│
├── requirements.txt         # Required libraries
└── README.md                # This file
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Skand0007/IDS-Project.git
cd IDS-Project
```

### 2. Create a virtual environment

```bash
python -m venv ids_env
ids_env\Scripts\activate
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

### 4. Install Npcap (Windows only)

Download from: [https://npcap.com/#download](https://npcap.com/#download)

This is required for Scapy to capture packets on Windows.

---

## 🚀 How to Use

### Step 1: Download the dataset

```bash
python download_dataset.py
```

### Step 2: Preprocess the data

```bash
python preprocess_data.py
```

### Step 3: Train the model

```bash
python train_model.py
```

### Step 4: Start real-time detection

> ⚠️ Must be run as **Administrator**

```bash
python realtime_detector.py
```

### Step 5: Generate a summary report

```bash
python generate_report.py
```

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | **99.78%** |
| Precision | 99.84% |
| Recall | 99.69% |
| F1 Score | 99.76% |

---

## 📂 Dataset

**NSL-KDD Dataset**

- Training records: **125,973**
- Testing records: **22,544**
- Source: [NSL-KDD Official](https://www.unb.ca/cic/datasets/nsl.html)

---

## 🧠 How It Works

```
Live Network Traffic
        │
        ▼
Scapy captures packets
        │
        ▼
Feature extraction
        │
        ▼
Random Forest classifier
        │
        ▼
Normal Traffic   OR   Attack Detected
                          │
                          ▼
                     Logged + Reported
```

---

## 🔮 Future Improvements

- [ ] Add a web dashboard for live monitoring
- [ ] Support for deep learning models (LSTM/CNN)
- [ ] Multi-class attack classification (DoS, Probe, R2L, U2R)
- [ ] Email/Telegram alerts for detected attacks
- [ ] Export reports as PDF
- [ ] Deploy on a cloud server

---

## 👤 Author

**Skand Sharma**  
Cybersecurity Student

- 🔗 **GitHub:** [Skand0007](https://github.com/Skand0007)
- 📧 **Email:** 0007skand@gmail.com
