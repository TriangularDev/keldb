from enum import Enum
import asyncio

class Enums():
    class InformationAvailability(Enum):
        NONE = 1
        VALIDATED = 2
        FULL = 3

class Node():
    pass

class KelDB(Node):
    pass

class Hook():
    pass

class FileStoreHook(Hook):
    pass