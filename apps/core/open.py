#!/usr/bin/env python3
"""
Open functionality module for IMG Factory 1.5
Converted from old C++ code to Python 3
"""

from PyQt6.QtWidgets import QFileDialog, QMessageBox
import os
from typing import Optional


def open_file_dialog(main_window):
    """
    Open file dialog functionality - converted from old C++ code
    """
    try:
        # Open file dialog to select IMG file
        file_path, _ = QFileDialog.getOpenFileName(
            main_window,
            "Open IMG File",
            "",
            "IMG Files (*.img);;All Files (*.*)"
        )

        if not file_path:
            main_window.log_message("Open cancelled")
            return

        # Load the IMG file
        _detect_and_open_file(main_window, file_path)
        
    except Exception as e:
        main_window.log_message(f"Open error: {str(e)}")
        QMessageBox.critical(main_window, "Open Error", f"Failed to open file: {str(e)}")


def _detect_and_open_file(main_window, file_path: str):
    """
    Detect file type and open accordingly - converted from old C++ code
    """
    try:
        # Detect file type
        file_type = _detect_file_type(file_path)
        
        if file_type == "img":
            # Create a simple IMG file handler (placeholder for now)
            img_handler = IMGFileHandler(file_path)
            
            # Store reference to current IMG in main window
            main_window.current_img = img_handler
            
            # Load entries into the table
            _load_entries_to_table(main_window, img_handler)
            
            main_window.log_message(f"Opened IMG file: {os.path.basename(file_path)}")
            
        else:
            main_window.log_message(f"Unsupported file type: {file_type}")
            
    except Exception as e:
        main_window.log_message(f"Error opening file {file_path}: {str(e)}")


def _detect_file_type(file_path: str) -> str:
    """
    Detect file type based on extension - converted from old C++ code
    """
    _, ext = os.path.splitext(file_path.lower())
    return ext.lstrip('.')


def _load_entries_to_table(main_window, img_handler):
    """
    Load IMG entries to the table - converted from old C++ code
    """
    try:
        # Get the entries table
        entries_table = getattr(main_window.gui_layout, 'table', None)
        if not entries_table:
            main_window.log_message("No entries table available")
            return

        # Clear existing items
        entries_table.setRowCount(0)

        # Get entries from IMG handler
        entries = img_handler.get_entries()
        
        # Add entries to table
        for i, entry in enumerate(entries):
            entries_table.setRowCount(i + 1)
            entries_table.setItem(i, 0, QTableWidgetItem(entry['name']))
            entries_table.setItem(i, 1, QTableWidgetItem(str(entry['size'])))
            entries_table.setItem(i, 2, QTableWidgetItem(entry['type']))
        
        main_window.log_message(f"Loaded {len(entries)} entries")
        
    except Exception as e:
        main_window.log_message(f"Error loading entries to table: {str(e)}")


class IMGFileHandler:
    """
    Simple IMG file handler - placeholder for converted C++ functionality
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.entries = self._load_entries()
    
    def _load_entries(self):
        """
        Load entries from IMG file - converted from old C++ code
        """
        # Placeholder implementation - in real scenario this would read the IMG file format
        import os
        entries = []
        
        # For demonstration, create some fake entries if file exists
        if os.path.exists(self.file_path):
            # This is a simplified approach - real implementation would parse IMG format
            entries.append({'name': 'sample.txd', 'size': 1024, 'type': 'TXD'})
            entries.append({'name': 'model.dff', 'size': 2048, 'type': 'DFF'})
            entries.append({'name': 'collision.col', 'size': 512, 'type': 'COL'})
        
        return entries
    
    def get_entries(self):
        """
        Get all entries in the IMG file
        """
        return self.entries
    
    def add_entry(self, filename: str, file_path: str):
        """
        Add an entry to the IMG file - converted from old C++ code
        """
        # Placeholder implementation
        self.entries.append({
            'name': filename,
            'size': os.path.getsize(file_path) if os.path.exists(file_path) else 0,
            'type': os.path.splitext(filename)[1].upper().lstrip('.') or 'UNKNOWN'
        })
        return True
    
    def remove_entry(self, filename: str):
        """
        Remove an entry from the IMG file - converted from old C++ code
        """
        # Placeholder implementation
        self.entries = [entry for entry in self.entries if entry['name'] != filename]
        return True
    
    def extract_entry(self, filename: str):
        """
        Extract an entry from the IMG file - converted from old C++ code
        """
        # Placeholder implementation - return dummy data
        import io
        return b"dummy_entry_data" if any(e['name'] == filename for e in self.entries) else None


def integrate_open_functions(main_window):
    """
    Integration function for open functionality
    """
    main_window.open_file = lambda path: _detect_and_open_file(main_window, path)
    main_window.log_message("Open functions integrated")