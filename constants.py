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

    @staticmethod
    def get_reset_cadence(raid):
        return {
            MoltenCore: 7,
            Naxxramas: 7,
            AQForty: 7,
            BlackwingLair: 7,
            Onyxia: 5,
            AQTwenty: 3,
            ZulGurub: 3
        }.get(raid)

class Days(int, enum.Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7

