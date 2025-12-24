#this belongs in apps/methods/ img_core_classes.py - Version: 1
# X-Seti - Nov21 2025 - IMG Factory 1.5 - Core Data Classes and Utilities
"""
Core Data Classes and Utilities - Provides essential data structures and utility functions for IMG Factory operations.
"""

##Methods list -
# format_file_size

##class IMGEntry: -
# __init__
# to_dict
# from_dict

##class COLFile: -
# __init__
# add_entry
# get_entry
# save

def format_file_size(size_bytes): #vers 1
    """
    Format file size in bytes to human readable format
    """
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"


class IMGEntry:
    def __init__(self, name, offset, size, compressed_size=None, timestamp=None): #vers 1
        """
        Initialize IMG entry with file information
        """
        self.name = name
        self.offset = offset
        self.size = size
        self.compressed_size = compressed_size if compressed_size is not None else size
        self.timestamp = timestamp if timestamp is not None else 0
        self.extracted_path = None
        self.is_compressed = (compressed_size is not None and compressed_size != size)

    def to_dict(self): #vers 1
        """
        Convert IMG entry to dictionary representation
        """
        return {
            'name': self.name,
            'offset': self.offset,
            'size': self.size,
            'compressed_size': self.compressed_size,
            'timestamp': self.timestamp,
            'extracted_path': self.extracted_path,
            'is_compressed': self.is_compressed
        }

    @classmethod
    def from_dict(cls, data): #vers 1
        """
        Create IMG entry from dictionary representation
        """
        entry = cls(
            data['name'],
            data['offset'],
            data['size'],
            data.get('compressed_size'),
            data.get('timestamp')
        )
        entry.extracted_path = data.get('extracted_path')
        return entry


class COLFile:
    def __init__(self, filename=None): #vers 1
        """
        Initialize COL file structure
        """
        self.filename = filename
        self.entries = []
        self.header = {}
        self.version = "1.0"

    def add_entry(self, entry): #vers 1
        """
        Add entry to COL file
        """
        self.entries.append(entry)

    def get_entry(self, index): #vers 1
        """
        Get entry by index
        """
        if 0 <= index < len(self.entries):
            return self.entries[index]
        return None

    def save(self, filepath): #vers 1
        """
        Save COL file to disk
        """
        # This is a placeholder implementation
        # Actual implementation would depend on the specific COL format
        pass