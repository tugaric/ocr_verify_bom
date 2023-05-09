from dataclasses import dataclass

@dataclass
class TextPosition:
    text:str
    x1: int
    y1: int
    x2: int
    y2: int