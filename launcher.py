#!/usr/bin/env python3
"""
Img Factory 1.5 Root Launcher
X-Seti - December24 2025 - IMG Factory 1.5 - Root Application Launcher
Connects GUI layout with converted methods
"""

import sys
import os

# Add the apps directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'apps'))

from gui.main_window import IMGFactoryMainWindow  # Import the main window class


def main():
    """Main entry point for the application"""
    app = QApplication(sys.argv)
    
    # Create and show the main window using the preserved GUI layout
    main_window = IMGFactoryMainWindow()
    main_window.show()
    
    # Start the event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    main()