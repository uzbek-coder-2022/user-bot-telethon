from environs import Env

env = Env()
env.read_env()

API_ID = env.int("api_id")  # Telegram API ID
API_HASH = env.str("api_hash")  # Telegram API Hash
SESSION_NAME = env.str("session_name")  # Session nomi
GROUP_ID = env.int("group_id")  # Guruh ID
CHANNEL_ID = env.int("channel_id")  # Kanal ID