import os

TOKEN = os.getenv("TOKEN")  # Get bot token from environment variables
API_URL = 'https://prod-api.viewlift.com/identity'
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")
CHANNEL_ID = os.getenv("CHANNEL_ID")
MAX_RETRIES = 3 
