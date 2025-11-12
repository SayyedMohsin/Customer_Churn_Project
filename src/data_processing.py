# src/data_processing.py
import pandas as pd
import numpy as np
import os
import sys

# Add parent directory to path
sys.path.append('..')

class DataProcessor:
    def __init__(self, data_path):
        """Initialize data processor"""
        try:
            self.df = pd.read_csv(data_path)
            print(f"✅ Data loaded successfully! Shape: {self.df.shape}")
        except FileNotFoundError:
            print(f"❌ File not found: {data_path}")
            print("📁 Available files in data/raw:")
            if os.path.exists('data/raw'):
                print(os.listdir('data/raw'))
            raise
    
    def clean_data(self):
        """Data cleaning and preprocessing"""
        print("🧹 Starting data cleaning process...")
        
        # Create a copy
        df_clean = self.df.copy()
        
        # Display initial info
        print(f"📊 Initial data shape: {df_clean.shape}")
        print(f"🔍 Initial missing values: {df_clean.isnull().sum().sum()}")
        
        # 1. Handle TotalCharges - empty strings ko NaN mein convert karenge
        print("1. Processing TotalCharges column...")
        df_clean['TotalCharges'] = pd.to_numeric(df_clean['TotalCharges'], errors='coerce')
        
        # Check missing values after conversion
        missing_total = df_clean['TotalCharges'].isnull().sum()
        print(f"   Missing values in TotalCharges: {missing_total}")
        
        # Fill missing values with median
        if missing_total > 0:
            median_val = df_clean['TotalCharges'].median()
            df_clean['TotalCharges'].fillna(median_val, inplace=True)
            print(f"   Filled {missing_total} missing values with median: {median_val:.2f}")
        
        # 2. Convert SeniorCitizen to categorical
        print("2. Converting SeniorCitizen to categorical...")
        df_clean['SeniorCitizen'] = df_clean['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
        
        # 3. Convert Churn to binary (1/0)
        print("3. Converting target variable...")
        df_clean['Churn'] = df_clean['Churn'].map({'Yes': 1, 'No': 0})
        
        # 4. Drop customerID (not useful for modeling)
        print("4. Dropping customerID column...")
        df_clean.drop('customerID', axis=1, inplace=True, errors='ignore')
        
        # Final check
        print(f"📊 Final data shape: {df_clean.shape}")
        print(f"🔍 Final missing values: {df_clean.isnull().sum().sum()}")
        
        # Display data types
        print("\n📋 Final Data Types:")
        print(df_clean.dtypes)
        
        print("✅ Data cleaning completed successfully!")
        return df_clean
    
    def save_cleaned_data(self, cleaned_df, save_path):
        """Save cleaned dataset"""
        # Ensure directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        cleaned_df.to_csv(save_path, index=False)
        print(f"💾 Cleaned data saved to: {save_path}")
        print(f"📁 File size: {os.path.getsize(save_path)} bytes")

def main():
    """Main function to run data processing"""
    print("🎯 Starting Agile Sprint 1: Data Processing")
    print("=" * 50)
    
    try:
        # Process data
        raw_data_path = 'data/raw/telco_churn_raw.csv'
        processor = DataProcessor(raw_data_path)
        cleaned_data = processor.clean_data()
        
        # Save cleaned data
        processed_data_path = 'data/processed/cleaned_churn_data.csv'
        processor.save_cleaned_data(cleaned_data, processed_data_path)
        
        print("\n🎉 Data processing completed successfully!")
        print("📋 Next: Run EDA in Jupyter Notebook")
        
    except Exception as e:
        print(f"❌ Error in data processing: {e}")
        print("💡 Please run dataset_download.py first!")

if __name__ == "__main__":
    main()