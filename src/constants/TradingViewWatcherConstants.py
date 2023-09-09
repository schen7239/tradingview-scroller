from enum import Enum

class FileTypes(Enum):
    JSON = "JSON"
    CSV = "CSV"
    EXCEL = "EXCEL"

class ScrollType(Enum):
    LAZY = "LAZY"
    MANUAL = "MANUAL"