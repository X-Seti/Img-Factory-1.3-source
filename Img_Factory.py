#!/usr/bin/env python3
"""
Img Factory 1.5 - Main Launcher
X-Seti - December24 2025 - Img Factory 1.5 - Main Application Launcher

This is the main entry point for the Img Factory application.
"""

import sys
import os

# Add the apps directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'apps'))

def main():
    """Main entry point for Img Factory 1.5"""
    print("Img Factory 1.5 - Starting Application...")
    
    try:
        # Run the main application directly
        import subprocess
        import sys
        result = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), 'apps', 'Img_Factory', 'Img_Factory.py')])
        
        if result.returncode != 0:
            print("Error: Img Factory application exited with an error.")
            sys.exit(result.returncode)
        
    except Exception as e:
        print(f"Error starting Img Factory: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()