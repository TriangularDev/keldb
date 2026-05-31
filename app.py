import asyncio
import keldb

database = keldb.KelDB(keldb.FileStoreHook("./testdb/"))

async def main():
    print(await database.get_value())

asyncio.run(main())