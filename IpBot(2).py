from aiogram import Bot,Dispatcher,types,executor
import requests


API_TOKEN = '6264131044:AAH4Aq3k33EG6RG5lulWKV8kyGwTnsLqGOw'
bot=Bot(API_TOKEN)
dp=Dispatcher(bot)


@dp.message_handler(chat_type=types.ChatType.PRIVATE)
async def main(msg: types.Message):
        startt=f""" Assalomu alaykum {msg.from_user.full_name} 👋🏻\n
📡 Ip adres orqali ip egasi haqida malumot va lokatsiaya oluvchi botga hush kelibsiz

🤖 Botdan foydalanish uchun ip manzil yuboring!

📠 Namuna ☛ 103.101.91.255
        
        """
        if msg.text.startswith("/start"):
            await bot.send_message(msg.chat.id,startt)
        else:
            try:
                botinfo=await bot.get_me()
                kb1=types.InlineKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
                btn1=types.InlineKeyboardButton("Botni guruhga qo'shish ➕",url=f"t.me/{botinfo.username}?startgroup=new")
                btn2=types.InlineKeyboardButton("Devloper 👨‍💻",url="t.me/KgzNet")
                kb1.add(btn1)
                kb1.add(btn2)
                res= requests.get(f"http://ip-api.com/json/{msg.text}")
                x=res.json()
                ip=f"""
🏰  Davlati  ☛ {x['country']}
🗺  Shaxari  ☛ {x['regionName']}
🕊 Davlat codi  ☛ {x['countryCode']}
🌚 Shaxar codi  ☛ {x['region']}
⏳ Vaqt mintaqasi  ☛ {x['timezone']}
                
                
                
                """
                loc=await bot.send_location(msg.chat.id,x['lat'],x['lon'])
                await bot.send_message(msg.chat.id,ip,reply_markup=kb1,reply_to_message_id=loc.message_id)
            except:
                await bot.send_message(msg.chat.id,"Bunday ip mavjud emas !!!")

executor.start_polling(dp,skip_updates=True)
