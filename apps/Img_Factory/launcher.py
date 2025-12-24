#!/usr/bin/env python3
"""
Img Factory 1.5 Launcher
X-Seti - December24 2025 - IMG Factory 1.5 - Main Application Launcher
Connects GUI layout with converted methods
"""

import sys
import os
from PyQt6.QtWidgets import QApplication

# Add the apps directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'apps'))

from gui.main_window import IMGFactoryMainWindow  # Import the main window class


def main():
    """Main entry point for the application"""
    app = QApplication(sys.argv)
    
    # Create and show the main window using the preserved GUI layout
    main_window = MainWindow()
    main_window.show()
    
    # Start the event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()