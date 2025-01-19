from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode  # Import ParseMode for Markdown or HTML

ADMIN_USERNAME = "abirxdhackz"  # Replace with your admin username

def setup_plan_handler(app: Client):
    @app.on_message(filters.command("plans"))
    async def handle_plan_command(client, message):
        chat_id = message.chat.id

        # Plan descriptions with improved formatting
        plans_text = (
            "**Plan 1**\n\n"
            "• **Envato Download**\n"
            "• Validity: **1 Month**\n"
            "• Mass Content Downloader (Max: **200**)\n"
            "• 24 Hours Support ❌\n"
            "• Premium Support by Chat ✅\n"
            "• Private Chat Supported ✅\n\n"
            "**Plan 2**\n\n"
            "• **Envato, Freepik, Motion Array**\n"
            "• Validity: **1 Month**\n"
            "• Mass Content Downloader (Max: **150**)\n"
            "• First Content Download ✅\n"
            "• Premium Support by Chat ✅\n"
            "• Private Chat Supported ✅\n"
            "• Unsplash Supported ❌\n\n"
            "**Plan 3**\n\n"
            "• **All Services Available**\n"
            "• Validity: **2 Months**\n"
            "• Mass Content **Unlimited**\n"
            "• Premium Support: 24 Hours via Chat ✅\n"
            "• Midnight Professor Support ✅\n"
            "• Private Inbox Support ✅\n"
            "• And Many More!\n"
        )

        # Inline buttons for purchasing plans
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Buy Plan 1", url=f"https://t.me/{ADMIN_USERNAME}?start=plan1")],
                [InlineKeyboardButton("Buy Plan 2", url=f"https://t.me/{ADMIN_USERNAME}?start=plan2")],
                [InlineKeyboardButton("Buy Plan 3", url=f"https://t.me/{ADMIN_USERNAME}?start=plan3")]
            ]
        )

        # Send the message with plan details and the inline buttons
        await client.send_message(
            chat_id,
            plans_text,
            parse_mode=ParseMode.MARKDOWN,  # Use Markdown for text formatting
            reply_markup=keyboard
        )
