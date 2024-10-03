import telebot

API_TOKEN = '6416867391:AAE6LEWcWd9w-h91WzlJ86JtTwkyfIIZhUM'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def enviar_ola(message):
    if message.from_user.username is None:
        username = "'Sem Nome de Usuário'"
    else:
        username = message.from_user.username
    
    bot.reply_to(message, f"Olá, Bem Vindo {username}!")
    print(username)

@bot.message_handler(commands=['user'])
def name_user(message):
    
    user = message.from_user

    full_name = f"{user.first_name} {user.last_name if user.last_name else ''}".strip()

    first_name = user.first_name
    last_name = user.last_name

    username = user.username

    response = (
        f'Nome Completo: {full_name}\n'
        f'Primeiro Nome: {first_name}\n'
        f'Último Nome: {last_name}\n'
        f'Nome Usuárrio: {username}'
    )
    bot.reply_to(message, response)

bot.infinity_polling()