import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

class CovidEDA:
    def __init__(self, input_file):
        self.input_file = input_file
        self.df = None
        self.cleaned_df = None
        self.scaled_df = None

    def load_data(self):
        self.df = pd.read_csv(self.input_file)
        self.df = self.df[['Confirmed', 'New cases']]
        print("Loaded Data:")
        print(self.df.head())

    def compute_statistics(self):
        print("\nStatistical Measures:")
        print("Mean:\n", self.df.mean())
        print("Median:\n", self.df.median())
        print("Variance:\n", self.df.var())
        print("Standard Deviation:\n", self.df.std())
        print("Correlation Matrix:\n", self.df.corr())

    def detect_and_remove_outliers(self):
        df = self.df.copy()
        for col in ['Confirmed', 'New cases']:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            outliers = df[(df[col] < lower) | (df[col] > upper)]
            print(f"\nOutliers in {col}:")
            print(outliers)
            df = df[(df[col] >= lower) & (df[col] <= upper)]
        self.cleaned_df = df
        print("\nCleaned Data:")
        print(self.cleaned_df.head())

    def normalize_data(self):
        scaler = StandardScaler()
        scaled = scaler.fit_transform(self.cleaned_df)
        self.scaled_df = pd.DataFrame(scaled, columns=['Confirmed', 'New cases'])
        print("\nNormalized Data:")
        print(self.scaled_df.head())

    def plot_histograms(self):
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        sns.histplot(self.cleaned_df['Confirmed'], kde=True)
        plt.title('Confirmed (Cleaned)')
        plt.subplot(1, 2, 2)
        sns.histplot(self.cleaned_df['New cases'], kde=True)
        plt.title('New cases (Cleaned)')
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        sns.histplot(self.scaled_df['Confirmed'], kde=True)
        plt.title('Confirmed (Normalized)')
        plt.subplot(1, 2, 2)
        sns.histplot(self.scaled_df['New cases'], kde=True)
        plt.title('New cases (Normalized)')
        plt.tight_layout()
        plt.show()

    def plot_heatmap(self):
        plt.figure(figsize=(6, 4))
        sns.heatmap(self.cleaned_df.corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap (Cleaned Data)')
        plt.show()

if __name__ == '__main__':
    input_file = '/Users/lakshmanraghu/Downloads/AI Engineer/weekly Assignments /country_wise_latest.csv'
    eda = CovidEDA(input_file)
    eda.load_data()
    eda.compute_statistics()
    eda.detect_and_remove_outliers()
    eda.normalize_data()
    eda.plot_histograms()
    eda.plot_heatmap()
