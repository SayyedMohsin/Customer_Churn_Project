# check_models.py - Ye file banayein aur run karen
import os
import joblib

print("🔍 Checking model files...")

model_path = 'models/trained_models/random_forest_advanced.pkl'
preprocessor_path = 'models/trained_models/preprocessor.pkl'

print(f"Model path: {model_path}")
print(f"Exists: {os.path.exists(model_path)}")

print(f"Preprocessor path: {preprocessor_path}") 
print(f"Exists: {os.path.exists(preprocessor_path)}")

if os.path.exists(model_path):
    try:
        model = joblib.load(model_path)
        print("✅ Model successfully loaded!")
        print(f"Model type: {type(model)}")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
else:
    print("❌ Model file not found!")