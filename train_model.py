# train_model.py
# Purpose: Trains Random Forest model to detect network attacks
# Author: SKAND SHARMA


# Import libraries
import pandas as pd                                       # For data handling
import pickle                                             # For saving model
from sklearn.ensemble import RandomForestClassifier      # The ML algorithm
from sklearn.metrics import accuracy_score                # To check accuracy
from sklearn.metrics import confusion_matrix              # To see predictions


# Step 1: Load preprocessed data
# These files were created by preprocess_data.py
print("Step 1: Loading preprocessed data...")
X_train = pd.read_csv('data/processed/X_train.csv')
X_test = pd.read_csv('data/processed/X_test.csv')
y_train = pd.read_csv('data/processed/y_train.csv')
y_test = pd.read_csv('data/processed/y_test.csv')


# Step 2: Convert labels to 1D array
# sklearn needs labels in 1D format
# .values.ravel() does this conversion
print("Step 2: Preparing labels...")
y_train = y_train.values.ravel()
y_test = y_test.values.ravel()


# Step 3: Create the Random Forest model
# Random Forest is an ensemble of decision trees
# n_estimators=100 means we use 100 trees
# More trees = better accuracy but slower training
# random_state=42 makes results same every time
print("Step 3: Creating Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)


# Step 4: Train the model
# This is where the model learns patterns from data
# It looks at features and learns which patterns mean 'attack'
# Takes 1-2 minutes depending on computer speed
print("Step 4: Training model... (this takes 1-2 minutes)")
model.fit(X_train, y_train)
print("Training complete!")


# Step 5: Test the model
# Use model to predict on test data
# Test data has answers but model doesn't know them
# This tells us how good our model is
print("Step 5: Testing model on test data...")
predictions = model.predict(X_test)


# Step 6: Calculate accuracy
# Accuracy = correct predictions / total predictions
# Multiply by 100 to get percentage
print("Step 6: Calculating accuracy...")
accuracy = accuracy_score(y_test, predictions)
accuracy_percent = round(accuracy * 100, 2)
print("Accuracy:", accuracy_percent, "%")


# Step 7: Show confusion matrix
# Confusion matrix shows where model got confused
# Format:
#   [[True Negatives, False Positives],
#    [False Negatives, True Positives]]
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))


# Step 8: Save the trained model
# We save it so we can use it later without retraining
# Pickle is Python's way of saving objects to file
print("\nStep 8: Saving model to file...")
with open('models/ids_model.pkl', 'wb') as f:
    pickle.dump(model, f)


# Final message
print("Model saved to: models/ids_model.pkl")
print("Training complete! Ready for real-time detection.")