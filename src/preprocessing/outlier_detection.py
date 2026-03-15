import pandas as pd

# File paths
input_file = '/Users/lakshmanraghu/Downloads/AI Engineer/EDA/SalesDataset1.csv'
outliers_file = 'outliers.csv'
cleaned_file = 'cleaned_data.csv'

def find_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    cleaned = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
   # outliers_summary = outliers[["Date", "Gender", "Age", "Product Category", "Quantity", "Price per Unit", "Total Amount"]]
    print(outliers)
    print(cleaned)
    return outliers, cleaned

def main():
    # Read the dataset
    df = pd.read_csv(input_file)
    numeric_cols = df.select_dtypes(include='number').columns
    print(numeric_cols)


    all_outliers = pd.DataFrame()
    cleaned_df = df.copy()
    for col in numeric_cols:
        outliers, cleaned = find_outliers_iqr(cleaned_df, col)
        if not outliers.empty:
            outliers['Outlier_Column'] = col
            all_outliers = pd.concat([all_outliers, outliers])
        cleaned_df = cleaned

    all_outliers.to_csv(outliers_file, index=False)
    cleaned_df.to_csv(cleaned_file, index=False)

    print(f'Outliers written to {outliers_file}')
    print(f'Cleaned data written to {cleaned_file}')

if __name__ == '__main__':
    main()
