import time
import asyncio  # Import asyncio for sleep
from pyrogram import Client, filters
from pyrogram.enums import ParseMode  # Import ParseMode for markdown

def setup_update_handler(app: Client):
    @app.on_message(filters.command("update"))
    async def handle_update_command(client, message):
        chat_id = message.chat.id

        # Initial message for the update animation
        update_message = await client.send_message(
            chat_id, 
            "🔄 Updating...Bro Our Dᴇꜱɪɢɴ Vᴀᴜʟᴛ 🔐 Bot\n\n[                    ] 0%"
        )

        # Progress bar animation steps
        progress_steps = [
            "[                    ] 0%",
            "[█                  ] 10%",
            "[███                ] 20%",
            "[█████              ] 40%",
            "[███████            ] 60%",
            "[█████████          ] 80%",
            "[███████████        ] 90%",
            "[████████████████] 100%"
        ]

        # Progress bar animation
        for step in progress_steps:
            try:
                await client.edit_message_text(
                    chat_id=chat_id,
                    message_id=update_message.id,
                    text=f"🔄 Updating...Bro Our Dᴇꜱɪɢɴ Vᴀᴜʟᴛ 🔐 Bot\n\n{step}"
                )
                await asyncio.sleep(0.25)  # Pause for animation timing (0.25 seconds per step)
            except Exception as e:
                print(f"Edit message failed: {e}")  # Debugging purposes

        # Delete the animation message after completion
        try:
            await client.delete_messages(chat_id, update_message.id)
        except Exception as e:
            print(f"Delete message failed: {e}")  # Debugging purposes

        # Notify the user that the update is complete
        await client.send_message(
            chat_id,
            "✅ *Bot Update Done Bro! Check Out New Features Now Through /start Command*",
            parse_mode=ParseMode.MARKDOWN  # Use ParseMode.MARKDOWN for Markdown formatting
        )
