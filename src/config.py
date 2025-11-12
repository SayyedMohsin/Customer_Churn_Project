# src/config.py
# Project configuration

# Paths
DATA_RAW_PATH = 'data/raw/telco_churn_raw.csv'
DATA_PROCESSED_PATH = 'data/processed/cleaned_churn_data.csv'
MODELS_PATH = 'models/trained_models/'

# Model parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2

# Feature names
NUMERICAL_FEATURES = ['tenure', 'MonthlyCharges', 'TotalCharges']
CATEGORICAL_FEATURES = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 
                       'PhoneService', 'MultipleLines', 'InternetService']