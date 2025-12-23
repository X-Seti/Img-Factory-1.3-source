#!/usr/bin/env python3
"""
Export functionality module for IMG Factory 1.5
Converted from old C++ code to Python 3
"""

from PyQt6.QtWidgets import QFileDialog, QMessageBox
import os
from typing import List, Optional


def export_selected_function(main_window):
    """
    Export selected entries functionality - converted from old C++ code
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
            main_window.log_message("No entries selected for export")
            return

        # Get unique selected rows
        selected_rows = list(set(item.row() for item in selected_items))
        
        # Open directory dialog to select export location
        export_dir = QFileDialog.getExistingDirectory(
            main_window,
            "Select Export Directory"
        )

        if not export_dir:
            main_window.log_message("Export cancelled")
            return

        # Export each selected entry
        exported_count = 0
        for row in selected_rows:
            try:
                # Get the filename to export
                filename_item = entries_table.item(row, 0)
                if filename_item:
                    filename = filename_item.text()
                    
                    # Export the entry from the IMG file
                    if hasattr(current_img, 'extract_entry'):
                        # Get the entry data
                        entry_data = current_img.extract_entry(filename)
                        if entry_data:
                            # Write to file
                            export_path = os.path.join(export_dir, filename)
                            with open(export_path, 'wb') as f:
                                f.write(entry_data)
                            exported_count += 1
                        else:
                            main_window.log_message(f"Could not extract {filename} - no data")
                    else:
                        main_window.log_message(f"Could not export {filename} - no extract_entry method")
            except Exception as e:
                main_window.log_message(f"Error exporting entry at row {row}: {str(e)}")

        main_window.log_message(f"Successfully exported {exported_count} entries to {export_dir}")
        
    except Exception as e:
        main_window.log_message(f"Export error: {str(e)}")
        QMessageBox.critical(main_window, "Export Error", f"Failed to export entries: {str(e)}")


def export_via_function(main_window):
    """
    Export via IDE file functionality
    """
    main_window.log_message("Export via IDE functionality not yet implemented")


def quick_export_function(main_window):
    """
    Quick export to project folder functionality
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
            main_window.log_message("No entries selected for quick export")
            return

        # Get unique selected rows
        selected_rows = list(set(item.row() for item in selected_items))
        
        # Use a default export directory (project folder)
        export_dir = os.path.join(os.path.dirname(current_img.file_path), "exported")
        os.makedirs(export_dir, exist_ok=True)

        # Export each selected entry
        exported_count = 0
        for row in selected_rows:
            try:
                # Get the filename to export
                filename_item = entries_table.item(row, 0)
                if filename_item:
                    filename = filename_item.text()
                    
                    # Export the entry from the IMG file
                    if hasattr(current_img, 'extract_entry'):
                        # Get the entry data
                        entry_data = current_img.extract_entry(filename)
                        if entry_data:
                            # Write to file
                            export_path = os.path.join(export_dir, filename)
                            with open(export_path, 'wb') as f:
                                f.write(entry_data)
                            exported_count += 1
                        else:
                            main_window.log_message(f"Could not extract {filename} - no data")
                    else:
                        main_window.log_message(f"Could not export {filename} - no extract_entry method")
            except Exception as e:
                main_window.log_message(f"Error exporting entry at row {row}: {str(e)}")

        main_window.log_message(f"Successfully quick exported {exported_count} entries to {export_dir}")
        
    except Exception as e:
        main_window.log_message(f"Quick export error: {str(e)}")


def dump_all_function(main_window):
    """
    Dump all entries functionality
    """
    try:
        # Get the current IMG file if available
        current_img = getattr(main_window, 'current_img', None)
        if not current_img:
            main_window.log_message("No IMG file loaded - please open one first")
            return

        # Get the table to see all entries
        entries_table = getattr(main_window.gui_layout, 'table', None)
        if not entries_table:
            main_window.log_message("No entries table available")
            return

        # Count total entries
        total_entries = entries_table.rowCount()
        main_window.log_message(f"IMG contains {total_entries} entries")
        
        # List all entries
        for row in range(total_entries):
            filename_item = entries_table.item(row, 0)
            if filename_item:
                filename = filename_item.text()
                main_window.log_message(f"Entry {row+1}: {filename}")
        
        main_window.log_message(f"Dump complete: {total_entries} entries listed")
        
    except Exception as e:
        main_window.log_message(f"Dump error: {str(e)}")


def integrate_export_functions(main_window):
    """
    Integration function for export functionality
    """
    main_window.export_selected = lambda: export_selected_function(main_window)
    main_window.export_via = lambda: export_via_function(main_window)
    main_window.quick_export = lambda: quick_export_function(main_window)
    main_window.dump_all = lambda: dump_all_function(main_window)
    main_window.log_message("Export functions integrated")