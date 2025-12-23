# X-Seti - November21 2025 - IMG Factory 1.5 - COL Manager
"""
COL Manager - Handles parsing and managing COL files.
"""

from .col_parser import COLFile, COLEntry
from .file_parser import FileParser
from .file_writer import FileWriter
from .string_utility import StringUtility

class COLManager:
    """
    Manager for COL files, handles parsing and storing COL data.
    Implements singleton pattern.
    """
    _instance = None

    def __new__(cls): #vers 1
        if cls._instance is None:
            cls._instance = super(COLManager, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance(): #vers 1
        """
        Get the singleton instance of COLManager.
        """
        if COLManager._instance is None:
            COLManager._instance = COLManager()
        return COLManager._instance

    def parse_file(self, file_path): #vers 1
        """
        Parse a COL file and return a COLFile object with its entries.
        """
        parser = FileParser.get_instance()
        parser.set_read_all_at_once(True)
        file_found = parser.open(file_path, True)
        seek_pos = 0

        col_file = COLFile()
        col_file.file_path = file_path
        
        if not file_found:
            return col_file

        while not parser.is_eof():
            bytes_str = parser.read_string(72)

            entry = COLEntry()
            col_file.entries.append(entry)

            entry.version = bytes_str[0:4]
            entry.file_size = StringUtility.unpack_ulong(bytes_str[4:8], False)
            entry.model_name = StringUtility.rtrim(bytes_str[8:30])
            entry.model_id = StringUtility.unpack_ushort(bytes_str[30:32], False)
            entry.t_bounds = bytes_str[32:72]

            if entry.version == "COL2" or entry.version == "COL3":
                entry.header_version2 = parser.read_string(36)

                if entry.version == "COL3":
                    entry.header_version3 = parser.read_string(16)
                    entry.body_start = seek_pos + 124
                    entry.body_length = (entry.file_size + 8) - 124
                else:
                    entry.body_start = seek_pos + 108
                    entry.body_length = (entry.file_size + 8) - 108
            else:
                entry.body_start = seek_pos + 72
                entry.body_length = (entry.file_size + 8) - 72

            seek_pos += entry.file_size + 8

        parser.close()

        return col_file

    def store_file(self, col_file): #vers 1
        """
        Store a COL file back to disk.
        """
        # This is a placeholder implementation - the original C++ code had this function commented out
        pass