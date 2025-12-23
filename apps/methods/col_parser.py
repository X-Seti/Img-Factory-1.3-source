# X-Seti - November21 2025 - IMG Factory 1.5 - COL Parser
"""
COL Parser - Handles COL file parsing and data structures.
"""

class COLParser:
    """
    Parser for COL files, which contain collision data for 3D models.
    """
    def __init__(self): #vers 1
        self.file_path = ""
        self.entries = []

    def get_model_names(self): #vers 1
        """
        Get a list of model names from all entries in the COL file.
        """
        model_names = []
        for entry in self.entries:
            model_names.append(entry.model_name)
        return model_names

class COLFile:
    """
    Represents a COL file with its path and entries.
    """
    def __init__(self): #vers 1
        self.file_path = ""
        self.entries = []

    def get_model_names(self): #vers 1
        """
        Get a list of model names from all entries in the COL file.
        """
        model_names = []
        for entry in self.entries:
            model_names.append(entry.model_name)
        return model_names

class COLEntry:
    """
    Represents a single entry in a COL file, containing collision data for a model.
    """
    def __init__(self): #vers 1
        self.version = ""
        self.file_size = 0
        self.model_name = ""
        self.model_id = 0
        self.t_bounds = ""
        self.header_version2 = ""
        self.header_version3 = ""
        self.body_start = 0
        self.body_length = 0