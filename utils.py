import time
import requests
from requests.exceptions import RequestException

def retry(key_operation, retries=3, delay=2):
    for attempt in range(retries):
        try:
            return key_operation()
        except RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry(lambda: fetch_data(url))
        print(data)
    except Exception as e:
        print(f"Failed to fetch data: {e}")