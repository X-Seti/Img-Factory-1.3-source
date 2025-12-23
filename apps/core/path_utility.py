"""
Python equivalent of CPathUtility.h and CPathUtility.cpp
Path manipulation utilities
"""


class PathUtility:
    """
    Python equivalent of CPathUtility class
    Provides path manipulation utilities
    """
    
    @staticmethod
    def getFileName(strPath: str) -> str:
        """
        Get the filename from a full path
        """
        # Replace backslashes with forward slashes
        strPath = strPath.replace("\\", "/")
        last_slash_pos = strPath.rfind('/')
        if last_slash_pos == -1:
            return strPath
        return strPath[last_slash_pos + 1:]
    
    @staticmethod
    def getFileExtension(strPath: str) -> str:
        """
        Get the file extension from a path
        """
        last_dot_pos = strPath.rfind('.')
        if last_dot_pos == -1:
            return ""
        return strPath[last_dot_pos + 1:]
    
    @staticmethod
    def replaceExtension(strPath: str, strExtension: str) -> str:
        """
        Replace the extension of a file path
        """
        last_dot_pos = strPath.rfind('.')
        if last_dot_pos == -1:
            return strPath + "." + strExtension
        return strPath[:last_dot_pos + 1] + strExtension
    
    @staticmethod
    def removeExtension(strPath: str) -> str:
        """
        Remove the extension from a file path
        """
        last_dot_pos = strPath.rfind('.')
        if last_dot_pos == -1:
            return strPath
        return strPath[:last_dot_pos]
    
    @staticmethod
    def addSlashToEnd(strPath: str) -> str:
        """
        Add a slash to the end of a path if not already present
        """
        if not strPath.endswith('/') and not strPath.endswith('\\'):
            strPath += "/"
        return strPath