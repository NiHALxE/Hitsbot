import requests
import logging
import time
import hashlib
from config import TOKEN, MAX_RETRIES


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Unique Bot ID
BOT_ID = hashlib.sha256(TOKEN.encode()).hexdigest()[:8]  

# Retry decorator for network requests
def retry_request(func):
    def wrapper(*args, **kwargs):
        retries = 0
        while retries < MAX_RETRIES:
            try:
                return func(*args, **kwargs)
            except requests.exceptions.RequestException as e:
                logging.error(f"Network error: {e}. Retrying in {2**retries} seconds...")
                time.sleep(2**retries)
                retries += 1
        logging.error(f"Failed after {MAX_RETRIES} retries.")
        return None  # Or handle the failure gracefully
    return wrapper

# Enhanced send_api_request_with_details function
@retry_request
def send_api_request_with_details(url, method='POST', headers=None, data=None):
    response = requests.request(method, url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return {
            'status_code': response.status_code,
            'response_text': response.text,
            'url': url,
            'method': method,
            'headers': headers,
            'data': data
        }
