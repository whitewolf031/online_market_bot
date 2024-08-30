from dotenv import load_dotenv
import os


class Config:
    def __init__(self):
        load_dotenv()
        self.getBotEnv()
        self.getclicktoken()
        self.db_bot()


    def getBotEnv(self):
        self.token = os.getenv("TOKEN", "deafulttoken")

    def getclicktoken(self):
        self.click_token = os.getenv("CLICK_TOKEN", "")

    def db_bot(self):
        self.host = os.getenv("DB_HOST", "")
        self.user = os.getenv("DB_USER", "")
        self.db = os.getenv("DB_NAME", "")
        self.password = os.getenv("DB_PASSWORD", "")


