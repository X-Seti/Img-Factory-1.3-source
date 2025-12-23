# X-Seti - November21 2025 - IMG Factory 1.5 - String Utility
"""
String Utility - Provides string manipulation functions for binary data handling.
"""

class StringUtility:
    """
    Utility class for string manipulation, particularly for binary data conversion.
    """

    @staticmethod
    def unpack_ulong(byte_str, little_endian=True): #vers 1
        """
        Unpack a 4-byte string as an unsigned long integer.
        """
        if len(byte_str) < 4:
            return 0
        byte_values = [ord(c) if isinstance(c, str) else c for c in byte_str[:4]]
        if little_endian:
            return byte_values[0] | (byte_values[1] << 8) | (byte_values[2] << 16) | (byte_values[3] << 24)
        else:
            return byte_values[3] | (byte_values[2] << 8) | (byte_values[1] << 16) | (byte_values[0] << 24)

    @staticmethod
    def unpack_ushort(byte_str, little_endian=True): #vers 1
        """
        Unpack a 2-byte string as an unsigned short integer.
        """
        if len(byte_str) < 2:
            return 0
        byte_values = [ord(c) if isinstance(c, str) else c for c in byte_str[:2]]
        if little_endian:
            return byte_values[0] | (byte_values[1] << 8)
        else:
            return byte_values[1] | (byte_values[0] << 8)

    @staticmethod
    def rtrim(text): #vers 1
        """
        Remove trailing whitespace from a string.
        """
        if text is None:
            return ""
        # Remove trailing null characters and whitespace
        return text.rstrip('\x00 \t\n\r')

    @staticmethod
    def zero_pad(text, length): #vers 1
        """
        Pad a string with null characters to the specified length.
        """
        if text is None:
            text = ""
        if len(text) >= length:
            return text[:length]
        return text + '\x00' * (length - len(text))

    @staticmethod
    def to_upper_case(text): #vers 1
        """
        Convert a string to uppercase.
        """
        if text is None:
            return ""
        return text.upper()