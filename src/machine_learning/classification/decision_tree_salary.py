# =============================================================================
# Decision Tree Classification
# =============================================================================

import pandas as pd

# Load data
df = pd.read_csv("/Users/lakshmanraghu/Downloads/AI Engineer/Decision Tree/salaries.csv.xls")
print("\nDataFrame Head:")
print(df.head())

# Prepare inputs and target
inputs = df.drop('salary_more_then_100k', axis='columns')
target = df['salary_more_then_100k']

# Label Encoding
from sklearn.preprocessing import LabelEncoder

le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])

print("\nInputs with Encoded Features:")
print(inputs)

inputs_n = inputs.drop(['company', 'job', 'degree'], axis='columns')
print("\nNumeric Features Only:")
print(inputs_n)
print("\nTarget Variable:")
print(target)

# Build Decision Tree model
from sklearn import tree

model = tree.DecisionTreeClassifier()
model.fit(inputs_n, target)
print("\nModel score:", model.score(inputs_n, target))

# Is salary of Google, Computer Engineer, Bachelors degree > 100k?
print("\nGoogle, Computer Engineer, Bachelors:", model.predict([[2, 1, 0]]))

# Is salary of Google, Computer Engineer, Masters degree > 100k?
print("\nGoogle, Computer Engineer, Masters:", model.predict([[2, 1, 1]]))

# =============================================================================
# Exercise: Build decision tree model to predict survival based on certain parameters
# Using Titanic dataset with columns: Pclass, Sex, Age, Fare
# Calculate score of your model
# =============================================================================
