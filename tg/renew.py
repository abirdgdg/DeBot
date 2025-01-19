from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode  # Import ParseMode for Markdown

# List to store premium user IDs
premium_users = [7303810912]

def setup_renew_handler(app: Client):
    @app.on_message(filters.command("renew"))
    async def handle_renew_command(client, message):
        chat_id = message.chat.id

        if chat_id not in premium_users:
            # Message for non-premium users
            response_text = (
                "❌ Sorry Bro! You Are Not On A Premium Member Or In A Premium Plan.\n"
                "Buy Your Desired Plans From [Abir XD](https://t.me/abirxdhackz)."
            )

            # Buttons for "Use Free" and "Order Plan"
            keyboard = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("✨ Use Free ✨", url="https://t.me/abir_x_official_graphics_hub")],
                    [InlineKeyboardButton("🛒 Order Plan 🛒", url="https://t.me/abirxdhackz")]
                ]
            )

            await client.send_message(
                chat_id,
                response_text,
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN,  # Use ParseMode.MARKDOWN
            )
        else:
            # Message for premium users (renewal placeholder)
            await client.send_message(
                chat_id,
                "✅ You Are Already A Premium Member!"
            )

    @app.on_message(filters.command("approve"))
    async def handle_approve_command(client, message):
        # Check if the user is the owner of the bot
        owner_id = 7303810912  # Replace with the bot owner's user ID
        if message.chat.id != owner_id:
            await message.reply("❌ You don't have permission to use this command.")
            return

        # Parse the user ID from the message
        try:
            user_id_to_approve = int(message.text.split()[1])
        except (IndexError, ValueError):
            await message.reply("❌ Please provide a valid user ID. Example: /approve 987654321")
            return

        # Add user to premium list
        if user_id_to_approve not in premium_users:
            premium_users.append(user_id_to_approve)
            try:
                await client.send_message(
                    user_id_to_approve,
                    "🎉 Bro, You're Now A Premium Member!"
                )
                await message.reply(f"✅ User {user_id_to_approve} has been approved as a premium member.")
            except Exception as e:
                await message.reply(f"⚠️ Could not send a message to user {user_id_to_approve}. Error: {e}")
        else:
            await message.reply(f"⚠️ User {user_id_to_approve} is already a premium member.")
