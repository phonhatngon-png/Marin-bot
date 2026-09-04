import discord
from discord.ext import commands
import random
import os
from flask import Flask
from threading import Thread

# Tạo web server giả lập để Render nhận diện Web Service thành công
app = Flask('')

@app.route('/')
def home():
    return "Bot is online!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Cài đặt Discord Bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

marin_quotes = [
    "Hạoo! Gọi tui có chuyện gì thế? (≧◡≦)",
    "Đồ cosplay đợt này khó quá cơ, nhưng mà vì Gojo-kun làm nên tui sẽ cố gắng hết sức! ✨",
    "Ể? Thật á? Cậu thích anime đó giống tui cơ à? Hợp cạ ghê nha! 💕",
    "Tui đói quá... Có ai tính đi ăn mì cay với tui không?",
    "Mấy món đồ này nhìn cuốn ghê á, ước gì có nhiều thời gian để xem hết ghê~",
    "Ehehe, nhìn tui trong bộ đồ này thế nào? Xinh xuất sắc đúng không nào! 🌸"
]

@bot.event
async def on_ready():
    print(f'Đã đăng nhập thành công dưới tên: {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="Mặc đồ Cosplay cùng Gojo-kun"))

@bot.command(name='marin', help='Trò chuyện cùng Kitagawa Marin')
async def chat_marin(ctx, *, message: str = None):
    reply = random.choice(marin_quotes)
    await ctx.send(f"{ctx.author.mention} {reply}")

keep_alive()
bot.run('MTU0NTQ1NzM0MTM4MDQzNTk4OA.GoBQrB.EtCCTdFUanpzPXh2ZBtPW_gBFpxc2sM6glLARQ')
