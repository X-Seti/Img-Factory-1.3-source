#!/usr/bin/env python3
"""
Rename functionality module for IMG Factory 1.5
Converted from old C++ code to Python 3
"""

from PyQt6.QtWidgets import QInputDialog, QMessageBox
from typing import Optional


def rename_entry(main_window):
    """
    Rename selected entry - converted from old C++ code
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
            main_window.log_message("No entries selected for renaming")
            return

        # Get the first selected row
        selected_row = selected_items[0].row()
        old_name_item = entries_table.item(selected_row, 0)
        if not old_name_item:
            main_window.log_message("Could not get selected entry name")
            return

        old_name = old_name_item.text()

        # Get new name from user
        new_name, ok = QInputDialog.getText(
            main_window,
            "Rename Entry",
            f"Enter new name for '{old_name}':",
            text=old_name
        )

        if not ok or not new_name:
            main_window.log_message("Rename cancelled")
            return

        # Rename the entry in the IMG file
        if hasattr(current_img, 'rename_entry'):
            if current_img.rename_entry(old_name, new_name):
                # Update the table
                old_name_item.setText(new_name)
                main_window.log_message(f"Renamed '{old_name}' to '{new_name}'")
            else:
                main_window.log_message(f"Failed to rename '{old_name}' to '{new_name}'")
        else:
            # If rename_entry method doesn't exist, try to simulate it
            # Remove old entry and add new one
            if hasattr(current_img, 'remove_entry') and hasattr(current_img, 'add_entry'):
                # This is a workaround for the placeholder implementation
                current_img.entries = [
                    entry for entry in current_img.entries 
                    if entry['name'] != old_name
                ]
                current_img.entries.append({
                    'name': new_name,
                    'size': next((e['size'] for e in current_img.entries if e['name'] == old_name), 0),
                    'type': next((e['type'] for e in current_img.entries if e['name'] == old_name), 'UNKNOWN')
                })
                
                # Update the table
                old_name_item.setText(new_name)
                main_window.log_message(f"Renamed '{old_name}' to '{new_name}' (simulated)")
            else:
                main_window.log_message(f"Could not rename {old_name} - no rename method available")

    except Exception as e:
        main_window.log_message(f"Rename error: {str(e)}")
        QMessageBox.critical(main_window, "Rename Error", f"Failed to rename entry: {str(e)}")


def integrate_rename_functions(main_window):
    """
    Integration function for rename functionality
    """
    main_window.rename_entry = lambda: rename_entry(main_window)
    main_window.log_message("Rename functions integrated")