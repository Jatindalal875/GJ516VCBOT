from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "19413864"))
API_HASH = getenv("API_HASH", "9e33b9fdf4b840a508be5706104737eb)
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","𝗧𝗕𝗛 ✦ 𝗠𝗨𝗦𝗜𝗖)
BOT_USERNAME = getenv("BOT_USERNAME", "TBH_MUSIC_BOT)
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "EAGLE_MAFIA_CLUB)
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "THE_BROTHERHOOD_COUNCIL)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9000"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9000"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/a0a72d2971424c77000e3.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/a0a72d2971424c77000e3.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5331427205").split()))
