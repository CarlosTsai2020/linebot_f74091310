import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from utils import send_text_message,send_image_message
from machine import create_machine

load_dotenv()
machines={} # unique fsm for multiple users

app = Flask(__name__, static_url_path='')

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

@app.route('/callback', methods=['POST'])
def webhook_handler():
    global mode
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f'Request body: {body}')

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        # create a machine for each user
        if event.source.user_id not in machines:
            machines[event.source.user_id]=create_machine()

        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue

        response = machines[event.source.user_id].advance(event)
        if response == False:
            if event.message.text.lower() == 'fsm':
                send_image_message(event.reply_token, 'https://www.linkpicture.com/q/fsm.png')
            elif machines[event.source.user_id].state == 'init':
                send_text_message(event.reply_token, '????????????????????????\n??????\"??????\"????????????')

        print(f'\nFSM STATE: {machines[event.source.user_id].state}')
        print(f'REQUEST BODY: \n{body}')

    return 'OK'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    fsm=create_machine()
    fsm.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file('./fsm.png', mimetype='image/png')


if __name__ == '__main__':
    port = os.environ.get('PORT', 8000)
    app.run(host='0.0.0.0', port=port, debug=True)
