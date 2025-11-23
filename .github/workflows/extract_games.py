from bs4 import BeautifulSoup
import sys

try:
    with open('schedule.html', 'r', encoding='utf-8') as f:
        html = f.read()
except Exception as e:
    print('❌ ERROR: Could not read schedule.html')
    print(e)
    sys.exit(1)

try:
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(separator='\n')
except Exception as e:
    print('❌ ERROR: Failed to parse HTML')
    print(e)
    sys.exit(1)

if not text.strip():
    print('❌ ERROR: Extracted text is empty — site may be dynamic')
    sys.exit(1)

try:
    with open('games.txt', 'w', encoding='utf-8') as f:
        f.write(text)
except Exception as e:
    print('❌ ERROR: Failed to save games.txt')
    print(e)
    sys.exit(1)
