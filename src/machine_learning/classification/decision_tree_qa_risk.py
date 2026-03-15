import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, r2_score

# -------------------------------
# Step 1: Dataset
# -------------------------------
data = {
    'Test_Coverage': [90, 85, 70, 60, 95, 50, 80, 65],
    'Open_Defects': [2, 4, 10, 15, 1, 18, 5, 12],
    'Automation': [80, 75, 60, 50, 90, 40, 70, 55],
    'Risk': [0, 0, 1, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)

X = df[['Test_Coverage', 'Open_Defects', 'Automation']]
y = df['Risk']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# -------------------------------
# Step 2: Decision Tree (Gini)
# -------------------------------
gini_model = DecisionTreeClassifier(criterion='gini', random_state=42)
gini_model.fit(X_train, y_train)
gini_pred = gini_model.predict(X_test)
print("\nAccuracy using Gini:", accuracy_score(y_test, gini_pred))

# -------------------------------
# Step 3: Decision Tree (Entropy)
# -------------------------------
entropy_model = DecisionTreeClassifier(criterion='entropy', random_state=42)
entropy_model.fit(X_train, y_train)
entropy_pred = entropy_model.predict(X_test)
print("Accuracy using Entropy:", accuracy_score(y_test, entropy_pred))

# -------------------------------
# Step 4: Pruning
# -------------------------------
pruned_model = DecisionTreeClassifier(
    criterion='gini',
    max_depth=2,
    random_state=42
)
pruned_model.fit(X_train, y_train)
pruned_pred = pruned_model.predict(X_test)
print("Accuracy after Pruning:", accuracy_score(y_test, pruned_pred))

# -------------------------------
# Step 5: Decision Tree Regressor
# -------------------------------
regressor_model = DecisionTreeRegressor(random_state=42)
regressor_model.fit(X_train, y_train)
regressor_pred = regressor_model.predict(X_test)

print("\nRegressor MSE:", mean_squared_error(y_test, regressor_pred))
print("Regressor R²:", r2_score(y_test, regressor_pred))
