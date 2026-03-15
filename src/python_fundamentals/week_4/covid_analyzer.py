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

    def save_all_analysis(self, output_file='covid_complete_analysis.csv'):
        """Save all analysis results to a single CSV file in a structured format"""
        # Create lists to store results
        analysis_results = []

        # Task 1: Region Summary
        region_summary = self.summarize_by_region()
        for region in region_summary.index:
            analysis_results.append({
                'Task': 'Region Summary',
                'Region': region,
                'Confirmed': region_summary.loc[region, 'Confirmed'],
                'Deaths': region_summary.loc[region, 'Deaths'],
                'Recovered': region_summary.loc[region, 'Recovered'],
                'Details': 'Summary of cases by region'
            })

        # Task 2: High Case Countries
        filtered_data = self.filter_low_cases()
        analysis_results.append({
            'Task': 'High Case Countries',
            'Region': 'All',
            'Confirmed': 'N/A',
            'Deaths': 'N/A',
            'Recovered': 'N/A',
            'Details': f'Countries with ≥10 cases: {len(filtered_data)}'
        })

        # Task 3: Highest Confirmed Region
        region, cases = self.highest_confirmed_region()
        analysis_results.append({
            'Task': 'Highest Confirmed Region',
            'Region': region,
            'Confirmed': cases,
            'Deaths': 'N/A',
            'Recovered': 'N/A',
            'Details': f'Region with most confirmed cases'
        })

        # Task 4: Sorted Cases (Top 5)
        sorted_data = self.sort_by_confirmed_cases()
        for _, row in sorted_data.head().iterrows():
            analysis_results.append({
                'Task': 'Sorted Cases (Top 5)',
                'Region': row['Country/Region'],
                'Confirmed': row['Confirmed'],
                'Deaths': row['Deaths'],
                'Recovered': row['Recovered'],
                'Details': 'Countries sorted by confirmed cases'
            })

        # Task 5: Top 5 Countries
        top_5 = self.top_5_countries()
        for _, row in top_5.iterrows():
            analysis_results.append({
                'Task': 'Top 5 Countries',
                'Region': row['Country/Region'],
                'Confirmed': row['Confirmed'],
                'Deaths': 'N/A',
                'Recovered': 'N/A',
                'Details': 'Top 5 countries by confirmed cases'
            })

        # Task 6: Lowest Death Region
        region, deaths = self.lowest_death_region()
        analysis_results.append({
            'Task': 'Lowest Death Region',
            'Region': region,
            'Confirmed': 'N/A',
            'Deaths': deaths,
            'Recovered': 'N/A',
            'Details': 'Region with lowest death count'
        })

        # Task 7: India Summary
        india_data = self.india_summary()
        analysis_results.append({
            'Task': 'India Summary',
            'Region': 'India',
            'Confirmed': india_data['Confirmed'],
            'Deaths': india_data['Deaths'],
            'Recovered': india_data['Recovered'],
            'Details': 'COVID-19 summary for India'
        })

        # Task 8: Mortality Rates
        mortality_rates = self.mortality_rate_by_region()
        for region, rate in mortality_rates.items():
            analysis_results.append({
                'Task': 'Mortality Rates',
                'Region': region,
                'Confirmed': 'N/A',
                'Deaths': 'N/A',
                'Recovered': 'N/A',
                'Details': f'Mortality Rate: {rate:.2f}%'
            })

        # Task 9: Recovery Rates
        recovery_rates = self.compare_recovery_rates()
        for region, rate in recovery_rates.items():
            analysis_results.append({
                'Task': 'Recovery Rates',
                'Region': region,
                'Confirmed': 'N/A',
                'Deaths': 'N/A',
                'Recovered': 'N/A',
                'Details': f'Recovery Rate: {rate:.2f}%'
            })

        # Task 10: Outliers
        outliers = self.detect_outliers()
        for _, row in outliers.iterrows():
            analysis_results.append({
                'Task': 'Outliers',
                'Region': row['Country/Region'],
                'Confirmed': row['Confirmed'],
                'Deaths': 'N/A',
                'Recovered': 'N/A',
                'Details': 'Countries with unusual case counts'
            })

        # Task 11: Country-Region Groups
        grouped_data = self.group_by_country_region()
        for (region, country), data in grouped_data.iterrows():
            analysis_results.append({
                'Task': 'Country-Region Groups',
                'Region': f'{region} - {country}',
                'Confirmed': data['Confirmed'],
                'Deaths': data['Deaths'],
                'Recovered': data['Recovered'],
                'Details': 'Grouped statistics by country and region'
            })

        # Task 12: Zero Recovery Regions
        zero_recovery = self.regions_zero_recovery()
        for region, count in zero_recovery.items():
            analysis_results.append({
                'Task': 'Zero Recovery Regions',
                'Region': region,
                'Confirmed': 'N/A',
                'Deaths': 'N/A',
                'Recovered': 0,
                'Details': f'Number of zero recovery cases: {count}'
            })

        # Convert to DataFrame and save
        results_df = pd.DataFrame(analysis_results)
        results_df.to_csv(output_file, index=False)
        print(f"\nAnalysis results have been saved to: {output_file}")
        return results_df

def main():
    # Initialize analyzer with the dataset
    file_path = "/Users/lakshmanraghu/Downloads/AI Engineer/weekly Assignments /country_wise_latest.csv"
    analyzer = CovidDataAnalyzer(file_path)
    
    # Save all analysis results to a single CSV file
    print("\n=== Saving All Analysis Results ===")
    analyzer.save_all_analysis('covid_complete_analysis.csv')
    print("All analysis results have been saved to 'covid_complete_analysis.csv'")
    
    # Display summary of results
    print("\nAnalysis Summary:")
    print("=" * 50)
    
    # Task 1-3
    region, cases = analyzer.highest_confirmed_region()
    print(f"Highest Cases Region: {region} with {cases:,} cases")
    
    # Task 5
    print("\nTop 5 Countries by Cases:")
    print(analyzer.top_5_countries())
    
    # Task 6
    region, deaths = analyzer.lowest_death_region()
    print(f"\nLowest Deaths Region: {region} with {deaths:,} deaths")
    
    # Task 8-9
    print("\nMortality Rates by Region:")
    print(analyzer.mortality_rate_by_region())
    
    print("\nRecovery Rates by Region:")
    print(analyzer.compare_recovery_rates())

if __name__ == "__main__":
    main()