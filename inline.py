import VOICES from variables # importing this to only main.py is good enough

def inline_unauth(user_id):
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
        'inline_query_id': user_id,
        'results': json.dumps(results)
    }
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/answerInlineQuery", data=data)

def inline_auth(user_id, query, offset):
    filtered_voices = [(url, title) for url, title in VOICES if query in title.lower()]
    offset = int(offset) if offset and offset != 'null' else 0
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
    data = {
        'inline_query_id': user_id,
        'results': results,
        'next_offset': next_offset
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/answerInlineQuery", json=data, headers=headers)
