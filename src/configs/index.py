import os
from dotenv import load_dotenv

load_dotenv()

configs_env = {
    "url_database": os.getenv("URL_DATABASE")
}