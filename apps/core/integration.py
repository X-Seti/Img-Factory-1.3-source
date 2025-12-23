#!/usr/bin/env python3
"""
Integration module for IMG Factory 1.5
Connects all core functionality to the GUI
"""

from .importer import integrate_import_functions
from .remove import integrate_remove_functions
from .export import integrate_export_functions
from .open import integrate_open_functions
from .close import install_close_functions
from .create import integrate_create_functions
from .rename import integrate_rename_functions
from .reload import integrate_reload_functions
from .rebuild import integrate_rebuild_functions
from .gui_search import integrate_search_functions


def integrate_all_core_functions(main_window):
    """
    Integrate all core functionality with the main window
    This function connects the old C++ functionality (now converted to Python)
    with the new GUI button signals
    """
    try:
        # Integrate all functionality
        integrate_import_functions(main_window)
        integrate_remove_functions(main_window)
        integrate_export_functions(main_window)
        integrate_open_functions(main_window)
        install_close_functions(main_window)
        integrate_create_functions(main_window)
        integrate_rename_functions(main_window)
        integrate_reload_functions(main_window)
        integrate_rebuild_functions(main_window)
        integrate_search_functions(main_window)
        
        main_window.log_message("✅ All core functionality integrated successfully")
        main_window.log_message("🎯 GUI signals connected to Python 3 backend")
        
    except Exception as e:
        main_window.log_message(f"❌ Integration error: {str(e)}")
        import traceback
        main_window.log_message(f"❌ Traceback: {traceback.format_exc()}")


def initialize_core_system(main_window):
    """
    Initialize the core system for the main window
    """
    # Set up any necessary core system components
    main_window.log_message("🔧 Core system initialized")
    
    # Integrate all functions
    integrate_all_core_functions(main_window)