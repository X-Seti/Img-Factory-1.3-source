#this belongs in apps/debug/ debug_functions.py - Version: 1
# X-Seti - Nov21 2025 - IMG Factory 1.5 - Debugging Utilities
"""
Debugging Utilities - Provides debugging functions for IMG Factory operations.
"""

##Methods list -
# img_debugger
# col_debugger
# file_parser_debug
# log_debug_info

def img_debugger(message, level="INFO"): #vers 1
    """
    Debug function for IMG operations
    """
    import datetime
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[IMG-DEBUG {level}] {timestamp}: {message}")

def col_debugger(message, level="INFO"): #vers 1
    """
    Debug function for COL operations
    """
    import datetime
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[COL-DEBUG {level}] {timestamp}: {message}")

def file_parser_debug(message, level="INFO"): #vers 1
    """
    Debug function for file parsing operations
    """
    import datetime
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[PARSER-DEBUG {level}] {timestamp}: {message}")

def log_debug_info(obj, name="Object"): #vers 1
    """
    Log detailed information about an object
    """
    img_debugger(f"{name} type: {type(obj)}")
    img_debugger(f"{name} attributes: {dir(obj) if hasattr(obj, '__dict__') or hasattr(obj, '__slots__') else 'N/A'}")