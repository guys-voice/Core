import json
import requests
from uuid import uuid4
from datetime import datetime, timedelta

# here are the global variables
from variables import BOT_TOKEN, ADMIN, GROUP, COMMANDS, AUTHORIZED_USER_IDS, VOICES, SPECIAL, last_update_id, last_sent_time

# importing core functions
import voice, inline, commands, special, log

def main():
    global last_update_id
    while True:
        updates = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={last_update_id}").json().get('result', [])
        for update in updates:
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
                    if any(update['message']['text'] == voice[1] for voice in VOICES): #not efficient though
                        voice.message_auth_voice(update['message']['from']['id'], update['message']['text'])
                    elif update['message']['text'] in COMMANDS:
                        commands.commands(update['message']['from']['id'], update['message']['from']['first_name'], update['message']['text'])
                    elif any(keyword in update['message']['text'] for keyword in SPECIAL) and update['message']['from']['id'] == ADMIN:
                        special.special(update['message']['text'])
                    else:
                        log.ignore()
                        log.log_ignore(update)
                else:
                    voice.message_unauth(update['message']['from']['id'])
                    log.log_unauth(update)
            else:
                log.ignore()
                log.log_ignore(update)
            last_update_id = update['update_id'] + 1
# used to start the program
if __name__ == "__main__":
    main()
