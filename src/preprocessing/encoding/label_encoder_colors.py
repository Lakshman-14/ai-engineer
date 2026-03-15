from sklearn.preprocessing import LabelEncoder

# Create a LabelEncoder instance
le = LabelEncoder()

# Fit the encoder with a list of labels
le.fit(['RED', 'red', 'YELOW', 'yellow', 'BLUE', 'blue', 'Red', 'Yellow'])

# Transform the labels into numerical values
encoded_labels = le.transform(['RED', 'red', 'YELOW', 'yellow', 'BLUE', 'blue', 'Red', 'Yellow'])
print(encoded_labels)

# Inverse transform to get the original labels back
original_labels = le.inverse_transform(encoded_labels)
print(original_labels)

# Show all unique labels and their encodings
print("\nAll unique labels and their encodings:")
for label in ['BLUE', 'RED', 'YELOW', 'blue', 'red', 'yellow', 'Red', 'Yellow']:
    encoded = le.transform([label])
    print(f"{label} -> {encoded[0]}")
