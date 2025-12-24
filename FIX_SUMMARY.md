# IMG Factory 1.5 C++ to Python Conversion Summary

## Overview
Converted core C++ functionality to Python for the IMG Factory 1.5 project while maintaining original functionality and following project structure guidelines.

## Files Converted

### COL Manager Conversion
- **Original C++ Files:**
  - `/COL Manager/Source/CCOLFile.cpp`
  - `/COL Manager/Source/CCOLFile.h`
  - `/COL Manager/Source/CCOLEntry.h`
  - `/COL Manager/Source/CCOLManager.cpp`
  - `/COL Manager/Source/CCOLManager.h`

- **New Python Files:**
  - `/apps/methods/col_parser.py` - Contains COLFile and COLEntry classes
  - `/apps/methods/col_manager.py` - Contains COLManager class with singleton pattern
  - `/apps/methods/file_parser.py` - Contains FileParser class for file operations
  - `/apps/methods/file_writer.py` - Contains FileWriter class for file writing
  - `/apps/methods/string_utility.py` - Contains StringUtility class with binary data functions

### IMG Manager Conversion
- **Original C++ Files:**
  - `/IMG Manager/Source/CIMGFile.cpp`
  - `/IMG Manager/Source/CIMGFile.h`
  - `/IMG Manager/Source/CIMGEntry.h`
  - `/IMG Manager/Source/CIMGManager.h`

- **New Python Files:**
  - `/apps/methods/img_parser.py` - Contains IMGFile, IMGEntry and IMGVersion classes
  - `/apps/methods/img_manager.py` - Contains IMGManager class with singleton pattern
  - `/apps/methods/path_utility.py` - Contains PathUtility class for path operations

## Directory Structure Created
- `/apps/methods/` - Contains all method-related Python files
- `/apps/corefiles/` - For core important/single-use functions
- `/apps/components/` - For editor components
- `/apps/Img_Factory/` - Contains main application placeholder

## Key Features Preserved
- Singleton patterns for managers
- Binary data handling and parsing
- File reading and writing capabilities
- String manipulation functions for binary data
- Original functionality for COL and IMG file processing

## Launchers Created
- `/launcher.py` - Root launcher for easy execution from project root
- `/apps/Img_Factory/launcher.py` - App-specific launcher

## Notes
- GUI functionality will need to be updated separately to work with Python (replacing dx9, opencl, QT6 dependencies)
- The gui_layout.py file structure is preserved as requested
- All original functionality is maintained while converting to Python
- Launchers connect the preserved GUI layout with converted Python methods