# dataset_download.py
import pandas as pd
import numpy as np
import os
from urllib.request import urlretrieve
import warnings
warnings.filterwarnings('ignore')

def download_dataset():
    """Dataset download karta hai aur proper folders create karta hai"""
    
    print("🚀 Starting Agile Project Setup...")
    
    # Create all required folders
    folders = [
        'data/raw',
        'data/processed', 
        'data/external',
        'notebooks',
        'src',
        'models/trained_models',
        'models/model_performance',
        'app/templates',
        'app/static',
        'docs'
    ]
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"✅ Folder created: {folder}")
    
    # Dataset URL
    dataset_url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
    
    try:
        print("📥 Downloading dataset from GitHub...")
        
        # Direct download using pandas
        df = pd.read_csv(dataset_url)
        
        # Save raw data
        raw_data_path = 'data/raw/telco_churn_raw.csv'
        df.to_csv(raw_data_path, index=False)
        
        print(f"✅ Dataset successfully downloaded!")
        print(f"📊 Dataset Shape: {df.shape}")
        print(f"💾 Saved at: {raw_data_path}")
        print(f"📁 File size: {os.path.getsize(raw_data_path)} bytes")
        
        # Display basic info
        print("\n🔍 Dataset Preview:")
        print(df.head())
        print(f"\n🎯 Target variable 'Churn' distribution:")
        print(df['Churn'].value_counts())
        
        return True
        
    except Exception as e:
        print(f"❌ Error downloading dataset: {e}")
        print("🔄 Creating sample dataset...")
        return create_sample_dataset()

def create_sample_dataset():
    """Agar download fail ho to sample dataset create karta hai"""
    print("📝 Creating sample dataset...")
    
    # Sample data create karte hain
    np.random.seed(42)
    n_samples = 1000
    
    sample_data = {
        'customerID': [f'C{str(i).zfill(5)}' for i in range(n_samples)],
        'gender': np.random.choice(['Male', 'Female'], n_samples),
        'SeniorCitizen': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]),
        'Partner': np.random.choice(['Yes', 'No'], n_samples),
        'Dependents': np.random.choice(['Yes', 'No'], n_samples),
        'tenure': np.random.randint(1, 72, n_samples),
        'PhoneService': np.random.choice(['Yes', 'No'], n_samples),
        'MultipleLines': np.random.choice(['Yes', 'No', 'No phone service'], n_samples),
        'InternetService': np.random.choice(['DSL', 'Fiber optic', 'No'], n_samples),
        'OnlineSecurity': np.random.choice(['Yes', 'No', 'No internet service'], n_samples),
        'OnlineBackup': np.random.choice(['Yes', 'No', 'No internet service'], n_samples),
        'DeviceProtection': np.random.choice(['Yes', 'No', 'No internet service'], n_samples),
        'TechSupport': np.random.choice(['Yes', 'No', 'No internet service'], n_samples),
        'StreamingTV': np.random.choice(['Yes', 'No', 'No internet service'], n_samples),
        'StreamingMovies': np.random.choice(['Yes', 'No', 'No internet service'], n_samples),
        'Contract': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_samples),
        'PaperlessBilling': np.random.choice(['Yes', 'No'], n_samples),
        'PaymentMethod': np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], n_samples),
        'MonthlyCharges': np.round(np.random.uniform(20, 120, n_samples), 2),
        'TotalCharges': np.round(np.random.uniform(50, 8000, n_samples), 2),
        'Churn': np.random.choice(['Yes', 'No'], n_samples, p=[0.25, 0.75])
    }
    
    df = pd.DataFrame(sample_data)
    raw_data_path = 'data/raw/telco_churn_raw.csv'
    df.to_csv(raw_data_path, index=False)
    
    print(f"✅ Sample dataset created with {n_samples} records!")
    print(f"💾 Saved at: {raw_data_path}")
    
    return True

if __name__ == "__main__":
    print("🎯 Agile Customer Churn Project - Initial Setup")
    print("=" * 50)
    success = download_dataset()
    if success:
        print("\n🎉 Project setup completed successfully!")
        print("📋 Next: Run data_processing.py")
    else:
        print("\n❌ Project setup failed!")