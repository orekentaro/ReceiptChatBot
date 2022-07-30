from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from config import LINE_BOT_API, HANDLER
from modules.rezept_calculation import RezeptCalculation

app = Flask(__name__)

line_bot_api = LineBotApi(LINE_BOT_API)
handler = WebhookHandler(HANDLER)


@app.route("/", methods=['GET'])
def test():
    return 'OKだよdd'


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    total, contact = map(int, event.message.text.split(' '))
    rezept = RezeptCalculation(total, contact)
    resutl = rezept.serialization(rezept.main())
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=resutl))


if __name__ == "__main__":
    app.run()