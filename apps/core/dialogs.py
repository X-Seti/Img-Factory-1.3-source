# this belongs in apps/core/ dialogs.py - Version: 1 of updates to file
# X-Seti - November21 2025 - IMG Factory 1.5 - Dialog Management System
"""
Dialog Management System - Handles all application dialogs and message boxes.
"""

import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import os
import sys

##Methods list -
# show_info
# show_warning
# show_error
# ask_question
# ask_yes_no
# ask_ok_cancel
# ask_retry_cancel
# ask_save_filename
# ask_open_filename
# ask_directory
# ask_color
# ask_font
# ask_string
# ask_integer
# ask_float

def show_info(title, message): #vers 1
    """
    Show an information dialog.
    
    Args:
        title (str): Dialog title
        message (str): Information message
    """
    messagebox.showinfo(title, message)

def show_warning(title, message): #vers 1
    """
    Show a warning dialog.
    
    Args:
        title (str): Dialog title
        message (str): Warning message
    """
    messagebox.showwarning(title, message)

def show_error(title, message): #vers 1
    """
    Show an error dialog.
    
    Args:
        title (str): Dialog title
        message (str): Error message
    """
    messagebox.showerror(title, message)

def ask_question(title, message): #vers 1
    """
    Ask a yes/no question.
    
    Args:
        title (str): Dialog title
        message (str): Question message
    
    Returns:
        bool: True if yes, False if no
    """
    return messagebox.askyesno(title, message)

def ask_yes_no(title, message): #vers 1
    """
    Ask a yes/no question.
    
    Args:
        title (str): Dialog title
        message (str): Question message
    
    Returns:
        bool: True if yes, False if no
    """
    return messagebox.askyesno(title, message)

def ask_ok_cancel(title, message): #vers 1
    """
    Ask an OK/Cancel question.
    
    Args:
        title (str): Dialog title
        message (str): Question message
    
    Returns:
        bool: True if OK, False if Cancel
    """
    return messagebox.askokcancel(title, message)

def ask_retry_cancel(title, message): #vers 1
    """
    Ask a Retry/Cancel question.
    
    Args:
        title (str): Dialog title
        message (str): Question message
    
    Returns:
        bool: True if Retry, False if Cancel
    """
    return messagebox.askretrycancel(title, message)

def ask_save_filename(title="Save As", initialdir=None, defaultextension="", filetypes=None): #vers 1
    """
    Open a save file dialog.
    
    Args:
        title (str): Dialog title
        initialdir (str): Initial directory
        defaultextension (str): Default file extension
        filetypes (list): List of file type tuples
    
    Returns:
        str: Selected file path or None if cancelled
    """
    if filetypes is None:
        filetypes = [("All Files", "*.*")]
    
    return filedialog.asksaveasfilename(
        title=title,
        initialdir=initialdir,
        defaultextension=defaultextension,
        filetypes=filetypes
    )

def ask_open_filename(title="Open", initialdir=None, filetypes=None): #vers 1
    """
    Open an open file dialog.
    
    Args:
        title (str): Dialog title
        initialdir (str): Initial directory
        filetypes (list): List of file type tuples
    
    Returns:
        str: Selected file path or None if cancelled
    """
    if filetypes is None:
        filetypes = [("All Files", "*.*")]
    
    return filedialog.askopenfilename(
        title=title,
        initialdir=initialdir,
        filetypes=filetypes
    )

def ask_directory(title="Select Directory", initialdir=None): #vers 1
    """
    Open a directory selection dialog.
    
    Args:
        title (str): Dialog title
        initialdir (str): Initial directory
    
    Returns:
        str: Selected directory path or None if cancelled
    """
    return filedialog.askdirectory(
        title=title,
        initialdir=initialdir
    )

def ask_string(title, prompt, initialvalue=""): #vers 1
    """
    Open a string input dialog.
    
    Args:
        title (str): Dialog title
        prompt (str): Input prompt
        initialvalue (str): Initial value
    
    Returns:
        str: Input string or None if cancelled
    """
    return simpledialog.askstring(title, prompt, initialvalue=initialvalue)

def ask_integer(title, prompt, initialvalue=0, minvalue=None, maxvalue=None): #vers 1
    """
    Open an integer input dialog.
    
    Args:
        title (str): Dialog title
        prompt (str): Input prompt
        initialvalue (int): Initial value
        minvalue (int): Minimum allowed value
        maxvalue (int): Maximum allowed value
    
    Returns:
        int: Input integer or None if cancelled
    """
    return simpledialog.askinteger(title, prompt, 
                                   initialvalue=initialvalue, 
                                   minvalue=minvalue, 
                                   maxvalue=maxvalue)

def ask_float(title, prompt, initialvalue=0.0, minvalue=None, maxvalue=None): #vers 1
    """
    Open a float input dialog.
    
    Args:
        title (str): Dialog title
        prompt (str): Input prompt
        initialvalue (float): Initial value
        minvalue (float): Minimum allowed value
        maxvalue (float): Maximum allowed value
    
    Returns:
        float: Input float or None if cancelled
    """
    return simpledialog.askfloat(title, prompt, 
                                 initialvalue=initialvalue, 
                                 minvalue=minvalue, 
                                 maxvalue=maxvalue)