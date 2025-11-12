# deploy.py
import os
import sys
import subprocess
import webbrowser
from datetime import datetime

def check_dependencies():
    """Check if all required packages are installed"""
    required_packages = [
        'flask', 'pandas', 'numpy', 'scikit-learn', 
        'matplotlib', 'seaborn', 'joblib', 'xgboost'
    ]
    
    print("🔍 Checking dependencies...")
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"   ✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"   ❌ {package}")
    
    if missing_packages:
        print(f"\n❌ Missing packages: {missing_packages}")
        print("💡 Install them using: pip install " + " ".join(missing_packages))
        return False
    
    print("✅ All dependencies installed!")
    return True

def start_application():
    """Start the Flask application"""
    print("\n🚀 Starting Customer Churn Prediction Application...")
    
    # Change to app directory
    os.chdir('app')
    
    # Start Flask application
    try:
        print("🌐 Starting web server on http://localhost:5000")
        print("📱 Open your browser and go to the above URL")
        print("⏹️  Press Ctrl+C to stop the server")
        
        # Open browser automatically
        webbrowser.open('http://localhost:5000')
        
        # Start Flask app
        os.system('python app.py')
        
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")

def main():
    """Main deployment function"""
    print("🎯 Customer Churn Prediction - Deployment Script")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Start application
    start_application()

if __name__ == "__main__":
    main()