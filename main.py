from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.enums import ParseMode
import time
import asyncio
from tg.privacy import setup_privacy_handler
from tg.info import setup_info_handler
from tg.status import setup_status_handler
from tg.help import setup_help_handler
from tg.support import setup_support_handler
from tg.faq import setup_faq_handler
from tg.update import setup_update_handler
from tg.plan import setup_plan_handler
from tg.renew import setup_renew_handler
from tg.downloaders import setup_download_handlers

# Replace with your bot token and API credentials
BOT_TOKEN = "7814177897:AAH_qvMC5Juny0rxhZILsgU_HxsuQS-eksM"
API_ID = 24602058  # Replace with your API_ID from https://my.telegram.org
API_HASH = "b976a44ccb8962b20113113f84aeebf6"

app = Client("my_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Set the start time when the bot starts
app.start_time = time.time()

# Dictionary to store total users
total_users = {}

# Function to increment user count
def increment_user_count(chat_id):
    total_users[chat_id] = True  # Add user to the dictionary

# Register handlers for Pyrogram
def register_handlers(client):
    setup_privacy_handler(client)
    setup_info_handler(client)
    setup_help_handler(client)
    setup_support_handler(client)
    setup_faq_handler(client)
    setup_update_handler(client)
    setup_plan_handler(client)
    setup_renew_handler(client)
    setup_download_handlers(client)
    setup_status_handler(client, total_users)  # Pass total_users here

# Properly call the registration function
register_handlers(app)

# Helper function to create the main menu
def create_main_menu():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Envato Elements", callback_data="envato"),
                InlineKeyboardButton("Motion Array", callback_data="motion")
            ],
            [
                InlineKeyboardButton("Freepik", callback_data="freepik"),
                InlineKeyboardButton("Unsplash", callback_data="unsplash")
            ],
            [
                InlineKeyboardButton("Free Access", callback_data="freeaccess"),
                InlineKeyboardButton("Paid Access", callback_data="paidaccess")
            ],
            [
                InlineKeyboardButton("For Reseller", callback_data="reseller"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
    )


@app.on_message(filters.command("start"))
async def send_start_message(client, message):
    chat_id = message.chat.id

    # Increment user count
    increment_user_count(chat_id)

    # Verify that user count is being incremented
    print(f"User {chat_id} added to total_users.")

    # Simulate typing animation with short delays and delete the messages afterward
    anim1 = await message.reply_text("<b>Starting Design Vault...</b>", parse_mode=ParseMode.HTML)
    await asyncio.sleep(0.3)
    await anim1.delete()

    anim2 = await message.reply_text("<b>Preparing Your Experience, Please Wait...</b>", parse_mode=ParseMode.HTML)
    await asyncio.sleep(0.3)
    await anim2.delete()

    start_message = (
        f"Hi — ⟨{message.from_user.first_name}⟩ Welcome to this bot\n"
        "________________________________\n\n"
        "<b><a href='https://t.me/DesVaultBot'>Dᴇꜱɪɢɴ Vᴀᴜʟᴛ 🔐</a></b>: "
        "Dᴇꜱɪɢɴ Vᴀᴜʟᴛ 🔐 is the most complete Bot to help you with Graphics Resources, "
        "Effortless Downloads 🔥\n\n"
        "Don't forget to <a href='https://t.me/abir_x_official'>join</a> for updates!"
    )

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Explore Dᴇꜱɪɢɴ Vᴀᴜʟᴛ 🔐", callback_data="main_menu")]]
    )

    await message.reply_text(
        start_message,
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )


