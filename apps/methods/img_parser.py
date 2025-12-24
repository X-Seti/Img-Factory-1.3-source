# X-Seti - November21 2025 - IMG Factory 1.5 - IMG Parser
"""
IMG Parser - Handles IMG file parsing and data structures.
"""

from enum import Enum

class IMGVersion(Enum):
    """
    Enumeration for IMG file versions.
    """
    IMG_1 = 0
    IMG_2 = 1
    IMG_3_ENCRYPTED = 2
    IMG_3_UNENCRYPTED = 3
    IMG_UNKNOWN = 4

class IMGEntry:
    """
    Represents a single entry in an IMG file, containing file data.
    """
    def __init__(self): #vers 1
        self.file_offset = 0  # in blocks (2048 bytes)
        self.file_size = 0    # in bytes
        self.file_name = ""
        self.version = 0
        self.resource_type = 0
        self.flags = 0
        self.new_file_offset = 0

class IMGFile:
    """
    Represents an IMG file with its path and entries.
    """
    def __init__(self): #vers 1
        self.file_found = False
        self.path = ""
        self.version = IMGVersion.IMG_UNKNOWN
        self.entry_count = 0
        self.entries = []

    def unload(self): #vers 1
        """
        Unload all entries from memory.
        """
        # In Python, we don't need to manually delete objects, but we can clear the list
        self.entries.clear()

    def get_entry_by_highest_offset(self): #vers 1
        """
        Get the entry with the highest file offset.
        """
        highest_offset = 0
        highest_offset_entry = None
        for entry in self.entries:
            if entry.file_offset > highest_offset:
                highest_offset = entry.file_offset
                highest_offset_entry = entry
        return highest_offset_entry

    def get_version3_names_length(self): #vers 1
        """
        Calculate the total length of names for version 3 files.
        """
        length = 0
        for entry in self.entries:
            length += len(entry.file_name)
        length += len(self.entries)
        return length

    def get_entry_by_name(self, entry_name): #vers 1
        """
        Get an entry by its name (case-insensitive).
        """
        from .string_utility import StringUtility
        for entry in self.entries:
            if StringUtility.to_upper_case(entry_name) == StringUtility.to_upper_case(entry.file_name):
                return entry
        return None

    def get_entry_by_name_without_extension(self, entry_name_without_extension): #vers 1
        """
        Get an entry by its name without extension (case-insensitive).
        """
        from .string_utility import StringUtility
        from .path_utility import PathUtility
        for entry in self.entries:
            if StringUtility.to_upper_case(entry_name_without_extension) == StringUtility.to_upper_case(
                    PathUtility.remove_extension(entry.file_name)):
                return entry
        return None

    def get_entry_index(self, img_entry): #vers 1
        """
        Get the index of a specific entry in the entries list.
        """
        for i in range(len(self.entries)):
            if self.entries[i] == img_entry:
                return i
        return -1  # Return -1 if not found (since Python doesn't have unsigned long -1)