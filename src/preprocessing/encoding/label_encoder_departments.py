from sklearn.preprocessing import LabelEncoder

# Create a LabelEncoder instance
le = LabelEncoder()

# Fit the encoder with a list of labels
le.fit(["Hardware", "Software", "HR", "Finance"])
# Finance - 0, HR - 1, Hardware - 2, Software - 3

# Transform the labels into numerical values
encoded_labels = le.transform(["Software", "HR", "Hardware"])
print(encoded_labels)  # Output: array([3, 1, 2])

# Inverse transform to get the original labels back
original_labels = le.inverse_transform([3, 1, 2])
print(original_labels)  # Output: ['Software' 'HR' 'Hardware']
