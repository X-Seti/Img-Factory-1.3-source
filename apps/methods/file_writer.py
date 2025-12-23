# X-Seti - November21 2025 - IMG Factory 1.5 - File Writer
"""
File Writer - Handles writing files in binary and text modes.
"""

class FileWriter:
    """
    Writer for creating files in binary and text modes.
    Implements singleton pattern.
    """
    _instance = None

    def __new__(cls): #vers 1
        if cls._instance is None:
            cls._instance = super(FileWriter, cls).__new__(cls)
        return cls._instance

    def __init__(self): #vers 1
        self.file_handle = None

    @staticmethod
    def get_instance(): #vers 1
        """
        Get the singleton instance of FileWriter.
        """
        if FileWriter._instance is None:
            FileWriter._instance = FileWriter()
        return FileWriter._instance

    def open_binary_file(self, file_path): #vers 1
        """
        Open a file for binary writing.
        """
        try:
            self.file_handle = open(file_path, 'wb')
            return True
        except:
            return False

    def write_string(self, text, length=None): #vers 1
        """
        Write a string to the file, optionally padded to a specific length.
        """
        if self.file_handle is None:
            return False

        if length:
            # Pad or truncate the string to the specified length
            if len(text) > length:
                text = text[:length]
            else:
                text = text.ljust(length, '\x00')

        try:
            self.file_handle.write(text.encode('latin-1', errors='ignore'))
            return True
        except:
            return False

    def write_ulong(self, value): #vers 1
        """
        Write an unsigned long integer to the file in little-endian format.
        """
        if self.file_handle is None:
            return False

        # Convert to 4-byte little-endian
        byte_data = bytes([
            value & 0xFF,
            (value >> 8) & 0xFF,
            (value >> 16) & 0xFF,
            (value >> 24) & 0xFF
        ])

        try:
            self.file_handle.write(byte_data)
            return True
        except:
            return False

    def write_ushort(self, value): #vers 1
        """
        Write an unsigned short integer to the file in little-endian format.
        """
        if self.file_handle is None:
            return False

        # Convert to 2-byte little-endian
        byte_data = bytes([
            value & 0xFF,
            (value >> 8) & 0xFF
        ])

        try:
            self.file_handle.write(byte_data)
            return True
        except:
            return False

    def close_binary_file(self): #vers 1
        """
        Close the currently open binary file.
        """
        if self.file_handle:
            self.file_handle.close()
            self.file_handle = None