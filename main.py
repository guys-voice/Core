import json
import requests
from uuid import uuid4
from datetime import datetime, timedelta

# here are the global variables
from variables import BOT_TOKEN, ADMIN, GROUP, COMMANDS, AUTHORIZED_USER_IDS, voices, last_update_id, last_sent_time

# importing core functions
import voice, commands, log
from inline import inline_auth

def main():
    global last_update_id
    while True:
        updates = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={last_update_id}").json().get('result', [])
        for update in updates:
            if 'inline_query' in update:
                user_id = update['inline_query']['from']['id']
                if user_id in AUTHORIZED_USER_IDS:
                    log.log_auth(update)
                    inline.inline_auth(user_id, update['inline_query']['query'].lower(), update['inline_query']['offset'])
                else:
                    inline.inline_unauth()
                    log.log_unauth()
            elif 'message' in update:
                user_id = update['message']['from']['id']
                if user_id in AUTHORIZED_USER_IDS:
                    log.log_auth(update)
                    if any(update['message']['text'] == voice[1] for voice in VOICES): #not efficient though
                        voice.message_auth_voice(user_id, update['message']['text'])
                    elif update['message']['text'] in COMMANDS:
                        commands.commands()
                    else:
                        log.ignore()
                        log.log_ignore(update)
                else:
                    voice.message_unauth(user_id)
                    log.log_unauth(update)
            else:
                log.ignore()
                log.log_ignore(update)
            last_update_id = update['update_id'] + 1
# used to start the program
if __name__ == "__main__":
    main()
