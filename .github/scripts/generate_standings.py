import os
import sys
import openai

api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    print('❌ ERROR: Missing OPENAI_API_KEY environment variable')
    sys.exit(1)

client = openai.OpenAI(api_key=api_key)

try:
    with open('games.txt', 'r', encoding='utf-8') as f:
        games_text = f.read()
except Exception as e:
    print('❌ ERROR: Could not read games.txt')
    print(e)
    sys.exit(1)

if len(games_text.strip()) < 50:
    print('❌ ERROR: games.txt is too small — scraping likely failed')
    sys.exit(1)

prompt = f"""
Here is a full text dump of a soccer schedule webpage. Extract only completed
games from the U9G Blue division. Ignore future-dated games and BYE games.
Calculate standings using:
- 3 points for a win
- 1 point for a draw
- 0 points for a loss

Return a clean table in this format:

Team | GP | W | D | L | GF | GA | GD | Points

Here is the schedule text:
{games_text}
"""

try:
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role':'user','content':prompt}]
    )
    standings = response.choices[0].message['content']
except Exception as e:
    print('❌ ERROR: ChatGPT API call failed')
    print(e)
    sys.exit(1)

if not standings.strip():
    print('❌ ERROR: ChatGPT returned empty standings')
    sys.exit(1)

try:
    with open('standings.txt', 'w', encoding='utf-8') as f:
        f.write(standings)
except Exception as e:
    print('❌ ERROR: Failed to write standings.txt')
    print(e)
    sys.exit(1)
