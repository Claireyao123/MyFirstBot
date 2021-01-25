from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import BotCommand
import pafy
import os

def youtubemusic(update,context):
    if len(context.args) == 1:
        url = context.args[0]
        video = pafy.new(url)
        bestaudio = video.getbestaudio(preftype="m4a")
        filepath = f"/tmp/{bestaudio.title}.{bestaudio.extension}"
        music_size = bestaudio.get_filesize()
        if music_size > 1000*1000*10:
            update.message.reply_text("你要下载的音乐太大了！我只能处理10M的音乐🎵")
            return
        bestaudio.download(filepath=filepath)
        update.message.reply_audio(open(filepath, 'rb'),caption=str(music_size))
        os.remove(filepath)
        # update.message.reply_text(str(video) )
    else:
        update.message.reply_text("URL呢")

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('ytm', youtubemusic))

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=iqL1BLzn3qc"
    video = pafy.new(url)
    bestaudio = video.getbestaudio(preftype="m4a")
    print(bestaudio)
    filepath = f"/tmp/{bestaudio.title}.{bestaudio.extension}"
    bestaudio.download(filepath=filepath)
    print(bestaudio.url)

    