import requests
import random
import aiogram
import asyncio
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
async def send_messages():
    # Inicia el bot
    bot = aiogram.Bot(token='Tu Bot token aqui')
    chat_id = '@de tu canal o id'



    # Lee el archivo de texto
    with open('apibin.txt') as file:
        lines = file.readlines()

    # Itera sobre las líneas del archivo de texto y envía cada mensaje al canal
    for line in lines:
        # Elimina los últimos 4 dígitos del número de tarjeta
        linea = line[:28]
        card_number = line[:12]

        # Verifica el bin de la tarjeta
        # Verifica el bin de la tarjeta
        BIN = card_number[:6]
        req = requests.get(f"https://bins.antipublic.cc/bins/{BIN}").json()

        # Capturando los valores de la respuesta JSON
        brand = req['brand']
        country = req['country']
        country_name = req['country_name']
        country_flag = req['country_flag']
        country_currencies = req['country_currencies']
        bank = req['bank']
        level = req['level']
        typea  = req['type']



        # Genera una fecha aleatoria en el rango de los últimos 5 años
        month = str(random.randint(1, 12)).zfill(2)

        # Genera un año aleatorio de dos dígitos (entre 22 y 29)
        year = str(random.randint(23, 29)).zfill(2)
        button_referencias = InlineKeyboardButton("Channel Oficial", url="https://t.me/+ZUb-tqFv--FhN2Jh")
        button_comprar_premium = InlineKeyboardButton("Bot Oficial", url="https://t.me/HyugaChk_bot")

        # Agrega los botones a una lista
        keyboard = [[button_referencias, button_comprar_premium]]

        # Crea el objeto InlineKeyboardMarkup con la lista de botones
        reply_markup = InlineKeyboardMarkup(keyboard)
        # Crea el mensaje con la cc y la información del bin
        message = f"<b>「 ⤳ 」CC</b>↛   <code>{linea}</code>\n"
        message += f"━━━━━━━━━━━━━━━━\n"
        message += f"<b>「 ⤳ 」Tipo</b>↛  <code>{brand}-{typea}-{level}</code>\n"
        message += f"<b>「 ⤳ 」Banco</b>↛  <code>{bank}</code>\n"
        message += f"<b>「 ⤳ 」Pais</b>↛  <code>{country_name} [{country_flag}]</code>\n"
        message += f"━━━━━━━━━━━━━━━━\n"
        message += f"<b>「 ⤳ 」New Extra</b>↛  <code>{card_number}xxxx|{month}|{year}|rnd</code>\n"
        message += f"「 ↳ 」<b>Scrapp By</b>↛  <code>@perkiras</code>\n"
        # Envía el mensaje al canal con parse_mode='HTML'
        await bot.send_message(chat_id, message, reply_markup=reply_markup, parse_mode='HTML')


        # Espera unos segundos antes de enviar el siguiente mensaje
        await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(send_messages())