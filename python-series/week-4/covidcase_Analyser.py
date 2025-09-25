import pandas as pd
import numpy as np

class CovidDataLoader:
    """Base class for loading and basic data operations"""
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.clean_data()
    
    def clean_data(self):
        """Basic data cleaning"""
        self.data = self.data.fillna(0)  # Fill NaN values with 0
    
    def save_to_csv(self, filename):
        """Save data to CSV file"""
        self.data.to_csv(filename, index=False)

class CovidDataAnalyzer(CovidDataLoader):
    """Main class for COVID data analysis"""
    
    def summarize_by_region(self):
        """Task 1: Summarize case counts by region"""
        summary = self.data.groupby('WHO Region').agg({
            'Confirmed': 'sum',
            'Deaths': 'sum',
            'Recovered': 'sum'
        })
        return summary
    
    def filter_low_cases(self, threshold=10):
        """Task 2: Filter out entries with low case counts"""
        return self.data[self.data['Confirmed'] >= threshold]
    
    def highest_confirmed_region(self):
        """Task 3: Identify region with highest confirmed cases"""
        region_cases = self.data.groupby('WHO Region')['Confirmed'].sum()
        return region_cases.idxmax(), region_cases.max()
    
    def sort_by_confirmed_cases(self, save_file='sorted_covid_data.csv'):
        """Task 4: Sort data by confirmed cases and save to CSV"""
        sorted_data = self.data.sort_values('Confirmed', ascending=False)
        sorted_data.to_csv(save_file, index=False)
        return sorted_data
    
    def top_5_countries(self):
        """Task 5: Get top 5 countries by case count"""
        return self.data.nlargest(5, 'Confirmed')[['Country/Region', 'Confirmed']]
    
    def lowest_death_region(self):
        """Task 6: Find region with lowest death count"""
        region_deaths = self.data.groupby('WHO Region')['Deaths'].sum()
        return region_deaths.idxmin(), region_deaths.min()
    
    def india_summary(self):
        """Task 7: Get India's case summary"""
        return self.data[self.data['Country/Region'] == 'India'].iloc[0]
    
    def mortality_rate_by_region(self):
        """Task 8: Calculate mortality rate by region"""
        mortality = self.data.groupby('WHO Region').apply(
            lambda x: (x['Deaths'].sum() / x['Confirmed'].sum() * 100)
        )
        return mortality
    
    def compare_recovery_rates(self):
        """Task 9: Compare recovery rates across regions"""
        recovery_rates = self.data.groupby('WHO Region').apply(
            lambda x: (x['Recovered'].sum() / x['Confirmed'].sum() * 100)
        )
        return recovery_rates
    
    def detect_outliers(self):
        """Task 10: Detect outliers in case counts"""
        mean = self.data['Confirmed'].mean()
        std = self.data['Confirmed'].std()
        outliers = self.data[
            (self.data['Confirmed'] > mean + 2*std) |
            (self.data['Confirmed'] < mean - 2*std)
        ]
        return outliers
    
    def group_by_country_region(self):
        """Task 11: Group data by country and region"""
        return self.data.groupby(['WHO Region', 'Country/Region']).agg({
            'Confirmed': 'sum',
            'Deaths': 'sum',
            'Recovered': 'sum'
        })
    
    def regions_zero_recovery(self):
        """Task 12: Identify regions with zero recovered cases"""
        zero_recovery = self.data[self.data['Recovered'] == 0]
        return zero_recovery.groupby('WHO Region').size()

def main():
    # Initialize analyzer with the dataset
    file_path = "/Users/lakshmanraghu/Downloads/AI Engineer/weekly Assignments /country_wise_latest.csv"
    analyzer = CovidDataAnalyzer(file_path)
    
    # Task 1: Region Summary
    print("\n=== Region-wise Summary ===")
    print(analyzer.summarize_by_region())
    
    # Task 2: Filtered Data
    print("\n=== Filtered Data (Cases >= 10) ===")
    print(analyzer.filter_low_cases())
    
    # Task 3: Highest Confirmed Region
    region, cases = analyzer.highest_confirmed_region()
    print(f"\n=== Region with Highest Cases ===")
    print(f"Region: {region}, Cases: {cases:,}")
    
    # Task 4: Sort and Save
    print("\n=== Sorting and Saving Data ===")
    analyzer.sort_by_confirmed_cases()
    print("Data sorted and saved to 'sorted_covid_data.csv'")
    
    # Task 5: Top 5 Countries
    print("\n=== Top 5 Countries by Cases ===")
    print(analyzer.top_5_countries())
    
    # Task 6: Lowest Death Region
    region, deaths = analyzer.lowest_death_region()
    print(f"\n=== Region with Lowest Deaths ===")
    print(f"Region: {region}, Deaths: {deaths:,}")
    
    # Task 7: India Summary
    print("\n=== India's COVID Summary ===")
    print(analyzer.india_summary())
    
    # Task 8: Mortality Rates
    print("\n=== Mortality Rates by Region ===")
    print(analyzer.mortality_rate_by_region())
    
    # Task 9: Recovery Rates
    print("\n=== Recovery Rates by Region ===")
    print(analyzer.compare_recovery_rates())
    
    # Task 10: Outliers
    print("\n=== Outlier Cases ===")
    print(analyzer.detect_outliers()[['Country/Region', 'Confirmed']])
    
    # Task 11: Country-Region Groups
    print("\n=== Country-Region Grouping ===")
    print(analyzer.group_by_country_region())
    
    # Task 12: Zero Recovery Regions
    print("\n=== Regions with Zero Recovery Cases ===")
    print(analyzer.regions_zero_recovery())

if __name__ == "__main__":
    main()