@app.on_callback_query()
async def handle_callback_query(client, query: CallbackQuery):
    data = query.data  # Extract the callback data
    responses = {
        "envato": (
            "Dᴇꜱɪɢɴ Vᴀᴜʟᴛ 🔐 🌟Quick Guide to Access Envato\n"
            "━━━━━━━━━━━━━━━━\n"
            "1: 🔗 Downloading Envato Elements File\n"
            "   - Type /env1 followed by an Envato URL.\n"
            "   - Example: /env1 https://elements.envato.com/crystal-logo\n\n"
            "2: 👑 Pro Features\n"
            "   - Plans Daily/Weekly/Monthly\n"
            "   - Unlimited Download Limit\n"
            "   - Download Files with license key\n"
            "   - 24x7 Downloading Service with No Downtime\n\n"
            "3: 👑 Buy Subscription\n"
            "   - To Buy Envato subscription Contact to <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>",
            {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
        ),
        "freepik": (
            "Dᴇꜱɪɢɴ Vᴀᴜʟᴛ 🔐 🌟 Quick Guide to Access Freepik\n"
            "━━━━━━━━━━━━━━━━\n"
            "1: 🔗 Downloading Freepik File\n"
            "   - Type /pik1 followed by a Freepik URL.\n"
            "   - Example: /pik1 https://www.freepik.com/premium-photo/sunny-forest.htm\n\n"
            "2: 👑 Pro Features\n"
            "   - Plans Daily/Weekly/Monthly\n"
            "   - Custom download Limit.\n"
            "   - 24x7 Downloading Service with No Downtime\n\n"
            "3: 👑 Buy Subscription\n"
            "   - To Buy Freepik subscription Contact to <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>",
            {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
        ),
        "unsplash": (
            "Dᴇꜱɪɢɴ Vᴀᴜʟᴛ 🔐 🌟 Quick Guide to Access Unsplash+\n"
            "━━━━━━━━━━━━━━━━\n"
            "1: 🔗 Downloading Unsplash File\n"
            "   - Type /uns followed by an Unsplash URL.\n"
            "   - Example: /uns https://unsplash.com/photos/a-baby\n\n"
            "2: 👑 Pro Features\n"
            "   - Plans Daily/Weekly/Monthly\n"
            "   - 100 downloads per day.\n"
            "   - 24x7 Downloading Service with No Downtime\n\n"
            "3: 👑 Buy Subscription\n"
            "   - To Buy Unsplash subscription Contact to <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>",
            {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
        ),
        "motion": (
            "Dᴇꜱɪɢɴ Vᴀᴜʟᴛ 🔐 🌟 Quick Guide to Access Motionarray\n"
            "━━━━━━━━━━━━━━━━\n"
            "1: 🔗 Downloading Motionarray File\n"
            "   - Type /mot followed by a Motionarray URL.\n"
            "   - Example: /mot https://motionarray.com/example\n\n"
            "2: 👑 Pro Features\n"
            "   - Plans Daily/Weekly/Monthly\n"
            "   - 100 downloads per day.\n"
            "   - 24x7 Downloading Service with No Downtime\n\n"
            "3: 👑 Buy Subscription\n"
            "   - To Buy MotionArray subscription Contact to <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>",
            {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
        ),
        "paidaccess": (
            "Dᴇꜱɪɢɴ Vᴀᴜʟᴛ 🔐 Paid Access\n"
            "━━━━━━━━━━━━━━━━\n"
            "1: 🔗 Buy Subscription\n"
            "   - Contact <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>\n\n"
            "2: 👑 Paid Features\n"
            "   - Fast Download Services\n"
            "   - Cheap Price\n"
            "   - Daily/Weekly/Monthly plan\n\n"
            "3: ✅ Daily Limits\n"
            "   - Envato: Unlimited\n"
            "   - Freepik: Custom\n"
            "   - Unsplash: 100\n"
            "━━━━━━━━━━━━━━━━\n"
            "   - To Buy PaidAccess subscription Contact <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>",
            {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
        ),
        "freeaccess": (
            "🌟 Dᴇꜱɪɢɴ Vᴀᴜʟᴛ 🔐 Free Access\n"
            "━━━━━━━━━━━━━━━━\n"
            "1: 🔗 To Get Free Access\n"
            "   - Join this Group: Graphics - Hub🌟 (<a href='https://t.me/abir_x_official_graphics_hub'>Graphics - Hub</a>)\n\n"
            "2: 👑 Free Features\n"
            "   - Lifetime Plan\n"
            "   - Fast Download Services\n\n"
            "3: ✅ Daily Limits\n"
            "   - Envato: 1\n"
            "   - Freepik: 1\n"
            "   - Unsplash+: 1\n"
            "━━━━━━━━━━━━━━━━\n"
            "All Commands Explanation: <a href='https://t.me/abir_x_official_graphics_hub'>Join Now</a>",
            {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
        ),
        "reseller": (
            "Dᴇꜱɪɢɴ Vᴀᴜʟᴛ 🔐 🌟 Instructions for Resellers to Sell Bot Subscriptions\n"
            "━━━━━━━━━━━━━━━━\n"
            "Step 1: Contact the Bot Owner\n"
            "   - Telegram Username: <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>\n\n"
            "Step 2: Take Reseller Subscription\n"
            "   - Reach out to Bot Owner to obtain reseller information.\n"
            "   - Discuss pricing and payment details directly with Bot Owner.\n\n"
            "Step 3: Acquire User IDs\n"
            "   - Collect the Telegram user IDs of customers interested in purchasing the bot subscription.\n\n"
            "Step 4: Send User IDs for Activation\n"
            "   - Send the collected user IDs to Bot Owner for activation.\n"
            "   - Activation will be processed promptly upon receiving the user IDs.\n\n"
            "Step 5: Confirm Activation\n"
            "   - Once the subscriptions are activated, Bot Owner will notify you.\n"
            "   - Inform your customers that their subscriptions are now active.\n\n"
            "Step 6: Process Payment\n"
            "   - After confirming the subscription activation, make the payment to Bot Owner for the subscriptions.\n\n"
            "Ensure timely payments to maintain a smooth reselling process and good standing.",
            {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
        ),
    }

    if data in responses:
        response_text, options = responses[data]
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Back", callback_data="main_menu")]]
        )

        await query.message.edit_text(
            response_text,
            reply_markup=back_button,
            **options,
        )
    elif data == "main_menu":
        await query.message.edit_text(
            "Here are the Dᴇꜱɪɢɴ Vᴀᴜʟᴛ 🔐 Options:",
            reply_markup=create_main_menu(),
        )
    elif data == "close":
        await query.message.delete()

if __name__ == "__main__":
    print("Bot is running...")
    app.run()
