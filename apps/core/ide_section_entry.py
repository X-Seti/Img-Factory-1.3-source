"""
Python equivalent of CIDESectionEntry.h
Base class for IDE section entries
"""

from typing import List, Optional
from .ide_enums import IDEFileSection


class IDESectionEntry:
    """
    Python equivalent of CIDESectionEntry class
    Base class for IDE section entries
    """
    
    def __init__(self):
        self.m_strComment: str = ""  # the comment at the end of the line
        self.m_pPreviousComment: Optional[str] = None  # the latest comment found on a previous line
        self.m_vecPreviousCommentLines: List[str] = []  # the comments on the line(s) directly before this section entry
        self.m_uiOldObjectId: int = 0
        self.m_eSectionType: IDEFileSection = IDEFileSection.IDE_UNKNOWN