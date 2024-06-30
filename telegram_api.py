import asyncio
import json
import logging
from telegram import Update, Bot, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, ReplyKeyboardRemove, \
    InlineKeyboardMarkup, InlineKeyboardButton, MessageEntity
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

request_kwargs = {'proxy_url': 'socks5://127.0.0.1:10809/'}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_chat.id)
    print(update.message)
    await context.bot.send_
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def start1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with a button that opens a the web app."""
    await update.message.reply_text(
        "Please press the button below to choose a color via the WebApp.",
        reply_markup=ReplyKeyboardMarkup.from_button(
            KeyboardButton(
                text="Open the color picker!",
                web_app=WebAppInfo(url="https://python-telegram-bot.org/static/webappbot"),
            )
        ),
    )


async def start2(update: Update, context) -> None:
    """Display a message with a button."""
    await update.message.reply_html(
        "This button was clicked <i>0</i> times.",
        reply_markup=InlineKeyboardMarkup.from_button(
            InlineKeyboardButton(text="Click me!", callback_data="button")
        ),
    )


async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Print the received data and remove the button."""
    # Here we use `json.loads`, since the WebApp sends the data JSON serialized string
    # (see webappbot.html)
    # data = json.loads(update.effective_message.web_app_data.data)

    html_message = ('<img src="https://pbs.twimg.com/media/GRNDcsgWAAAOrg7.jpg">樱花树下的粉发少女，日本动画风格，柔和色调。\n![粉发少女](https://pbs.twimg.com/media/GRNDcsgWAAAOrg7.jpg)')
    h = "这是一段视频: \n![点击观看](https://www.runoob.com/try/demo_source/movie.mp4)"
    # 创建消息实体，指定图片链接
    image_url = "https://pbs.twimg.com/media/GRNDcsgWAAAOrg7.jpg"
    message_entities = [
        MessageEntity(type=MessageEntity.TEXT_LINK,
                      offset=23,  # 从哪个字符开始
                      length=len(image_url),  # 链接的长度
                      url=image_url)
    ]

    await update.message.reply_text(
        parse_mode="Markdown",
        text=h,
        # entities=message_entities
        # reply_markup=ReplyKeyboardRemove(),
    )

    html_message = "樱花树下的粉发少女，日本动画风格，柔和色调。"

    # 创建一个内联键盘按钮，链接到图片
    inline_keyboard = [
        [InlineKeyboardButton("查看图片", url="http://example.com/image.jpg")]
    ]

    # 创建内联键盘的布局
    reply_markup = InlineKeyboardMarkup(inline_keyboard)

    # 发送消息，设置parse_mode为'HTML'，并添加内联键盘
    await update.message.reply_text(html_message, parse_mode='HTML', reply_markup=reply_markup)


async def send(text:str):
    proxy_url = "http://127.0.0.1:10809"
    application = ApplicationBuilder().token('7288765779:AAG1E_xRtg8WJ40tt349nl-ZneB_qGnOhcs') \
        .proxy_url(proxy_url).get_updates_proxy_url(proxy_url).build()
    await application.bot.send_message(chat_id=7385540771, text=text)


async def bot_send_message():

    bot = Bot("7288765779:AAG1E_xRtg8WJ40tt349nl-ZneB_qGnOhcs")
    async with bot:
        await bot.send_message(text='Hi John!', chat_id=7385540771)

if __name__ == '__main__':
    # send()
    proxy_url = "http://127.0.0.1:10809"
    application = ApplicationBuilder().token('7288765779:AAG1E_xRtg8WJ40tt349nl-ZneB_qGnOhcs')\
        .proxy_url(proxy_url).get_updates_proxy_url(proxy_url).build()

    start_handler = CommandHandler('start', start)
    start_handler1 = CommandHandler('start1', start1)
    application.add_handler(start_handler)
    application.add_handler(CommandHandler('start1', start1))
    application.add_handler(CommandHandler('start2', start2))
    application.add_handler(CommandHandler('web_app_data', web_app_data))
    application.run_polling()

    # asyncio.run(send())
