from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
from tg.renew import premium_users

# Define questions and answers
faqs = {
    "What is Design Vault?": "Design Vault 🔐 is a bot that provides a wide range of graphic resources and effortless downloads.",
    "How to use the bot?": "Simply navigate through the bot's menu and follow the instructions to explore resources.",
    "Is this bot free?": "Yes, the bot is free to use, but some resources may require joining certain channels.",
    "Who created this bot?": "This bot was created by @abirxdhackz. Check out updates on @abir_x_official.",
}

def setup_faq_handler(app: Client):
    async def show_questions_menu(chat_id, message_id=None):
        """Show the FAQ questions as buttons."""
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(question, callback_data=f"faq_{idx}")] for idx, question in enumerate(faqs.keys())]
        )

        if message_id:
            # Edit the message if message_id is provided
            await app.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="📖 Choose a question:",
                reply_markup=keyboard
            )
        else:
            # Send a new message otherwise
            await app.send_message(chat_id, "📖 Choose a question:", reply_markup=keyboard)

    @app.on_message(filters.command("faq"))
    async def faq_command(client, message):
        """Handler for the /faq command."""
        await show_questions_menu(message.chat.id)

    @app.on_callback_query(filters.regex("^faq_"))
    async def handle_faq_selection(client, callback_query):
        """Handle question selection."""
        callback_data = callback_query.data[4:]  # Extract callback data
        if callback_data.isdigit() and int(callback_data) < len(faqs):
            question = list(faqs.keys())[int(callback_data)]
            answer = faqs[question]

            # Send the answer with a back button
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔙 Back to Questions", callback_data="faq_menu")]]
            )

            # Correctly reference chat_id and message_id in Pyrogram callback query
            await client.edit_message_text(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.id,
                text=f"📖 **{question}**\n\n{answer}",
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN
            )
        elif callback_query.data == "faq_menu":
            await show_questions_menu(callback_query.message.chat.id, callback_query.message.id)
        else:
            await callback_query.answer("Invalid selection. Please try again.", show_alert=True)
