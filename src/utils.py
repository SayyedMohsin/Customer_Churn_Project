# src/utils.py
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

def load_model(model_path):
    """Load trained model"""
    return joblib.load(model_path)

def save_model(model, model_path):
    """Save trained model"""
    joblib.dump(model, model_path)

def plot_feature_importance(feature_importance, top_n=10):
    """Plot feature importance"""
    plt.figure(figsize=(10, 6))
    top_features = feature_importance.head(top_n)
    plt.barh(top_features['feature'], top_features['importance'])
    plt.title(f'Top {top_n} Feature Importance')
    plt.xlabel('Importance')
    plt.tight_layout()
    return plt