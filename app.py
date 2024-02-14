import json
from uuid import uuid4
import requests
from flask import Flask, request
import io

BOT_TOKEN = '6966843961:AAH7Xd9joskzqexl--ixR1i0I25v6CyUPJw'
ADMIN = 5934725286
GROUP = 1635762236
AUTHORIZED_USER_IDS = [5934725286, 5377327708, 5817420325, 1918582402, 699882662, 1257545168, 1753264718, 1203220311, 6955248384, 752492336, 1673876488, 650599868, 1732613271, 1180727254, 1309190580, 967340481, 5322473767, 6426386490, 1036831407]

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_webhook():
    try:
        process(json.loads(request.get_data()))
        return 'Success!'
    except Exception as e:
        print(e)
        return 'Error'





def process(update):
    if 'message' in update:
        if update['message']['from']['id'] not in AUTHORIZED_USER_IDS:
            return
        if 'text' in update['message']:
            if update['message']['text'] == '/mannual':
                manual(update['message']['from']['id'])
            elif update['message']['text'] == '/VOICES' and update['message']['from']['id'] == ADMIN:
                send_voices()
            elif update['message']['text'] == '/FILE' and update['message']['from']['id'] == ADMIN:
                voice()
            elif 'reply_to_message' in update['message'] and 'voice' in update['message']['reply_to_message']:
                with open('voices.txt', 'r') as file:
                    lines = file.readlines()
                    updated_lines = [line for line in lines if update['message']['reply_to_message']['file_id'] != line.split()[0]]
                with open('users.txt', 'w') as file:
                    file.write(f"{update['message']['reply_to_message']['file_id']} {0} {update['message']['from']['first_name'].split()[0]} {update['message']['text']}\n")
                    file.writelines(updated_lines)
            else:
                # just say please first send the voice then reply to that voice with the title
                pass
        elif 'voice' in update['message']:
            # just say reply to your voice to give it a title
            pass
    else: #'inline_query' in update:
        if update['inline_query']['from']['id'] not in AUTHORIZED_USER_IDS:
            results = [{'type': 'article','title': "Access denied!",'input_message_content': {'message_text': "*Contact* ➡️ @boot\_to\_root",'parse_mode': 'Markdown'}}]
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/answerInlineQuery", data={'inline_query_id': update['inline_query']['id'],'results': json.dumps(results)})
            return
        with open('voices.txt', 'r') as file:
            lines = file.readlines()
        voices = [line for line in lines if update['inline_query']['query'].lower() in line.split()[3].lower()]
        filtered_voices = sorted(voices, key=lambda line: int(line.split()[1]), reverse=True)
        offset = int(update['inline_query']['offset']) if update['inline_query']['offset'] and update['inline_query']['offset'] != 'null' else 0
        next_offset = str(offset + 20) if offset + 20 < len(lines) else ''
        results = []
        for line in filtered_voices[offset:offset + 20]:
            results.append({'id': str(uuid4()),'voice_file_id': line.split()[0],'title': line.split()[3],'type': 'voice',})
        print(requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/answerInlineQuery", json={'inline_query_id': update['inline_query']['id'],'results': results,'next_offset': next_offset}, headers={'Content-Type': 'application/json'}))
def send_voices():
    with open('voices.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        print(requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendVoice",json={'chat_id': ADMIN, 'voice': line.split()[0], 'caption': line}).json())

def voice():
    with open('referral.txt', 'r') as file:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",params={'chat_id': ADMIN},files={'document': ('Referral.txt', io.StringIO(''.join(file.readlines())))})
    file.close()
    return

def manual():
    pass

if __name__ == '__main__':
    app.run(debug=False)
