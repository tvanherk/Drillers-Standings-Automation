import smtplib
import sys
import os
from email.mime.text import MIMEText

try:
    with open('standings.txt', 'r', encoding='utf-8') as f:
        standings = f.read()
except Exception as e:
    print('❌ ERROR: Could not read standings.txt')
    print(e)
    sys.exit(1)

if not standings.strip():
    print('❌ ERROR: standings.txt is empty')
    sys.exit(1)

msg = MIMEText(standings)
msg['Subject'] = 'U9G Blue Weekly Standings'
msg['From'] = os.environ.get('SMTP_USERNAME')
msg['To'] = 'tonyvanherk@gmail.com'

try:
    with smtplib.SMTP(os.environ.get('SMTP_SERVER'), int(os.environ.get('SMTP_PORT')), timeout=30) as server:
        server.starttls()
        server.login(os.environ.get('SMTP_USERNAME'), os.environ.get('SMTP_PASSWORD'))
        server.send_message(msg)
except Exception as e:
    print('❌ ERROR: Failed to send email')
    print(e)
    sys.exit(1)
