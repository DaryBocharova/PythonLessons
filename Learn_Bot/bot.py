from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem, datetime, re


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

def word_count(bot, update):
        word = update.message.text
        word_split = word.split()
        
        # print(word_split)
        if word == "/wordcount":
            empty_text = "Вы ввели пустую строку. Введите слова."
        update.message.reply_text(empty_text)
   
        # if word == "%":
        #     symbols_text = "Вы ввели символы. Введите слова"
        #     update.message.reply_text(symbols_text)
        # else: 
        users_word_count = len(word_split[1:])
        print(users_word_count)
        update.message.reply_text(users_word_count)

def full_moon(bot, update):
    word_moon = update.message.text
    # print(word_moon)
    
    today_str1 = datetime.datetime.today()
    text_moon = update.message.text[16:]
    # print(text_moon)
    # date_fullmoon = datetime.strptime(text_moon, '%Y-%d-%m')
    # print(date_fullmoon)
    next_moon = ephem.next_full_moon(today_str1)
    update.message.reply_text(next_moon)
        
  

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

# dict_city = {'Архангельск',
# 'Асбест',
# 'Астрахань',
# 'Ачинск',
# 'Балаково',
# 'Балахна',
# 'Балашиха',
# 'Златоуст',
# 'Иваново',
# 'Ивантеевка',
# 'Ижевск',
# 'Избербаш',
# 'Иркутск',
# 'Искитим',
# 'Тшим'}
# def play_city(bot, update):



 
        

def main():
    mybot = Updater("705592417:AAFcQXYDC_X2YM7SqQoIVetuvP33QSUpDqY", request_kwargs=PROXY)


    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_definition))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("wordcount", word_count))
    dp.add_handler(CommandHandler("next_full_moon", full_moon))

    mybot.start_polling()
    mybot.idle()

main()

