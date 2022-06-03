import telebot
import config, text
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Вид на проживання")
    item2 = types.KeyboardButton("Jobcenter")
    item3 = types.KeyboardButton("Житло")
    item4 = types.KeyboardButton("Робота")
    item5 = types.KeyboardButton("Корисні канали")
    item6 = types.KeyboardButton("Зв'язок з автором")
    item7 = types.KeyboardButton("Випадкове число")

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id, "Вітаю, {0.first_name}!\nЯ - <b>{1.first_name}</b>, створений щоб допомогати корисною інформацією!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Вид на проживання":
            bot.send_message(message.chat.id, text.vnp, parse_mode='html', disable_web_page_preview=True)
        elif message.text == "Jobcenter":
            
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Додаткова інформація", callback_data='dopInfoJobc')
            item2 = types.InlineKeyboardButton("Корисна інформація при реєстрації", callback_data='korInfoJobc')
            
            markup.add(item1, item2)
            
            bot.send_message(message.chat.id, text.jobcenter, parse_mode='html', disable_web_page_preview=True, reply_markup=markup)
        elif message.text == "Житло":
            bot.send_message(message.chat.id, text.zhytlo, parse_mode='html')
        elif message.text == "Робота":
            bot.send_message(message.chat.id, text.robota, parse_mode='html')
        elif message.text == "Корисні канали":
            bot.send_message(message.chat.id, text.links, parse_mode='html')
        elif message.text == 'Випадкове число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == "Зв'язок з автором":
            bot.send_message(message.chat.id, "Якщо у Вас є правильніша чи більш повна інформація, "
                                              "або ж пропозиції чи побажання - можете зв'язатись в телеграмі з @hdrhighd")
        elif (message.text == "Слава Україні!") or (message.text == "слава Україні!") or (message.text == "слава україні!") or (message.text == "Слава україні!") or (message.text == "Слава Україні") or (message.text == "слава Україні") or (message.text == "слава україні") or (message.text == "Слава україні"):
            bot.send_message(message.chat.id, "Героям слава!")
        elif (message.text == "Слава Нації!") or (message.text == "слава Нації!") or (message.text == "слава нації!") or (message.text == "Слава Нації") or (message.text == "слава Нації") or (message.text == "слава нації") or (message.text == "Слава нації") or (message.text == "Слава нації!"):
                bot.send_message(message.chat.id, "П@^!&ць російській федерації")
        else:
            answers = ["Перепрошую, я би з задоволенням поспілкувався з Вами, але я ще не навчився",
                       "Навіть не знаю що тут відповісти",
                       "Краще Вам поспілкуватись з моїм автором", "Мрію стати людиною, щоб бути Українцем!", "Хочу борщу",
                       "На жаль, я поки що не можу відповідати на повідомлення, знаю відповідь тільки на декілька 🙃", "З радістю би відповів, але я поки що не можу"]
            random_message = lambda : random.choice(answers)
            bot.send_message(message.chat.id, random_message())

@bot.callback_query_handler(func=lambda call: True)
def callback_inline_jobc(call):
    try:
        if call.message:
            if call.data == 'dopInfoJobc':
                bot.send_message(call.message.chat.id, text.dopInfoJobc, parse_mode='html')
            elif call.data == 'korInfoJobc':
                bot.send_message(call.message.chat.id, text.korInfoJobc, parse_mode='html')

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                 text="Для отримання максимально достовірної інформації краще про все запитати працівника Jobcenter при реєстрації!")

    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)