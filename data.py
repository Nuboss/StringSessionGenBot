from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton(" Start Generating Session ", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text=" Home ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("ᴀxᴇᴏɴ", url="https://t.me/Nustring_bot")],
        [
            InlineKeyboardButton("How to Use", callback_data="help"),
            InlineKeyboardButton(" About ", callback_data="about")
        ],
        [InlineKeyboardButton("Support", url="https://t.me/ALONE_MUSIC_ADD_ICT")],
    ]

    START = """
Hey {}

Welcome to {}

✪ I'm an String Session Bot [🔥](https://telegra.ph/file/f9fc0e44d5b94cbddc6f6.jpg) 

You can use me to generate pyrogram (even version 2) and telethon string session. Use below buttons to learn more !

By @gobloklahnomer

    """

    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @StarkBots

Music bot : [ϟ ᴀŔᴏN](https://t.me/IndoPlayer_bot)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @gobloklahnomer
    """
