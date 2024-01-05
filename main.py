import os
from uuid import uuid4
from datetime import datetime, timedelta
import requests
import json

# here are the global variables

from variables import BOT_TOKEN, ADMIN, GROUP, AUTHORIZED_USER_IDS, last_id_update, voices

# used to handle inline requests and send results if the user is authorised and ignore and pass in to upcoming function otherwise
def inline_query(update):
    user_id = update['inline_query']['from']['id']
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
        send_unauthorized_access_alert(ADMIN, user_id, update)
        send_inline_query_message(update['inline_query']['id'], results)
        return

    query = update['inline_query']['query'].lower()
    filtered_voices = [(url, title) for url, title in voices if query in title.lower()]

    offset = int(update['inline_query']['offset']) if update['inline_query']['offset'] and update['inline_query']['offset'] != 'null' else 0
    next_offset = str(offset + 20) if offset + 20 < len(voices) else ''

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
    send_inline_query_results(update['inline_query']['id'], results, next_offset)
    send_audio_access_notification(ADMIN, user_id, update['inline_query']['from']['first_name'])

# used to actually send the inline text to unauthorised user
def send_inline_query_message(inline_query_id, results):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/answerInlineQuery"
    data = {
        'inline_query_id': inline_query_id,
        'results': json.dumps(results)
    }
    requests.post(url, data=data)

# used to send the alert to ADMIN about who has used the bot AND also to send the notification message to the GROUP
def send_audio_access_notification(chat_id, user_id, name):
    global last_sent_time
    now = datetime.now()

    if last_sent_time and now - last_sent_time < timedelta(minutes=1):
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    text = f"Authorized inline use. ID: {user_id} , Name: {name}"
    data = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, data=data)
    requests.post(url, data={'chat_id': GROUP, 'text': "tezroq tanla."})
    if response.status_code == 200:
        last_sent_time = now
    else:
        print(f"Failed to send notification: {response.content}")

# used to alert both the ADMIN and the unauthorised user about the unauthorised use

def send_unauthorized_access_alert(chat_id, unauthorized_user_id, update):
    try:
        name = update['inline_query']['from']['first_name']
    except:
        name = update['inline_query']['from']['first_name']

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    text1 = f"Unauthorized use has been detected! ID: {unauthorized_user_id}, Name: {name}"
    text2 = (f"Hmm, I understand that you are very curious, but I can not share anything with you right now! Try "
             f"contacting @boot_to_root . Your ID: {unauthorized_user_id}.")
    data2 = {
        'chat_id': unauthorized_user_id,
        'text': text2
    }
    data1 = {
        'chat_id': chat_id,
        'text': text1
    }
    requests.post(url, data=data1)
    requests.post(url, data=data2)

# used to send inline voices with offsets

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

def send_actual_voices_to_dm(update):
    user_id = update['message']['from']['id']
    user_text = update['message']['text']
    print(f"User Text: {user_text}")
    found = False
    # Check if the user's message matches any title in the voices[1] array
    for i in range(200):
        if user_text.lower() == voices[i][1].lower():
            voice_url = voices[i][0]
            found = True

    if found:
        # Use sendVoice method for sending voice messages
        data = {
            'chat_id': user_id,
            'voice': voice_url,
            'caption': f"Here is the voice",
            'parse_mode': 'Markdown',
        }

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVoice"
        response = requests.post(url, json=data)

# forwards the request to a specific function. serves as a transformer between actually working functions
def process_update(update):
    global last_update_id
    if 'inline_query' in update:
        inline_query(update)
    elif 'message' in update and 'text' in update['message']:
        send_actual_voices_to_dm(update)
    last_update_id = update['update_id'] + 1
    # here you will write the function that handles direct messages
    return

# Function to get actual updates from the bot's API
def get_updates():
    global last_update_id
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={last_update_id}"
    response = requests.get(url)
    if response.status_code == 200:
        updates = response.json().get('result', [])
        return updates
    else:
        print(f"Error getting updates: {response.status_code}")
        print(f"Response content: {response.content}")
        return []

# Main function
def main():
    global last_update_id
    # used for continuous check
    while True:
        updates = get_updates()
        for update in updates:
            process_update(update)

# used to start the program
if __name__ == "__main__":
    last_update_id = -1
    print('Bot starts working...')
    main()
