import base64
import requests
import os

def create_sound():
    file_path = 'list.txt'

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip()
            encoded_data = base64.b64encode(data.encode('utf-8'))
            encoded_string = encoded_data.decode('utf-8')

            url = 'https://voice.reverso.net/RestPronunciation.svc/v1/output=json/GetVoiceStream/voiceName=Heather22k?voiceSpeed=100&inputText=' + encoded_string
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }

            response = requests.get(url, headers = headers)

            if response.status_code == 200:
                file_path = os.path.join('media', f'{data}.mp3')
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f'Saved: {file_path}')
            else:
                print(f'Error: {response.status_code}')


create_sound()


