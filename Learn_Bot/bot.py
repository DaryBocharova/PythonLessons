from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem, datetime


PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(bot, update):
    text1 = 'вызов /start'
    text = update.message.reply_text(text1)
    print(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def planet_definition(bot, update):
    today_str = datetime.datetime.today()
    text_split = update.message.text.split()
    text = text_split[1].capitalize()
    if text == 'Mercury':
        const = ephem.constellation(ephem.Mercury(today_str))
        print(const)
    elif text == 'Venus':
        const = ephem.constellation(ephem.Venus(today_str))
        print(const)
    elif text == 'Earth':
        const = ephem.constellation(ephem.Earth(today_str))
        print(const)
 
        

def main():
    mybot = Updater("705592417:AAFcQXYDC_X2YM7SqQoIVetuvP33QSUpDqY", request_kwargs=PROXY)


    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_definition))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()

