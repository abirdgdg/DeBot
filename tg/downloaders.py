import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
import random
from tg.renew import premium_users

# Global dictionary to store user download limits
user_download_limits = {}

# Constants
MAX_DOWNLOADS = 4  # Daily limit for free users
ALLOWED_GROUP_ID = -1002161947125  # Group ID where commands can be used

def setup_download_handlers(app: Client):
    @app.on_message(filters.command(['env1', 'mot', 'pik1', 'uns']))
    async def handle_download_commands(client, message):
        chat_id = message.chat.id
        user_id = message.from_user.id
        full_name = message.from_user.first_name + (f" {message.from_user.last_name}" if message.from_user.last_name else "")
        profile_link = f"https://t.me/{message.from_user.username}" if message.from_user.username else "User Profile"
        command = message.text.split()[0][1:]  # Extract the command name without "/"
        given_url = message.text.split()[1:]  # Extract URL provided after the command

        # Map commands to services and validation rules
        service_data = {
            "env1": {"name": "Envato", "url_prefix": "https://elements.envato.com/"},
            "mot": {"name": "Motion Array", "url_prefix": "https://motionarray.com/"},
            "pik1": {"name": "Freepik", "url_prefix": "https://www.freepik.com/"},
            "uns": {"name": "Unsplash", "url_prefix": "https://unsplash.com/"},
        }
        service_info = service_data.get(command)

        if not service_info:
            await message.reply("❌ Unknown command. Please use a valid one.")
            return

        # Check if the command is used in the correct group or private chat
        if chat_id > 0:  # Private Chat
            if user_id not in premium_users:
                response_text = (
                    "❌ You're Not A Premium Member To Use Me In Private.\n"
                    "For Free, Use Me In [Abir X Official Graphics Hub](https://t.me/abir_x_official_graphics_hub)."
                )
                await client.send_message(chat_id, response_text, parse_mode=ParseMode.MARKDOWN)
                return
        elif chat_id != ALLOWED_GROUP_ID:
            await message.reply("❌ This command is not allowed here.")
            return

        # Ensure a URL is provided
        if not given_url:
            await message.reply("❌ Please provide a valid URL after the command.")
            return

        user_url = given_url[0]

        # Validate the URL
        if not user_url.startswith(service_info["url_prefix"]):
            await message.reply(f"❌ Please provide a valid URL starting with {service_info['url_prefix']}.")
            return

        # Initialize user download limits
        user_download_limits.setdefault(user_id, {}).setdefault(command, 0)

        # Check and handle download limits
        if user_id in premium_users or user_download_limits[user_id][command] < MAX_DOWNLOADS:
            processing_message = await client.send_message(chat_id, "⏳ Processing Your Request... Please Wait Patiently.")
            
            # Use asyncio.sleep to wait before deleting the message
            await asyncio.sleep(2)
            await processing_message.delete()

            # Generate a random license ID
            license_id = f"LIC-{random.randint(100000, 999999)}"

            # Update download count for free users
            if user_id not in premium_users:
                user_download_limits[user_id][command] += 1

            remaining_downloads = MAX_DOWNLOADS - user_download_limits[user_id][command]
            user_type = "Premium" if user_id in premium_users else "Free"

            # Format the response message
            response_text = (
                f"{service_info['name']} - Download Link ✅\n"
                "━━━━━━━━━━━━━━━━\n"
                f"**File Link:** [Click Here]({user_url})\n"
                f"**Download Link:** [Click Here]({user_url})\n"
                f"**License:** `{license_id}`\n"
                f"**User Type:** {user_type}\n"
                f"**Remaining:** {remaining_downloads} downloads\n"
                f"**Download By:** [{full_name}]({profile_link})\n"
                "━━━━━━━━━━━━━━━━\n"
                f"{service_info['name']} Downloader By: [Design Vault](https://t.me/DesVaultBot)"
            )

            # Inline buttons
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("📂 Download File", url=user_url)],
                [InlineKeyboardButton("🛒 Buy Plan", url="https://t.me/abirxdhackz")]
            ])

            # Send the message with the link preview disabled
            await client.send_message(chat_id, response_text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        else:
            # Notify user about reaching their limit
            await message.reply(
                "❌ Sorry Bro, You Reached Your Limit. For Premium, Knock [Abir XD](https://t.me/abirxdhackz).",
                parse_mode=ParseMode.MARKDOWN
            )
