from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode  # Import ParseMode for Markdown support

def setup_support_handler(app: Client):
    @app.on_message(filters.command("support"))
    async def send_support_info(client, message):
        chat_id = message.chat.id

        # Message body with the support group info
        support_message = (
            "🤖 **Support Information**\n\n"
            "Please join our support group for assistance: \n"
            "👉 [@abir_x_official_chat](https://t.me/abir_x_official_chat)\n\n"
            "To help us understand your issue better, please describe it with emojis and in a polite manner. We'll be happy to assist you!\n\n"
            "🔴 If you have a critical issue or need to contact the owner, please use the /feedback command."
        )

        # Inline button to join the support group
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Join Support Group", url="https://t.me/abir_x_official_chat")]]
        )

        # Send the message with the support group and the button, using Markdown properly
        await client.send_message(  # Use client, not app
            chat_id,
            support_message,
            parse_mode=ParseMode.MARKDOWN,  # Use ParseMode.MARKDOWN
            reply_markup=keyboard,
            disable_web_page_preview=True  # Prevent preview for URLs
        )
