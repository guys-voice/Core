import json
import requests
from uuid import uuid4
from flask import Flask, request
from datetime import datetime, timedelta
import time

app = Flask(__name__)


@app.route('/', methods=['POST'])
def handle_webhook():
    try:
        process(json.loads(request.get_data()))
        return 'Success!'
    except Exception as e:
        return e


from variables import BOT_TOKEN, ADMIN, GROUP, COMMANDS, AUTHORIZED_USER_IDS, VOICES, SPECIAL, last_sent_time

# importing core functions
import voice, inline, commands, special, log


def process(update):
    if 'inline_query' in update:
        if update['inline_query']['from']['id'] in AUTHORIZED_USER_IDS:
            log.log_auth(update)
            inline.inline_auth(update)
        else:
            inline.inline_unauth(update)
            log.log_unauth(update)
    elif 'message' in update and 'text' in update['message']:
        if update['message']['from']['id'] in AUTHORIZED_USER_IDS:
            log.log_auth(update)
            if any(update['message']['text'] == voice[1] for voice in VOICES):  # not efficient though
                voice.message_auth_voice(update['message']['from']['id'], update['message']['text'])
            elif update['message']['text'] in COMMANDS:
                commands.commands(update['message']['from']['id'], update['message']['from']['first_name'],
                                  update['message']['text'])
            elif update['message']['text'][
                 :12] == 'SEND_MESSAGE':  # any(keyword in update['message']['text'][:12] for keyword in SPECIAL) and update['message']['from']['id'] == ADMIN:
                special.special(update['message']['text'])
            elif update['message']['text'] == '/Hammasi':
                count = 1
                for i in range(len(VOICES)):
                    if count <= 295:
                        count = count + 1
                        continue
                    data = {
                        'chat_id': update['message']['from']['id'],
                        'voice': VOICES[i][0],
                    }
                    reply_id = \
                    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendVoice", json=data).json()['result'][
                        'message_id']
                    print(requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage',
                                        json={'chat_id': update['message']['from']['id'], 'text': f"{VOICES[i][1]}",
                                              'reply_to_message_id': reply_id}).json())
            else:
                log.ignore()
                log.log_ignore(update)
        else:
            voice.message_unauth(update['message']['from']['id'])
            log.log_unauth(update)
    else:
        log.ignore()
