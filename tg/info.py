from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode  # Import ParseMode for HTML

def setup_info_handler(app: Client):
    @app.on_message(filters.command("info"))
    async def send_info(client, message):
        info_message = (
            "<b>Information about the Bot</b>\n"
            "━━━━━━━━━━━━━━━━━\n\n"
            "Welcome to the Design Vault Bot! Here are the features and commands available:\n\n"
            "<b>Features:</b>\n"
            "1. Download Envato Elements files 🌐\n"
            "2. Get Motion Array files 🎬\n"
            "3. Download Freepik files 🖼\n"
            "4. Get Unsplash images 📸\n"
            "5. Start the bot 🚀\n"
            "6. View privacy settings 🔒\n"
            "7. Check subscription plans 💼\n"
            "8. List of available commands ❓\n"
            "9. Send feedback or report an issue 💬\n"
            "10. Check for new updates or features 🔄\n"
            "11. Contact support or join the support group 🆘\n"
            "12. Information about the bot and its capabilities ℹ️\n"
            "13. Frequently asked questions and answers 📑\n"
            "14. Check the bot's operational status 📊\n"
            "15. Renew your subscription or check status 🔁\n"
            "16. View your download or command history 📜\n\n"
            "Thank you for using the Design Vault Bot! We are here to make your graphics resource downloading easier and faster. 💼"
        )

        # Adding a button to return to the main menu
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Main Menu", callback_data="main_menu")]
            ]
        )

        # Send the message with information and the inline button
        await client.send_message(
            message.chat.id,
            info_message,
            parse_mode=ParseMode.HTML,  # Use ParseMode.HTML
            reply_markup=keyboard
        )
