#this belongs in root /ChangeLog.md - Version: 3
# X-Seti - October22 2025 - IMG Factory 1.3 ChangeLog

# IMG Factory 1.5 - ChangeLog - (New System)

Complete history of fixes, updates, and improvements.

---
Port from MexUK Img Factory 1.2

## IMG Factory 1.5 Updates

### November 21, 2025
- Converted C++ COL Manager files to Python:
  - Created /apps/methods/col_parser.py
  - Created /apps/methods/col_manager.py
  - Created /apps/methods/file_parser.py
  - Created /apps/methods/file_writer.py
  - Created /apps/methods/string_utility.py

- Converted C++ IMG Manager files to Python:
  - Created /apps/methods/img_parser.py
  - Created /apps/methods/img_manager.py
  - Created /apps/methods/path_utility.py

- Created directory structure:
  - /apps/methods/
  - /apps/corefiles/
  - /apps/components/
  - /apps/Img_Factory/Img_Factory.py (placeholder)

- Updated project to Python implementation while preserving original functionality

### December 24, 2025
- Created launcher.py in /apps/Img_Factory/ to connect GUI with converted methods
- Created root launcher.py for easy execution from project root
- Connected preserved gui_layout.py with converted Python methods
- Maintained 100% original functionality in converted methods
