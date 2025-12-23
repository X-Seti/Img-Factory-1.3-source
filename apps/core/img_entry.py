"""
Python equivalent of CIMGEntry.h and CIMGEntry.cpp
Represents an entry in an IMG file
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class IMGVersion:
    """Enum equivalent for IMG versions"""
    IMG_1 = 0
    IMG_2 = 1
    IMG_3_ENCRYPTED = 2
    IMG_3_UNENCRYPTED = 3
    IMG_UNKNOWN = 4


@dataclass
class IMGEntry:
    """
    Python equivalent of CIMGEntry struct
    Represents a single entry/file within an IMG archive
    """
    # Initialize with default values
    m_uiFileOffset: int = 0  # in blocks (2048 bytes)
    m_uiFileSize: int = 0    # in bytes
    m_strFileName: str = ""
    m_uiVersion: int = 0
    m_uiResourceType: int = 0
    m_usFlags: int = 0
    
    # For file operations
    m_uiNewFileOffset: int = 0
    
    def __init__(self):
        self.m_uiFileOffset = 0  # in blocks (2048 bytes)
        self.m_uiFileSize = 0    # in bytes
        self.m_strFileName = ""
        self.m_uiVersion = 0
        self.m_uiResourceType = 0
        self.m_usFlags = 0
        
        # For file operations
        self.m_uiNewFileOffset = 0