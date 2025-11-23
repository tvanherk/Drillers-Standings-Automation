import requests
import sys

url = 'https://emsamain.com/schedules/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
except Exception as e:
    print('❌ ERROR: Failed to fetch schedule URL')
    print(e)
    sys.exit(1)

try:
    with open('schedule.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
except Exception as e:
    print('❌ ERROR: Failed to save schedule.html')
    print(e)
    sys.exit(1)
