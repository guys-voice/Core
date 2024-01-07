import json
import requests
from uuid import uuid4
from variables import BOT_TOKEN, ADMIN, GROUP, COMMANDS, AUTHORIZED_USER_IDS, VOICES, last_update_id, last_sent_time

def inline_query(user_id, query, off):
    if user_id not in AUTHORIZED_USER_IDS:
        unauthorized_message = "*Contact* ➡️ @boot\_to\_root"

        results = [
            {
                'type': 'article',
                'id': str(uuid4()),
                'title': "Access denied!",
                'input_message_content': {
                    'message_text': unauthorized_message,
                    'parse_mode': 'Markdown'
                }
            }
        ]
        send_inline_query_message(user_id, results)
        return
    filtered_voices = [(url, title) for url, title in VOICES if query in title.lower()]

    offset = int(off) if off and off != 'null' else 0
    next_offset = str(offset + 20) if offset + 20 < len(VOICES) else ''

    results = []

    if user_id == ADMIN:
        caption = '෴'
    else:
        caption = ''

    for voice_url, title in filtered_voices[offset:offset+20]:
        results.append({
            'id': str(uuid4()),
            'voice_url': voice_url,
            'title': title,
            'type': 'voice',
            'caption': caption #(caption function doesnot work as expected)
        })
    send_inline_query_results(user_id, results, next_offset)

# used to actually send the inline text to unauthorised user
def send_inline_query_message(inline_query_id, results):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/answerInlineQuery"
    data = {
        'inline_query_id': inline_query_id,
        'results': json.dumps(results)
    }
    requests.post(url, data=data)

def send_inline_query_results(inline_query_id, results, offset):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/answerInlineQuery"
    data = {
        'inline_query_id': inline_query_id,
        'results': results,
        'next_offset': offset
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)
