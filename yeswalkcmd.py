from telegram.ext import Dispatcher,CommandHandler
import random
result6 = ["海风吹过面颊，兴奋的船员们安静了下来。哦不！你们遇到了巨乌贼海怪克拉肯！战斗还是逃跑？\n输入 /fight 来战斗\n输入 /run 来逃跑", "船员们因为失眠而吊儿郎当。哦不！你们遇到了巨乌贼海怪克拉肯！战斗还是逃跑？\n输入 /fight 来战斗\n输入 /run 来逃跑", "就算你竭尽全力去安抚大家，水手们还是对你不满。哦不！你们遇到了巨乌贼海怪克拉肯！战斗还是逃跑？\n输入 /fight 来战斗\n输入 /run 来逃跑"]

def yeswalk(update, context):
    update.message.reply_text(random.choice(result6))



def add_handler(dp:Dispatcher):
    yeswalk_handler = CommandHandler('yeswalk', yeswalk)
    dp.add_handler(yeswalk_handler)