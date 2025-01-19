from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode  # Import ParseMode for HTML

def setup_help_handler(app: Client):
    @app.on_message(filters.command("help"))
    async def send_help(client, message):
        help_message = (
            "<b>Help - List of Commands</b>\n"
            "━━━━━━━━━━━━━━━━━\n\n"
            "Welcome to the Design Vault Bot! Here are the available commands:\n\n"
            "<b>Basic User Commands:</b>\n"
            "1. /env1 - Download Envato Elements files 🌐\n"
            "2. /mot - Get Motion Array files 🎬\n"
            "3. /pik1 - Download Freepik files 🖼\n"
            "4. /uns - Get Unsplash images 📸\n"
            "5. /start - Start the bot 🚀\n"
            "6. /privacy - View privacy settings 🔒\n"
            "7. /plans - Check subscription plans 💼\n"
            "8. /help - List of available commands ❓\n"
            "9. /feedback - Send feedback or report an issue 💬\n"
            "10. /update - Check for new updates or features 🔄\n"
            "11. /support - Contact support or join the support group 🆘\n"
            "12. /info - Information about the bot and its capabilities ℹ️\n"
            "13. /faq - Frequently asked questions and answers 📑\n"
            "14. /status - Check the bot's operational status 📊\n"
            "15. /renew - Renew your subscription or check status 🔁\n"
            "16. /history - View your download or command history 📜\n\n"
            "Thank you for using the Design Vault Bot! We are here to make your graphics resource downloading easier and faster. 💼"
        )

        # Adding a button to return to the main menu
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Main Menu", callback_data="main_menu")]
            ]
        )

        # Send the message with the help information and the inline button
        await client.send_message(
            message.chat.id,
            help_message,
            parse_mode=ParseMode.HTML,  # Use ParseMode.HTML
            reply_markup=keyboard
        )

