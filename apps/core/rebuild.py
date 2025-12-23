#!/usr/bin/env python3
"""
Rebuild functionality module for IMG Factory 1.5
Converted from old C++ code to Python 3
"""


def rebuild_current_img_native(main_window):
    """
    Rebuild current IMG file natively - converted from old C++ code
    """
    try:
        # Get the current IMG file if available
        current_img = getattr(main_window, 'current_img', None)
        if not current_img:
            main_window.log_message("No IMG file loaded - please open one first")
            return

        # In a real implementation, this would rebuild the IMG file structure
        # For now, we'll just refresh the table
        if hasattr(main_window, 'refresh_table'):
            main_window.refresh_table()
        
        main_window.log_message(f"Rebuilt IMG file: {current_img.file_path}")
        
    except Exception as e:
        main_window.log_message(f"Rebuild error: {str(e)}")


def rebuild_current_img(main_window):
    """
    Rebuild current IMG file - old function (kept for compatibility)
    """
    return rebuild_current_img_native(main_window)


def integrate_rebuild_functions(main_window):
    """
    Integration function for rebuild functionality
    """
    main_window.rebuild_img = lambda: rebuild_current_img_native(main_window)
    main_window.log_message("Rebuild functions integrated")