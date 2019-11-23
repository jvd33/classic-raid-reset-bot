"""constants.py"""
import enum


class Raids(str, enum.Enum):
    MoltenCore = 'MC'
    Onyxia = 'Onyxia'
    Naxxramas = 'Naxxramas'
    ZulGurub = 'ZG'
    AQTwenty = 'AQ20'
    AQForty = 'AQ40'
    BlackwingLair = 'BWL'


class Days(int, enum.Enum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6

