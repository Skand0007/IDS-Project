# run_all.py
# Purpose: Main menu to run different parts of the IDS project
# Author:SKAND SHARMA


# Import os to run other Python files
import os


# Show menu
print("\n" + "=" * 50)
print("INTRUSION DETECTION SYSTEM - MAIN MENU")
print("=" * 50)
print("\nWhat do you want to do?")
print("1. Download dataset")
print("2. Explore dataset")
print("3. Preprocess data")
print("4. Train ML model")
print("5. Start real-time detection")
print("6. Generate report")
print("7. Exit")


# Get user choice
choice = input("\nEnter choice (1-7): ")


# Run the chosen script
if choice == '1':
    # Download NSL-KDD dataset
    os.system('python download_dataset.py')

elif choice == '2':
    # Show dataset information
    os.system('python explore_data.py')

elif choice == '3':
    # Clean and prepare data
    os.system('python preprocess_data.py')

elif choice == '4':
    # Train Random Forest model
    os.system('python train_model.py')

elif choice == '5':
    # Capture packets and detect attacks
    os.system('python realtime_detector.py')

elif choice == '6':
    # Generate summary report
    os.system('python generate_report.py')

elif choice == '7':
    # Exit the program
    print("Goodbye!")

else:
    # If user enters wrong choice
    print("Invalid choice. Please run again and enter 1-7")