# X-Seti - November21 2025 - IMG Factory 1.5 - Path Utility
"""
Path Utility - Provides path manipulation functions.
"""

class PathUtility:
    """
    Utility class for path manipulation operations.
    """

    @staticmethod
    def remove_extension(file_path): #vers 1
        """
        Remove the extension from a file path.
        """
        if '.' in file_path:
            return file_path.rsplit('.', 1)[0]
        return file_path

    @staticmethod
    def get_extension(file_path): #vers 1
        """
        Get the extension from a file path.
        """
        if '.' in file_path:
            return file_path.rsplit('.', 1)[1]
        return ""

    @staticmethod
    def get_file_name(file_path): #vers 1
        """
        Get the file name from a full path.
        """
        import os
        return os.path.basename(file_path)

    @staticmethod
    def get_directory(file_path): #vers 1
        """
        Get the directory from a full path.
        """
        import os
        return os.path.dirname(file_path)