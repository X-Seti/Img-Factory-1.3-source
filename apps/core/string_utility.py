"""
Python equivalent of CStringUtility.h and CStringUtility.cpp
String manipulation utilities
"""

import math
from typing import List, Deque
from collections import deque


class StringUtility:
    """
    Python equivalent of CStringUtility class
    Provides string manipulation utilities
    """
    
    @staticmethod
    def split(strString: str, strDelimiter: str) -> List[str]:
        """
        Split a string by delimiter
        """
        # If string ends with delimiter, remove it
        if strString and strString.endswith(strDelimiter):
            strString = strString[:-len(strDelimiter)]
        
        return strString.split(strDelimiter)
    
    @staticmethod
    def join(vecTokens: List[str], strDelimiter: str) -> str:
        """
        Join a list of strings with a delimiter
        """
        if not vecTokens:
            return ""
        
        return strDelimiter.join(vecTokens)
    
    @staticmethod
    def combineVectors(vecVector1: List[str], vecVector2: List[str]) -> List[str]:
        """
        Combine two string vectors/lists
        """
        result = []
        result.extend(vecVector1)
        result.extend(vecVector2)
        return result
    
    @staticmethod
    def convertVectorToDeque(vecVector: List[str]) -> Deque[str]:
        """
        Convert a vector/list to deque
        """
        return deque(vecVector)
    
    @staticmethod
    def toUpperCaseVector(vecVector: List[str]) -> List[str]:
        """
        Convert all strings in a vector to uppercase
        """
        return [StringUtility.toUpperCase(strValue) for strValue in vecVector]
    
    @staticmethod
    def findVectorKey(vecVector: List[str], strValue: str) -> int:
        """
        Find the index of a value in a vector
        """
        try:
            return vecVector.index(strValue)
        except ValueError:
            return -1  # Return -1 if not found
    
    @staticmethod
    def replace(strString: str, strFind: str, strReplace: str) -> str:
        """
        Replace all occurrences of a substring
        """
        return strString.replace(strFind, strReplace)
    
    @staticmethod
    def packULong(uiULong: int, bBigEndian: bool = True) -> bytes:
        """
        Pack an unsigned long integer into bytes
        """
        if bBigEndian:
            # Big endian: most significant byte first
            return uiULong.to_bytes(4, byteorder='big')
        else:
            # Little endian: least significant byte first
            return uiULong.to_bytes(4, byteorder='little')
    
    @staticmethod
    def packUShort(uiUShort: int, bBigEndian: bool = True) -> bytes:
        """
        Pack an unsigned short integer into bytes
        """
        if bBigEndian:
            # Big endian: most significant byte first
            return uiUShort.to_bytes(2, byteorder='big')
        else:
            # Little endian: least significant byte first
            return uiUShort.to_bytes(2, byteorder='little')
    
    @staticmethod
    def packUChar(ucUChar: int) -> bytes:
        """
        Pack an unsigned char into bytes
        """
        return ucUChar.to_bytes(1, byteorder='big')
    
    @staticmethod
    def unpackULong(strData: bytes, bBigEndian: bool = True) -> int:
        """
        Unpack bytes to an unsigned long integer
        """
        if bBigEndian:
            # Big endian: most significant byte first
            return int.from_bytes(strData[:4], byteorder='big')
        else:
            # Little endian: least significant byte first
            return int.from_bytes(strData[:4], byteorder='little')
    
    @staticmethod
    def unpackUShort(strData: bytes, bBigEndian: bool = True) -> int:
        """
        Unpack bytes to an unsigned short integer
        """
        if bBigEndian:
            # Big endian: most significant byte first
            return int.from_bytes(strData[:2], byteorder='big')
        else:
            # Little endian: least significant byte first
            return int.from_bytes(strData[:2], byteorder='little')
    
    @staticmethod
    def unpackUChar(strData: bytes) -> int:
        """
        Unpack bytes to an unsigned char
        """
        return int.from_bytes(strData[:1], byteorder='big')
    
    @staticmethod
    def toString(iNumber: int) -> str:
        """
        Convert integer to string
        """
        return str(iNumber)
    
    @staticmethod
    def toNumber(strText: str) -> int:
        """
        Convert string to integer
        """
        try:
            return int(strText)
        except ValueError:
            return 0
    
    @staticmethod
    def toULong(strString: str) -> int:
        """
        Convert string to unsigned long (integer)
        """
        try:
            return int(strString)
        except ValueError:
            return 0
    
    @staticmethod
    def toLong(strString: str) -> int:
        """
        Convert string to signed long (integer)
        """
        try:
            return int(strString)
        except ValueError:
            return 0
    
    @staticmethod
    def toFloat(strString: str) -> float:
        """
        Convert string to float
        """
        try:
            return float(strString)
        except ValueError:
            return 0.0
    
    @staticmethod
    def trim(strString: str) -> str:
        """
        Trim whitespace from both ends of string
        """
        return strString.strip()
    
    @staticmethod
    def ltrim(strString: str) -> str:
        """
        Trim whitespace from left end of string
        """
        return strString.lstrip()
    
    @staticmethod
    def rtrim(strString: str) -> str:
        """
        Trim whitespace from right end of string
        """
        return strString.rstrip()
    
    @staticmethod
    def rtrimFromLeft(strString: str) -> str:
        """
        Trim from left until first whitespace
        """
        for i, char in enumerate(strString):
            if ord(char) <= 32 or ord(char) >= 127:
                return strString[:i]
        return strString
    
    @staticmethod
    def zeroPad(strData: bytes, uiPadLength: int) -> bytes:
        """
        Pad data with zeros to specified length
        """
        if len(strData) >= uiPadLength:
            return strData[:uiPadLength]
        return strData + b'\x00' * (uiPadLength - len(strData))
    
    @staticmethod
    def toUpperCase(strString: str) -> str:
        """
        Convert string to uppercase
        """
        return strString.upper()