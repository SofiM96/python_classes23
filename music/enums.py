"""
The enums used in this project - Vocals and Instrument
"""
from enum import Enum


class Vocals(Enum):
    LEAD_VOCALS = 'lead vocals'
    BACKGROUND_VOCALS = 'background vocals'


class Instrument(Enum):
    LEAD_GUITAR = 'lead guitar'
    RHYTHM_GUITAR = 'rhythm guitar'
    BASS = 'bass'
    DRUMS = 'drums'


class BaseColors(Enum):
    yellow = '#FFFF00'
    red = '#FF0000'
    blue = '#0000FF'


print(list(BaseColors))
