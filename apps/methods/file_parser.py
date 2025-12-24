# X-Seti - November21 2025 - IMG Factory 1.5 - File Parser
"""
File Parser - Handles reading files in binary and text modes.
"""

class FileParser:
    """
    Parser for reading files in binary and text modes.
    Implements singleton pattern.
    """
    _instance = None

    def __new__(cls): #vers 1
        if cls._instance is None:
            cls._instance = super(FileParser, cls).__new__(cls)
        return cls._instance

    def __init__(self): #vers 1
        self.file_handle = None
        self.read_all_at_once = False
        self.file_content = b""
        self.current_position = 0

    @staticmethod
    def get_instance(): #vers 1
        """
        Get the singleton instance of FileParser.
        """
        if FileParser._instance is None:
            FileParser._instance = FileParser()
        return FileParser._instance

    def set_read_all_at_once(self, value): #vers 1
        """
        Set whether to read the entire file at once.
        """
        self.read_all_at_once = value

    def open(self, file_path, binary_mode=False): #vers 1
        """
        Open a file for reading.
        """
        try:
            if binary_mode:
                self.file_handle = open(file_path, 'rb')
                self.file_content = self.file_handle.read()
                self.current_position = 0
            else:
                self.file_handle = open(file_path, 'r')
            return True
        except FileNotFoundError:
            return False

    def read_string(self, length): #vers 1
        """
        Read a string of specified length from the file.
        """
        if self.file_handle and self.current_position < len(self.file_content):
            result = self.file_content[self.current_position:self.current_position + length]
            self.current_position += length
            return result.decode('latin-1', errors='ignore')  # Use latin-1 to handle binary data
        return ""

    def is_eof(self): #vers 1
        """
        Check if we've reached the end of the file.
        """
        return self.current_position >= len(self.file_content)

    def close(self): #vers 1
        """
        Close the file.
        """
        if self.file_handle:
            self.file_handle.close()
            self.file_handle = None