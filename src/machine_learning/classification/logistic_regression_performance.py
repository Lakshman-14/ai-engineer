import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# ----------------------------------------------------
# 1. LOAD DATA FROM CSV
# ----------------------------------------------------
df = pd.read_csv("/Users/lakshmanraghu/Downloads/AI Engineer/LogisticRegression_sales_data.csv")

print("=== Loaded Data ===")
print(df.head())

# ----------------------------------------------------
# 2. SELECT FEATURE & LABEL COLUMNS
#    (modify below names if your CSV differs)
# ----------------------------------------------------
feature_col = "Total Amount"
label_col = "CardType"

X = df[[feature_col]]
y = df[label_col]

# ----------------------------------------------------
# 3. LABEL ENCODE THE TARGET (if it is categorical)
# ----------------------------------------------------
le = LabelEncoder()
y_encoded = le.fit_transform(y)

print("\nLabel Encoding Mapping:")
print(dict(zip(le.classes_, le.transform(le.classes_))))

# ----------------------------------------------------
# 4. TRAIN-TEST SPLIT
# ----------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.3, random_state=42
)

# ----------------------------------------------------
# 5. TRAIN LOGISTIC REGRESSION MODEL
# ----------------------------------------------------
model = LogisticRegression(class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# ----------------------------------------------------
# 6. MAKE PREDICTIONS
# ----------------------------------------------------
y_pred = model.predict(X_test)

# ----------------------------------------------------
# 7. EVALUATE METRICS
# ----------------------------------------------------
print("\n=== Model Evaluation ===")
print(f"Accuracy  : {accuracy_score(y_test, y_pred):.3f}")
print(f"Precision : {precision_score(y_test, y_pred, zero_division=0):.3f}")
print(f"Recall    : {recall_score(y_test, y_pred, zero_division=0):.3f}")
print(f"F1 Score  : {f1_score(y_test, y_pred, zero_division=0):.3f}")

print("\n=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred))

print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# ----------------------------------------------------
# 8. FIND THE DECISION THRESHOLD
# ----------------------------------------------------
threshold = -model.intercept_[0] / model.coef_[0][0]
print(f"\nDecision Threshold Learned = {threshold:.2f}")
print(f"Meaning: {feature_col} > {threshold:.2f} predicts class 1")


# ----------------------------------------------------
# 9. USER INPUT PREDICTION
# ----------------------------------------------------
new_value = float(input(f"\nEnter a new {feature_col} to classify: "))

value_array = np.array([[new_value]])

predicted_label = model.predict(value_array)
predicted_name = le.inverse_transform(predicted_label)

print(f"Prediction: {predicted_name[0]}")


