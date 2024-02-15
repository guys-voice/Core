import json
from uuid import uuid4
import requests
from flask import Flask, request
import io

BOT_TOKEN = '6814451088:AAFOLBu7M3dCI605Gol_bEccPYJNQwRcf7Q'
ADMIN = 5934725286
GROUP = 1635762236
AUTHORIZED_USER_IDS = [5934725286, 5377327708, 5817420325, 1918582402, 699882662, 1257545168, 1753264718, 1203220311, 6955248384, 752492336, 1673876488, 650599868, 1732613271, 1180727254, 1309190580, 967340481, 5322473767, 6426386490, 1036831407]
#global last_update_id

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_webhook():
    try:
        process(json.loads(request.get_data()))
        return 'Success!'
    except Exception as e:
        print(e)
        return 'Error'

def random():
    global last_update_id
    last_update_id = -1
    while True:
        updates = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={last_update_id}").json().get('result', [])
        for update in updates:
            process(update)
            last_update_id = update['update_id'] + 1

def process(update):
    if 'message' in update:
        print(update)
        if update['message']['from']['id'] not in AUTHORIZED_USER_IDS:
            return
        if 'text' in update['message']:
            if update['message']['text'] == '/manual':
                manual(update['message']['from']['id'])
            elif update['message']['text'] == '/voices':
                callback(update['message']['from']['id'], 0, 0)
            elif update['message']['text'] == '/VOICES' and update['message']['from']['id'] == ADMIN:
                send_voices()
            elif update['message']['text'] == '/FILE' and update['message']['from']['id'] == ADMIN:
                voice()
            elif 'reply_to_message' in update['message'] and 'voice' in update['message']['reply_to_message']:
                print('kelli')
                with open('voices.txt', 'r') as file:
                    lines = file.readlines()
                    updated_lines = [line for line in lines if update['message']['reply_to_message']['voice']['file_id'] != line.split()[0]]
                print(updated_lines)
                with open('voices.txt', 'w') as file:
                    file.write(f"{update['message']['reply_to_message']['voice']['file_id']} {0} {update['message']['from']['first_name'].split()[0]} {update['message']['text']}\n")
                    file.writelines(updated_lines)
                print(requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",json={'chat_id': update['message']['from']['id'],'text': '*Done!*', 'parse_mode': 'Markdown'}).json())
            else:
                # just say please first send the voice then reply to that voice with the title
                pass
        elif 'voice' in update['message']:
            # just say reply to your voice to give it a title
            pass
    elif 'inline_query' in update:
        if update['inline_query']['from']['id'] not in AUTHORIZED_USER_IDS:
            results = [{'type': 'article','title': "Access denied!",'input_message_content': {'message_text': "*Contact* ➡️ @boot\_to\_root",'parse_mode': 'Markdown'}}]
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/answerInlineQuery", data={'inline_query_id': update['inline_query']['id'],'results': json.dumps(results)})
            return
        with open('voices.txt', 'r') as file:
            lines = file.readlines()
        voices = [line for line in lines if update['inline_query']['query'].lower() in ' '.join(line.split()[3:]).lower()]
        filtered_voices = sorted(voices, key=lambda line: int(line.split()[1]), reverse=True)
        offset = int(update['inline_query']['offset']) if update['inline_query']['offset'] and update['inline_query']['offset'] != 'null' else 0
        next_offset = str(offset + 20) if offset + 20 < len(lines) else ''
        results = []
        for line in filtered_voices[offset:offset + 20]:
            results.append({'id': str(uuid4()),'voice_file_id': line.split()[0],'title': ' '.join(line.split()[3:]),'type': 'voice',})
        print(requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/answerInlineQuery", json={'inline_query_id': update['inline_query']['id'],'results': results,'next_offset': next_offset, 'cache_time': 20}, headers={'Content-Type': 'application/json'}).json())
    else:
        print(update['callback_query']['data'])
        if update['callback_query']['data'].isdigit():
            callback(update['callback_query']['from']['id'], int(update['callback_query']['data']), update['callback_query']['message']['message_id'])
        else:
            with open('voices.txt', 'r') as file:
                voices1 = file.readlines()
            for voice1 in voices1:
                if ' '.join(voice1.split()[3:]) == update['callback_query']['data']:
                    print(requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendVoice",json={'chat_id': update['callback_query']['from']['id'], 'voice': voice1.split()[0]}).json())

def callback(user_id, limit, state):
    with open('voices.txt', 'r') as file:
        lines = file.readlines()
    final = len(lines)
    reply_markup = {'inline_keyboard' : [[{'text': "######################", 'callback_data': 'xay'}]]}
    counter = 0
    for line in lines:
        if counter >= limit and counter < limit + 10:
            reply_markup['inline_keyboard'].append([{'text': f"{' '.join(line.split()[3:])}", 'callback_data': f"{' '.join(line.split()[3:])}"}])
            counter = counter + 1
        elif counter < limit:
            counter = counter + 1
        else:
            break
    if len(reply_markup['inline_keyboard']) == 1:
        print(requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage',json={'chat_id': user_id, 'text': 'That was all in my database!'}).json())
        return
    else:
        del reply_markup['inline_keyboard'][0]
    if limit == 0:
        reply_markup['inline_keyboard'].append([{'text': f"▶️️️", 'callback_data': f"{limit + 10}"}])
    elif len(reply_markup['inline_keyboard']) < 10:
        reply_markup['inline_keyboard'].append([{'text': f"◀️", 'callback_data': f"{limit - 10}"}])
    else:
        reply_markup['inline_keyboard'].append([{'text': f"◀️", 'callback_data': f"{limit - 10}"}, {'text': f"▶️️️", 'callback_data': f"{limit + 10}"}])
    if state == 0:
        print(requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage', json={'chat_id': user_id, 'text': 'Choose:','reply_markup': reply_markup}).json())
    else:
        print(requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/editMessageReplyMarkup', json={'chat_id': user_id, "message_id": state, 'reply_markup': reply_markup}).json())


def send_voices():
    with open('voices.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        print(requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendVoice",json={'chat_id': ADMIN, 'voice': line.split()[0], 'caption': line}).json())

def voice():
    with open('voices.txt', 'r') as file:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",params={'chat_id': ADMIN},files={'document': ('voices.txt', io.StringIO(''.join(file.readlines())))})
    file.close()
    return

def manual(user_id):
    print(requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/copyMessage',data={'chat_id': user_id, 'from_chat_id': ADMIN,'message_id': 2502}))

#if __name__ == '__main__':
#    random()

if __name__ == '__main__':
    app.run(debug=False)
