"""
Python equivalent of CCOLEntry.h
Represents an entry in a COL file (collision file)
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class COLVersion:
    """Enum equivalent for COL versions"""
    COL_1 = 1
    COL_2 = 2
    COL_3 = 3
    COL_UNKNOWN = 0


@dataclass
class COLBounds:
    """
    Represents collision bounds data
    """
    m_fRadius: float = 0.0
    m_fCenter: list = None  # [float, float, float]
    m_fMin: list = None     # [float, float, float]
    m_fMax: list = None     # [float, float, float]
    
    def __post_init__(self):
        if self.m_fCenter is None:
            self.m_fCenter = [0.0, 0.0, 0.0]
        if self.m_fMin is None:
            self.m_fMin = [0.0, 0.0, 0.0]
        if self.m_fMax is None:
            self.m_fMax = [0.0, 0.0, 0.0]


class COLEntry:
    """
    Python equivalent of CCOLEntry struct
    Represents a single entry/file within a COL archive
    """
    
    def __init__(self):
        self.m_strVersion: str = ""
        self.m_uiFileSize: int = 0
        self.m_strModelName: str = ""
        self.m_usModelId: int = 0
        self.m_bounds: COLBounds = COLBounds()
        self.m_strTBounds: str = ""
        self.m_strHeaderVersion2: str = ""
        self.m_strHeaderVersion3: str = ""
        self.m_uiBodyStart: int = 0
        self.m_uiBodyLength: int = 0