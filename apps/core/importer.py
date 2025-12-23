#!/usr/bin/env python3
"""
Import functionality module for IMG Factory 1.5
Converted from old C++ code to Python 3
"""

from PyQt6.QtWidgets import QFileDialog, QMessageBox
import os
from typing import List, Optional


def import_files_function(main_window):
    """
    Import files functionality - converted from old C++ code
    """
    try:
        # Get the current IMG file if available
        current_img = getattr(main_window, 'current_img', None)
        if not current_img:
            main_window.log_message("No IMG file loaded - please open one first")
            return

        # Open file dialog to select files to import
        file_paths, _ = QFileDialog.getOpenFileNames(
            main_window,
            "Select files to import",
            "",
            "All Files (*.*)"
        )

        if not file_paths:
            main_window.log_message("Import cancelled")
            return

        # Process each selected file
        imported_count = 0
        for file_path in file_paths:
            try:
                # Extract filename
                filename = os.path.basename(file_path)
                
                # Add the file to the current IMG
                if hasattr(current_img, 'add_entry'):
                    current_img.add_entry(filename, file_path)
                    imported_count += 1
                else:
                    main_window.log_message(f"Could not add {filename} - no add_entry method")
            except Exception as e:
                main_window.log_message(f"Error importing {file_path}: {str(e)}")

        main_window.log_message(f"Successfully imported {imported_count} files")
        
        # Refresh the table to show new entries
        if hasattr(main_window, 'refresh_table'):
            main_window.refresh_table()
        
    except Exception as e:
        main_window.log_message(f"Import error: {str(e)}")
        QMessageBox.critical(main_window, "Import Error", f"Failed to import files: {str(e)}")


def integrate_import_functions(main_window):
    """
    Integration function for import functionality
    """
    main_window.import_files = lambda: import_files_function(main_window)
    main_window.log_message("Import functions integrated")


# For backward compatibility
def import_via_function(main_window):
    """
    Import via IDE file functionality
    """
    main_window.log_message("Import via IDE functionality not yet implemented")