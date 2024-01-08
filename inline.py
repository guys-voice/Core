import json
import requests
from uuid import uuid4
from variables import BOT_TOKEN, ADMIN, VOICES

def inline_unauth(update):
    results = [
        {
            'type': 'article',
            'id': str(uuid4()),
            'title': "Access denied!",
            'input_message_content': {
                'message_text': "*Contact* ➡️ @boot\_to\_root",
                'parse_mode': 'Markdown'
            }
        }
    ]
    data = {
        'inline_query_id': update['inline_query']['id'],
        'results': json.dumps(results)
    }
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/answerInlineQuery", data=data)
        
def inline_auth(update):
    filtered_voices = [(url, title) for url, title in VOICES if update['inline_query']['query'].lower() in title.lower()]
    offset = int(update['inline_query']['offset']) if update['inline_query']['offset'] and update['inline_query']['offset'] != 'null' else 0
    next_offset = str(offset + 20) if offset + 20 < len(VOICES) else ''
    results = []
    if update['inline_query']['from']['id'] == ADMIN:
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
    data = {
        'inline_query_id': update['inline_query']['id'],
        'results': results,
        'next_offset': next_offset
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/answerInlineQuery", json=data, headers=headers)
