import requests
import telebot
from config import TOKEN
import logging

logging.basicConfig(level=logging.INFO)

bot = telebot.TeleBot(TOKEN)# бот в тг @booknig11_bot

logging.info(bot.get_me()) # чтобы запустить в одном терминале открываем апи апп и в другом python bot.py

user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "Привет!\n\n"
        "/books - список книг\n"
        "/books_db - книги из базы\n"
        "/add_book - добавить книгу"
    )
    bot.send_message(message.chat.id, text)



@bot.message_handler(commands=['add_book'])
def add_book(message):
    user_states[message.chat.id] = 'waiting_book'

    bot.send_message(
        message.chat.id,
        'Введите книгу:\nНазвание;Автор;Жанр;Год;Описание'
    )



@bot.message_handler(commands=['books'])
def get_books(message):

    try:
        response = requests.get('http://127.0.0.1:5000/api/books/')
        books = response.json()

        text = ""

        for book in books:
            text += (
                f"{book['title']}\n"
                f"Автор: {book['author']}\n"
                f"Жанр: {book['genre']}\n\n"
            )

        bot.send_message(message.chat.id, text or "Пусто")

    except Exception as e:
        bot.send_message(message.chat.id, f"API error: {e}")



@bot.message_handler(commands=['books_db'])
def get_books_db(message):

    try:
        response = requests.get('http://127.0.0.1:5000/api/books_db/')
        books = response.json()

        text = ""

        for book in books:
            text += (
                f"{book['title']}\n"
                f"Автор: {book['author']}\n"
                f"Жанр: {book['genre']}\n\n"
            )

        bot.send_message(message.chat.id, text or "Пусто")

    except Exception as e:
        bot.send_message(message.chat.id, f"API error: {e}")

@bot.message_handler(content_types=['text'])
def handle_message(message):

    if message.text.startswith('/'):
        return

    chat_id = message.chat.id

    if user_states.get(chat_id) == 'waiting_book':
        try:
            title, author, genre, year, description = message.text.split(';')

            data = {
                "title": title,
                "author": author,
                "genre": genre,
                "year": int(year),
                "description": description
            }

            response = requests.post(
                'http://127.0.0.1:5000/api/books_db/',
                json=data
            )

            if response.status_code == 200:
                bot.send_message(chat_id, 'Книга добавлена')
            else:
                bot.send_message(chat_id, f'Ошибка API: {response.status_code}')

        except Exception as e:
            bot.send_message(chat_id, f'Неверный формат: {e}')

        user_states.pop(chat_id, None)

bot.remove_webhook()

logging.info("BOT STARTED")

bot.infinity_polling(
    skip_pending=True,
    timeout=30,
    long_polling_timeout=30
)