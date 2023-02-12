from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from config import MONGO_DB_NAME, MONGO_URL


client = AsyncIOMotorClient(MONGO_URL)
engine = AIOEngine(motor_client, database=MONGO_DB_NAME)


class MongoDB:

    def __init__(self):
        self.client = None
        self.engine = None

    def connect(self):
        self.client = AsyncIOMotorClent(MONGO_URL)
        self.engine = AIOEngine(
            motor_client=self.client, database=MONGO_DB_NAME)


mongodb = MongoDB()
