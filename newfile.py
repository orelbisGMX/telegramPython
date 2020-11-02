from pyrogram import Client
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

#922109298


# Create a client using your bot token
app = Client(
    "my_bot", 
    bot_token="1373563559:AAH2KtK2CRADOX7OMQgdNgC5qcAJFN0k318",
    # phone_number='+5356436434',
    api_id='1930134',
    api_hash='a988c8aa7eb216f02ce593afe392e777'
    )
with app:
    app.send_message(
        922109298,  # Edit this
        "hi"
    )

@app.on_message()
def answer4(client, message):
    if(message.text == 'llamar' and message.chat.id == -1001486914721):
        miembros = ''
        for member in app.iter_chat_members(-1001486914721):
            if(member.user.is_bot == False):
                print(member)
                miembros = miembros + ' @' + member.user.username
        message.reply_text(miembros)
    # if(message.text == 'telefonos' and message.chat.id == -1001486914721):
    #     miembros = ''
    #     for member in app.iter_chat_members(-1001486914721):
    #         if(member.user.is_bot == False):
    #             miembros = miembros + ' ' + member.user.phone_number
    #     message.reply_text(miembros)

# @app.on_raw_update()
# def answer(client, aa):
#     print('entro en raw_update')
#     print(aa)
app.run()
