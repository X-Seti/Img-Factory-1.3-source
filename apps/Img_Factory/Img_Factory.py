# X-Seti - December24 2025 - IMG Factory 1.5 - Main Application
"""
Img Factory 1.5 - Main Application
This is the main application class for Img Factory 1.5.
"""
import sys
import os

# Add the methods directory to the Python path to access COL and IMG managers
import sys
import os
methods_path = os.path.join(os.path.dirname(__file__), '..', 'methods')
corefiles_path = os.path.join(os.path.dirname(__file__), '..', 'corefiles')
sys.path.insert(0, methods_path)
sys.path.insert(0, corefiles_path)

# Import using importlib to avoid relative import issues
import importlib.util

# Load COLManager
col_manager_spec = importlib.util.spec_from_file_location("COLManager", os.path.join(methods_path, "col_manager.py"))
col_manager_module = importlib.util.module_from_spec(col_manager_spec)
col_manager_spec.loader.exec_module(col_manager_module)
COLManager = col_manager_module.COLManager

# Load IMGManager
img_manager_spec = importlib.util.spec_from_file_location("IMGManager", os.path.join(methods_path, "img_manager.py"))
img_manager_module = importlib.util.module_from_spec(img_manager_spec)
img_manager_spec.loader.exec_module(img_manager_module)
IMGManager = img_manager_module.IMGManager


class ImgFactoryApp:
    """Main application class for Img Factory 1.5"""
    
    def __init__(self):
        """Initialize the Img Factory application"""
        self.col_manager = COLManager()
        self.img_manager = IMGManager()
        self.running = False
        
    def run(self):
        """Run the Img Factory application"""
        print("Img Factory 1.5 - Application Started")
        self.running = True
        
        # Main application loop
        while self.running:
            self.show_menu()
            choice = input("Enter your choice: ").strip().lower()
            
            if choice == '1':
                self.handle_col_operations()
            elif choice == '2':
                self.handle_img_operations()
            elif choice == '3':
                self.show_info()
            elif choice == 'q' or choice == 'quit':
                self.quit_app()
            else:
                print("Invalid choice. Please try again.")
    
    def show_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("           IMG FACTORY 1.5")
        print("="*50)
        print("1. COL File Operations")
        print("2. IMG File Operations")
        print("3. Show Application Info")
        print("Q. Quit")
        print("="*50)
    
    def handle_col_operations(self):
        """Handle COL file operations"""
        print("\nCOL File Operations:")
        print("1. Load COL file")
        print("2. Parse COL data")
        print("3. Export COL data")
        print("B. Back to main menu")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == '1':
            file_path = input("Enter COL file path: ").strip()
            if file_path:
                try:
                    self.col_manager.load_file(file_path)
                    print(f"Successfully loaded COL file: {file_path}")
                except Exception as e:
                    print(f"Error loading COL file: {e}")
        elif choice == '2':
            if self.col_manager.get_current_file():
                try:
                    data = self.col_manager.parse_data()
                    print(f"Successfully parsed COL data. Found {len(data)} entries.")
                except Exception as e:
                    print(f"Error parsing COL data: {e}")
            else:
                print("No COL file loaded. Please load a file first.")
        elif choice == '3':
            print("Export functionality would be implemented here.")
        elif choice == 'b':
            return
        else:
            print("Invalid choice.")
    
    def handle_img_operations(self):
        """Handle IMG file operations"""
        print("\nIMG File Operations:")
        print("1. Load IMG file")
        print("2. Parse IMG data")
        print("3. Export IMG data")
        print("B. Back to main menu")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == '1':
            file_path = input("Enter IMG file path: ").strip()
            if file_path:
                try:
                    self.img_manager.load_file(file_path)
                    print(f"Successfully loaded IMG file: {file_path}")
                except Exception as e:
                    print(f"Error loading IMG file: {e}")
        elif choice == '2':
            if self.img_manager.get_current_file():
                try:
                    data = self.img_manager.parse_data()
                    print(f"Successfully parsed IMG data. Found {len(data)} entries.")
                except Exception as e:
                    print(f"Error parsing IMG data: {e}")
            else:
                print("No IMG file loaded. Please load a file first.")
        elif choice == '3':
            print("Export functionality would be implemented here.")
        elif choice == 'b':
            return
        else:
            print("Invalid choice.")
    
    def show_info(self):
        """Show application information"""
        print("\nImg Factory 1.5 - Information")
        print("Version: 1.5")
        print("Developed by: X-Seti")
        print("Purpose: COL and IMG file processing tool")
        print(f"COL Manager Status: {'Ready' if self.col_manager.is_ready() else 'Not Ready'}")
        print(f"IMG Manager Status: {'Ready' if self.img_manager.is_ready() else 'Not Ready'}")
    
    def quit_app(self):
        """Quit the application"""
        print("Thank you for using Img Factory 1.5!")
        self.running = False


if __name__ == "__main__":
    # If running as main script, create and run the app directly
    import sys
    import os
    
    # Add the methods directory to the Python path to access COL and IMG managers
    methods_path = os.path.join(os.path.dirname(__file__), '..', 'methods')
    corefiles_path = os.path.join(os.path.dirname(__file__), '..', 'corefiles')
    sys.path.insert(0, methods_path)
    sys.path.insert(0, corefiles_path)
    
    # Import using importlib to avoid relative import issues
    import importlib.util

    # Load COLManager
    col_manager_spec = importlib.util.spec_from_file_location("COLManager", os.path.join(methods_path, "col_manager.py"))
    col_manager_module = importlib.util.module_from_spec(col_manager_spec)
    col_manager_spec.loader.exec_module(col_manager_module)
    COLManager = col_manager_module.COLManager

    # Load IMGManager
    img_manager_spec = importlib.util.spec_from_file_location("IMGManager", os.path.join(methods_path, "img_manager.py"))
    img_manager_module = importlib.util.module_from_spec(img_manager_spec)
    img_manager_spec.loader.exec_module(img_manager_module)
    IMGManager = img_manager_module.IMGManager
    
    # Create and run the app
    app = ImgFactoryApp()
    app.run()