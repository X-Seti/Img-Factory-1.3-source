#!/usr/bin/env python3
"""
Remove functionality module for IMG Factory 1.5
Converted from old C++ code to Python 3
"""

from PyQt6.QtWidgets import QMessageBox
from typing import List, Optional


def remove_selected_function(main_window):
    """
    Remove selected entries functionality - converted from old C++ code
    """
    try:
        # Get the current IMG file if available
        current_img = getattr(main_window, 'current_img', None)
        if not current_img:
            main_window.log_message("No IMG file loaded - please open one first")
            return

        # Get selected items from the table
        entries_table = getattr(main_window.gui_layout, 'table', None)
        if not entries_table:
            main_window.log_message("No entries table available")
            return

        selected_items = entries_table.selectedItems()
        if not selected_items:
            main_window.log_message("No entries selected for removal")
            return

        # Get unique selected rows
        selected_rows = list(set(item.row() for item in selected_items))
        
        # Confirm removal
        reply = QMessageBox.question(
            main_window,
            "Confirm Removal",
            f"Remove {len(selected_rows)} selected entries?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.No:
            main_window.log_message("Removal cancelled")
            return

        # Remove entries (process in reverse order to maintain indices)
        removed_count = 0
        for row in sorted(selected_rows, reverse=True):
            try:
                # Get the filename to remove
                filename_item = entries_table.item(row, 0)
                if filename_item:
                    filename = filename_item.text()
                    
                    # Remove the entry from the IMG file
                    if hasattr(current_img, 'remove_entry'):
                        current_img.remove_entry(filename)
                        removed_count += 1
                    else:
                        main_window.log_message(f"Could not remove {filename} - no remove_entry method")
            except Exception as e:
                main_window.log_message(f"Error removing entry at row {row}: {str(e)}")

        main_window.log_message(f"Successfully removed {removed_count} entries")
        
        # Refresh the table to show updated entries
        if hasattr(main_window, 'refresh_table'):
            main_window.refresh_table()
        
    except Exception as e:
        main_window.log_message(f"Remove error: {str(e)}")
        QMessageBox.critical(main_window, "Remove Error", f"Failed to remove entries: {str(e)}")


def remove_via_entries_function(main_window):
    """
    Remove entries via IDE file functionality
    """
    main_window.log_message("Remove via IDE functionality not yet implemented")


def integrate_remove_functions(main_window):
    """
    Integration function for remove functionality
    """
    main_window.remove_selected = lambda: remove_selected_function(main_window)
    main_window.log_message("Remove functions integrated")