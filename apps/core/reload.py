#!/usr/bin/env python3
"""
Reload functionality module for IMG Factory 1.5
Converted from old C++ code to Python 3
"""


def reload_current_file(main_window):
    """
    Reload current file - converted from old C++ code
    """
    try:
        # Get the current IMG file if available
        current_img = getattr(main_window, 'current_img', None)
        if not current_img:
            main_window.log_message("No IMG file loaded - please open one first")
            return

        # Get the file path to reload
        file_path = getattr(current_img, 'file_path', None)
        if not file_path:
            main_window.log_message("No file path available to reload")
            return

        # Reopen the same file
        from .open import _detect_and_open_file
        _detect_and_open_file(main_window, file_path)
        
        main_window.log_message(f"Reloaded file: {file_path}")
        
    except Exception as e:
        main_window.log_message(f"Reload error: {str(e)}")


def integrate_reload_functions(main_window):
    """
    Integration function for reload functionality
    """
    main_window.reload_file = lambda: reload_current_file(main_window)
    main_window.log_message("Reload functions integrated")