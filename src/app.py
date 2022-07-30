from flask import Flask, request, abort
import os
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

# from config import LINE_BOT_API, HANDLER
from modules.rezept_calculation import RezeptCalculation

app = Flask(__name__)
YOUR_CHANNEL_ACCESS_TOKEN = os.environ.get("YOUR_CHANNEL_ACCESS_TOKEN", "s8Q5GKHXNft77NFjOlxGey/w5DGMGIGPtI0VXGejD3mWZrDoP4jA1+NF7304hMKjWw+HUu8r3esiA09STedhHnmRB8tVPErjzWnO0YdhVynrDJHncdbh0WwAZQzrRS/ZJRWLOx1SG3xJRFhzvuE2dgdB04t89/1O/w1cDnyilFU=")
YOUR_CHANNEL_SECRET = os.environ.get("YOUR_CHANNEL_SECRET", "97606a458d1a1c8398558a6849e7dffd")

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/", methods=['GET'])
def test():
    try:
        return 'OKだよdd'
    except Exception as e:
        print(f"えらーろぐ{e}")

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
    app.run(port=os.environ.get("PORT", 5000), host=os.environ.get("HOST", '0.0.0.0'))
