# performance_checker.py
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import accuracy_score, classification_report
import os

print("🔍 Checking Actual Model Performance...")
print("=" * 50)

# Load data and model
try:
    # Load engineered data
    df = pd.read_csv('data/processed/engineered_churn_data.csv')
    print(f"✅ Data loaded: {df.shape}")
    
    # Load model
    model_path = 'models/trained_models/random_forest_advanced.pkl'
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        print("✅ Model loaded successfully!")
        
        # Prepare data for testing
        from sklearn.preprocessing import LabelEncoder
        df_encoded = df.copy()
        
        # Encode categorical variables
        categorical_cols = df_encoded.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            le = LabelEncoder()
            df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
        
        X = df_encoded.drop('Churn', axis=1)
        y = df_encoded['Churn']
        
        # Split data
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Make predictions
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"🎯 ACTUAL MODEL ACCURACY: {accuracy:.4f} ({accuracy*100:.2f}%)")
        print(f"📊 Test set size: {len(y_test)} samples")
        
        # Detailed report
        print("\n📋 Classification Report:")
        print(classification_report(y_test, y_pred))
        
    else:
        print("❌ Model file not found!")
        
except Exception as e:
    print(f"❌ Error: {e}")