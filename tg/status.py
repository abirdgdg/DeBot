import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode

def setup_status_handler(client: Client, total_users: dict):
    @client.on_message(filters.command("status"))
    async def send_status(client, message):
        chat_id = message.chat.id

        # Calculate uptime
        uptime_seconds = int(time.time() - client.start_time)
        uptime_days = uptime_seconds // (24 * 3600)
        uptime_hours = (uptime_seconds % (24 * 3600)) // 3600
        uptime_minutes = (uptime_seconds % 3600) // 60
        uptime_seconds %= 60
        uptime = f"{uptime_days}d {uptime_hours}h {uptime_minutes}m {uptime_seconds}s"

        # Total users count
        total_users_count = len(total_users)

        status_message = (
            "━━━━━━━━━━━━━━━━━\n"
            "📊 **Bot Live Statistics** 📊\n"
            "━━━━━━━━━━━━━━━━━\n\n"
            f"**💡 Total Users:** {total_users_count}\n"
            f"**✅ Uptime:** {uptime}\n"
            f"**📛 Version:** 10.10.1\n"
            f"**🟢 Last Update:** 9 Dec, 2024"
        )

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
        ])

        try:
            await client.send_message(chat_id, status_message, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        except Exception as e:
            print(f"Failed to send status message: {e}")
