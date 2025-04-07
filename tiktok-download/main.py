import requests
import telebot
import tiktok
from telebot import types

bot = telebot.TeleBot('API_TOKEN')


def get_video(url) -> str:
    response = requests.get(url)

    video_id = tiktok.get_tiktok_video_id(response.url)

    return video_id


@bot.message_handler(commands=['start'])
def start(message):
    link = bot.send_message(message.chat.id, 'Отправьте ссылку на видео.')
    bot.register_next_step_handler(link, download_video_from_tiktok)


def download_video_from_tiktok(message):
    bot.reply_to(message, '🔄 Загрузка видео...')
    tiktok.tiktok(message.text)
    video_id = get_video(message.text)
    video = open(f'{video_id}.mp4', 'rb')
    bot.send_video(message.chat.id, video)
    os.remove(f'{video_id}.mp4')


print('Bot started.')

bot.polling(none_stop=True)
