#!/usr/bin/env python3
"""
GUI Search functionality for IMG Factory 1.5
Converted from old C++ code to Python 3
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, 
    QPushButton, QTableWidget, QTableWidgetItem, 
    QLabel, QCheckBox
)
from PyQt6.QtCore import Qt
from typing import List, Dict, Any


class ASearchDialog(QDialog):
    """
    Search dialog for IMG Factory - converted from old C++ code
    """
    def __init__(self, parent=None, table=None):
        super().__init__(parent)
        self.table = table
        self.setWindowTitle("Search Entries")
        self.resize(500, 400)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the search dialog UI"""
        layout = QVBoxLayout()
        
        # Search input
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter search term...")
        self.search_input.textChanged.connect(self.on_search_changed)
        
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.perform_search)
        
        search_layout.addWidget(QLabel("Search:"))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        
        layout.addLayout(search_layout)
        
        # Case sensitive checkbox
        self.case_sensitive = QCheckBox("Case Sensitive")
        layout.addWidget(self.case_sensitive)
        
        # Results table
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(3)
        self.results_table.setHorizontalHeaderLabels(["Name", "Size", "Type"])
        layout.addWidget(self.results_table)
        
        # Buttons
        button_layout = QHBoxLayout()
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        button_layout.addWidget(close_button)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def on_search_changed(self, text):
        """Handle search text changes"""
        if text:
            self.perform_search()
    
    def perform_search(self):
        """Perform the search operation"""
        search_term = self.search_input.text()
        if not search_term or not self.table:
            return
        
        case_sensitive = self.case_sensitive.isChecked()
        if not case_sensitive:
            search_term = search_term.lower()
        
        # Clear results table
        self.results_table.setRowCount(0)
        
        # Search through the main table
        for row in range(self.table.rowCount()):
            match_found = False
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item:
                    text = item.text()
                    if not case_sensitive:
                        text = text.lower()
                    
                    if search_term in text:
                        match_found = True
                        break
            
            if match_found:
                # Add matching row to results
                current_row = self.results_table.rowCount()
                self.results_table.setRowCount(current_row + 1)
                
                for col in range(min(3, self.table.columnCount())):
                    item = self.table.item(row, col)
                    if item:
                        self.results_table.setItem(current_row, col, QTableWidgetItem(item.text()))


class SearchManager:
    """
    Search manager for IMG Factory - converted from old C++ code
    """
    def __init__(self, main_window):
        self.main_window = main_window
        self.search_dialog = None
    
    def show_search_dialog(self):
        """Show the search dialog"""
        if not self.search_dialog:
            entries_table = getattr(self.main_window.gui_layout, 'table', None)
            self.search_dialog = ASearchDialog(self.main_window, entries_table)
        
        self.search_dialog.show()
        self.search_dialog.raise_()
        self.search_dialog.activateWindow()


def integrate_search_functions(main_window):
    """
    Integration function for search functionality
    """
    search_manager = SearchManager(main_window)
    main_window.show_search = lambda: search_manager.show_search_dialog()
    main_window.log_message("Search functions integrated")