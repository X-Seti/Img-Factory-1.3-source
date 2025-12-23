#!/usr/bin/env python3
"""
Close functionality module for IMG Factory 1.5
Converted from old C++ code to Python 3
"""

from PyQt6.QtWidgets import QMessageBox
from typing import Optional


def close_img_file(main_window):
    """
    Close current IMG file - converted from old C++ code
    """
    try:
        # Check if there's a current IMG file
        current_img = getattr(main_window, 'current_img', None)
        if not current_img:
            main_window.log_message("No IMG file is currently open")
            return

        # Confirm close operation
        reply = QMessageBox.question(
            main_window,
            "Confirm Close",
            f"Close current IMG file: {getattr(current_img, 'file_path', 'Unknown')}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.No:
            main_window.log_message("Close cancelled")
            return

        # Clear the current IMG reference
        main_window.current_img = None
        
        # Clear the entries table
        entries_table = getattr(main_window.gui_layout, 'table', None)
        if entries_table:
            entries_table.setRowCount(0)

        main_window.log_message("IMG file closed")
        
    except Exception as e:
        main_window.log_message(f"Close error: {str(e)}")


def close_all_img(main_window):
    """
    Close all IMG files - converted from old C++ code
    """
    try:
        # For now, just close the current IMG file (single file mode)
        close_img_file(main_window)
        main_window.log_message("All IMG files closed")
        
    except Exception as e:
        main_window.log_message(f"Close all error: {str(e)}")


def install_close_functions(main_window):
    """
    Install close functions to main window - converted from old C++ code
    """
    main_window.close_img = lambda: close_img_file(main_window)
    main_window.close_all = lambda: close_all_img(main_window)
    main_window.log_message("Close functions installed")


def setup_close_manager(main_window):
    """
    Setup close manager - converted from old C++ code
    """
    install_close_functions(main_window)
    main_window.log_message("Close manager setup completed")