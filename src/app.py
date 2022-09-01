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
from modules.recept_calculation import ReceiptCalculation

app = Flask(__name__)
YOUR_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_BOT_CHANNEL_TOKEN", "")
YOUR_CHANNEL_SECRET = os.environ.get("LINE_BOT_CHANNEL_SECRET", "")

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/", methods=['GET'])
def test():
    try:
        return "ok"
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
    try:
        if (text := event.message.text) in "使い方" or text in "教えて":
            result = "【使い方】\n"
            result += "メッセージを入力のフォームに半角で『総件数』『スペース』『CL件数』を入れて送信ボタンを押してね！\n"
            result += "例）785 344"
        else:
            total, contact = map(int, text.split(' '))
            receipt = ReceiptCalculation(total, contact)
            result = receipt.serialization(receipt.main())
    except Exception as e:
        print('エラー:', e)
        result = "例に倣って送ってね！\n"
        result += "メッセージを入力のフォームに半角で『総件数』『スペース』『CL件数』\n"
        result += "例）785 344"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result))


if __name__ == "__main__":
    app.run(port=os.environ.get("PORT", 5000),
            host=os.environ.get("HOST", '0.0.0.0'))
