"""
Python equivalent of eIDEFileSection.h
IDE file section enums
"""

from enum import IntEnum


class IDEFileSection(IntEnum):
    """
    Python equivalent of eIDEFileSection enum
    """
    IDE_OBJS = 0
    IDE_TOBJ = 1
    IDE_ANIM = 2
    IDE_PEDS = 3
    IDE_WEAP = 4
    IDE_CARS = 5
    IDE_HIER = 6
    IDE_TXDP = 7
    IDE_2DFX = 8  # This is a general 2dfx section
    IDE_PATH = 9
    IDE_TREE = 10
    IDE_TANM = 11
    IDE_MLO = 12
    IDE_AMAT = 13
    IDE_HAND = 14
    
    IDE_UNKNOWN = 15
    
    # not file sections but used to determine derived type of CIDESectionEntry
    IDE_2DFX_LIGHTS = 16
    IDE_2DFX_PARTICLES = 17
    IDE_2DFX_UNKNOWN1 = 18
    IDE_2DFX_PEDS = 19
    IDE_2DFX_SUNREFLECTIONS = 20