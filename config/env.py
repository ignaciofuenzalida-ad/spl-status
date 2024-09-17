import os
from dotenv import load_dotenv

load_dotenv()

config = {"DEFAULT_CRON_TIME": os.getenv("DEFAULT_CRON_TIME", 1)}
