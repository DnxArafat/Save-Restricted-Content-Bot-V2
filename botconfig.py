# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("24266722", ""))
API_HASH = getenv("5dd6bedd030fd733bb5997a1d62a9b2a", "")
BOT_TOKEN = getenv("7531297522:AAGHKt2RYE2GLnTocUnxrNNSNsdU-woMQhM", "")
OWNER_ID = list(map(int, getenv("5091918803", "").split()))
MONGO_DB = getenv(" mongodb+srv://arafat6six:oyPh2oacHe8OXRwJ@cluster0.sx4en.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
LOG_GROUP = getenv("-4511169970", "")
CHANNEL_ID = int(getenv("BinaryPaidLeaker", ""))
