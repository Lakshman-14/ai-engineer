import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# ================================
# Step 1: Load the dataset
# ================================
df = pd.read_csv("/Users/lakshmanraghu/Downloads/AI Engineer/decisiontree.csv")

# Drop empty rows if any
df = df.dropna()

# ================================
# Step 2: Encode Categorical Features
# ================================
le_dict = {}  # Store encoders for later use

for column in df.columns:
    if df[column].dtype == 'object':
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        le_dict[column] = le

# ================================
# Step 3: Split Features & Target
# ================================
X = df.drop(['Day', 'Play'], axis=1)  # Features: Weather, Temperature, Humidity, Wind
y = df['Play']                        # Target

# ================================
# Step 4: Train Decision Tree
# ================================
model = DecisionTreeClassifier(criterion='entropy', max_depth=3)
model.fit(X, y)

# ================================
# Step 5: Visualize the Tree
# ================================
plt.figure(figsize=(12, 8))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=le_dict['Play'].classes_,
    filled=True,
    fontsize=10
)
plt.show()

# ================================
# Step 6: Predict from User Input
# ================================
def predict_play(weather, temperature, humidity, wind):

    w = le_dict['Weather'].transform([weather])[0]
    t = le_dict['Temperature'].transform([temperature])[0]
    h = le_dict['Humidity'].transform([humidity])[0]
    wi = le_dict['Wind'].transform([wind])[0]

    # Create DataFrame for prediction
    user_input = pd.DataFrame([[w, t, h, wi]], columns=X.columns)

    # Predict numeric
    prediction = model.predict(user_input)[0]

    # Convert numeric prediction back to label
    return le_dict['Play'].inverse_transform([prediction])[0]


# ================================
# Example Predictions
# ================================
print("="*60)
print("PREDICTIONS:")
print("="*60)
print(f"Rain, Mild, High, Weak        → predict_play = {predict_play('Rain', 'Mild', 'High', 'Weak')}")
print(f"Rain, Mild, High, Strong      → predict_play = {predict_play('Rain', 'Mild', 'High', 'Strong')}")
print(f"Sunny, Hot, High, Weak        → predict_play = {predict_play('Sunny', 'Hot', 'High', 'Weak')}")
print(f"Cloudy, Cool, Normal, Strong  → predict_play = {predict_play('Cloudy', 'Cool', 'Normal', 'Strong')}")
print("="*60)
