import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "13542361").strip()
API_HASH = os.getenv("API_HASH", "6790fc68ed5f71b5a5676af19d5fafd3").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "5547343957:AAFXFlWueDBtz9_UFRLhV9gRcMvMZ8ZfjV0").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://irfdxpvxonpnwi:2879b75d0dc2f2372f20f4edb257d74220b7c14a47e5f9ab81916de8579b6f52@ec2-35-174-248-1.compute-1.amazonaws.com:5432/d4a6fkh5cgk0b6").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "ALONE_MUSIC_ADD_ICT")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
