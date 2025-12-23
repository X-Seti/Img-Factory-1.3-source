"""
Python equivalent of CIMGFile.h and CIMGFile.cpp
Handles IMG file operations and contains IMG entries
"""

from typing import List, Optional
from .img_entry import IMGEntry, IMGVersion
import os


class IMGFile:
    """
    Python equivalent of CIMGFile struct
    Handles IMG file operations and contains IMG entries
    """
    
    def __init__(self):
        self.m_bFileFound = False
        self.m_strPath = ""
        self.m_eVersion = IMGVersion.IMG_UNKNOWN
        self.m_uiEntryCount = 0
        self.m_vecEntries: List[IMGEntry] = []
    
    def unload(self) -> None:
        """
        Unload all entries from memory (cleanup)
        """
        # In Python, we don't need explicit deletion, but we can clear the list
        self.m_vecEntries.clear()
        self.m_bFileFound = False
        self.m_uiEntryCount = 0
    
    def getEntryByHighestOffset(self) -> Optional[IMGEntry]:
        """
        Get the entry with the highest file offset
        """
        if not self.m_vecEntries:
            return None
        
        highest_offset = 0
        highest_offset_entry = None
        
        for entry in self.m_vecEntries:
            if entry.m_uiFileOffset > highest_offset:
                highest_offset = entry.m_uiFileOffset
                highest_offset_entry = entry
        
        return highest_offset_entry
    
    def getVersion3NamesLength(self) -> int:
        """
        Get the total length of all filenames for IMG version 3
        """
        total_length = 0
        for entry in self.m_vecEntries:
            total_length += len(entry.m_strFileName)
        
        # Add one byte per entry for null terminators
        total_length += len(self.m_vecEntries)
        return total_length
    
    def getEntryByName(self, strEntryName: str) -> Optional[IMGEntry]:
        """
        Get an entry by its full filename (case-insensitive)
        """
        for entry in self.m_vecEntries:
            if entry.m_strFileName.upper() == strEntryName.upper():
                return entry
        return None
    
    def getEntryByNameWithoutExtension(self, strEntryNameWithoutExtension: str) -> Optional[IMGEntry]:
        """
        Get an entry by its name without extension (case-insensitive)
        """
        for entry in self.m_vecEntries:
            # Remove extension from the entry's filename
            entry_name_without_ext = self.removeExtension(entry.m_strFileName)
            if entry_name_without_ext.upper() == strEntryNameWithoutExtension.upper():
                return entry
        return None
    
    def getEntryIndex(self, pIMGEntry: IMGEntry) -> int:
        """
        Get the index of a specific entry in the vector
        """
        try:
            return self.m_vecEntries.index(pIMGEntry)
        except ValueError:
            return -1  # Return -1 if entry not found (equivalent to C++ return -1)
    
    def removeExtension(self, strPath: str) -> str:
        """
        Remove extension from a filename (equivalent to CPathUtility::removeExtension)
        """
        last_dot_pos = strPath.rfind('.')
        if last_dot_pos == -1:
            return strPath
        return strPath[:last_dot_pos]
    
    def getFileName(self, strPath: str) -> str:
        """
        Get filename from full path (equivalent to CPathUtility::getFileName)
        """
        # Replace backslashes with forward slashes
        strPath = strPath.replace("\\", "/")
        last_slash_pos = strPath.rfind('/')
        if last_slash_pos == -1:
            return strPath
        return strPath[last_slash_pos + 1:]
    
    def getFileExtension(self, strPath: str) -> str:
        """
        Get file extension (equivalent to CPathUtility::getFileExtension)
        """
        last_dot_pos = strPath.rfind('.')
        if last_dot_pos == -1:
            return ""
        return strPath[last_dot_pos + 1:]
    
    def addEntry(self, entry: IMGEntry) -> None:
        """
        Add a new entry to the IMG file
        """
        self.m_vecEntries.append(entry)
        self.m_uiEntryCount = len(self.m_vecEntries)
    
    def loadFromFile(self, file_path: str) -> bool:
        """
        Load an IMG file from disk (placeholder implementation)
        """
        try:
            if os.path.exists(file_path):
                self.m_strPath = file_path
                self.m_bFileFound = True
                # This is a placeholder - actual IMG file parsing would go here
                # For now, we just set basic properties
                self.m_eVersion = IMGVersion.IMG_3_UNENCRYPTED  # Default assumption
                return True
            else:
                self.m_bFileFound = False
                return False
        except Exception:
            self.m_bFileFound = False
            return False