import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

import random

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://yandex-images.clstorage.net/h5LJ02E31/3d1e8bLQkq/Caq7G8BsK8I-QPOA47ZlW92yMK6Nlkp4pS3n6J0W_Q6s_WVLIPJvan4EXE3gQ5BHGwlH2Kvvjzud7YlJ3WdEe0ryrVeGKDOZYwXr1Ou1YFnA73O_kcxOJb9vu7eIGfZSrvgPIwTWH1YHNCZvmDrdEUxVGsS0pMxdoan8FPFOUioXhq4fw0Vq1jhUrrPonm9Qw_o5oo_cdhe9CJK8n0XOGvqgAzQzxidgDiUMQJ8CwSJEfBfayZjtb5vOyC7BV2cpE76GL9dSY9YSXr-o8LxFVcLtKLq61lImuwa-rp5n0yzcmxMPKsQ_XiEgB0ajHtQHa3MM6des2me24-0v3ENnLC6Srg7WWkvjIH-RtPaXY3jm6BSPks5KAosMsI-hZfIXy5onDRPiNmMKEydNpRrLOWhZC_fxl8l1p9D1Jel0XyQVspsP3nRB7Ahmm5TnnGR4zvgKqLvrUS6eA7CommjuOe-AOxU8widoJA83aZsW8TpIcxPO373-bJDn8zr1cnAGGYWtIvtQTcQRe5Gs1rZEdNHeFaKy9GQkoQS0u4hs9xn2szcwNeI2XgsEK02DIM4HY2YP0sqU1W2L4uoW03tRPjeHuw_ebEHgPFW-q-qwbUrx7R-RgOhlP4MHvoq7Y80ryaIRBjb4Nl8RIyNSvDzAI3BcEtvwh_JWsN_sDvZkQDwLhI42xXdczh9ZkrbDu2ZqyvkNoIv8cAufPpC4k0rXLOWMHzgDwgpZBh4jfIUZzQplQyzS0aLJQa7Nzwz4SmQCL66pAvdlRv48fpqy7rxVZsb7BIyszGcIowurtr5vzB7-gjMyB9I-Wj0iAE-CDfQVbWYH6cqDz06rxPMtwW5SKRa4qjLWe23dP12ageiWTUvX1xGOmtxvEokzvKyeTtcpxqoBHw_DKH0FKiJAtQH2BGdZJ9fXg81yid7gMtZ7Twc5ibc-6H5v6w5QqYvGrnZGyes3iZ_Uew2LJ7Sdrmk', 'https://avatars.mds.yandex.net/i?id=898e6d6ea798c9ea51c40d3a435bde2746f4edcd-9878235-images-thumbs&n=13', 'https://avatars.mds.yandex.net/i?id=79bde58bfdde4ceac6de4eba8ce0ec468ed53fb3-9220617-images-thumbs&n=13']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Слоники')


@dp.message(F.photo)
async def react_photo(message: Message):
    list =['Ого какая фотка', 'Не понятно что тут изображено','Не присылай мне это больше']
    rand_ans =random.choice(list)
    await message.answer(rand_ans)
    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg')

@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer('ИИ это искуственный интеллект')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять комманды: \n /start \n /help ')

@dp.message()
async def start(message: Message):
    if message.text.lower() == 'test':
        await message.answer('Тестируем')
    #await message.answer(f'Привет, {message.from_user.first_name}')



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())