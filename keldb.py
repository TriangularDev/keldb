from enum import Enum
import aiofiles
import asyncio
import json
import os

class Enums():
    class InformationAvailability(Enum):
        NONE = 1
        INPUT = 2
        VALIDATED = 3
        FULL = 4

class Node():
    def __init__(self):
        self.InformationAvailability = Enums.InformationAvailability.NONE

        # Basic information (INPUT and VALIDATED information availability)
        self.root = None
        self.parent = None
        self.name = None
        self.path = None

    async def get_value(self):
        return await self.root.hook.get_path_value(self.path)

class Hook():
    pass

class FileStoreHook(Hook):
    def __init__(self, dir:str):
        self.dir = dir

        self.store = {}
    
    async def get_path_value(self, path:str, cached=False):
        parts = (self.dir,) + tuple(x for x in path.split("/") if x != "") + ("value.json",)

        if not cached:
            async with aiofiles.open(os.path.join(*parts), 'r') as f:
                return json.loads(await f.read())

class KelDB(Node):
    def __init__(self, hook:Hook):
        self.InformationAvailability = Enums.InformationAvailability.NONE

        self.root = self
        self.parent = None
        self.name = ""
        self.path = "/"

        self.hook = hook