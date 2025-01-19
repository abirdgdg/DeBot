from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode  # Import ParseMode

def setup_privacy_handler(app: Client):
    @app.on_message(filters.command("privacy"))
    async def send_privacy_policy(client, message):
        privacy_message = (
            "<b>Privacy Policy for Design Vault Bot</b>\n"
            "━━━━━━━━━━━━━━━━━\n\n"
            "Welcome to Design Vault Bot! We offer access to premium graphics services, such as Envato, Freepik, Motion Array, Unsplash, and more. "
            "By using this bot, you agree to the terms and conditions of this privacy policy.\n\n"
            
            "<b>Information We Collect</b>\n\n"
            "1. <u>Personal Information:</u>\n"
            "   - <i>User ID and Username:</i> We collect your User ID and username to provide personalized services and improve your experience.\n\n"
            
            "2. <u>Usage Data:</u>\n"
            "   - Data on the commands you use, the files you access, and the frequency of use to optimize our services and enhance functionality.\n\n"
            
            "<b>How We Use Your Information</b>\n\n"
            "   - <u>Service Provision:</u> To provide and enhance the graphics and design-related services offered by the bot, such as downloading assets, images, and videos.\n"
            "   - <u>Communication:</u> To notify you about new features, updates, and important information regarding the bot.\n"
            "   - <u>Security:</u> To monitor for unauthorized access and protect against potential threats and spam.\n"
            "   - <u>Promotions and Advertisements:</u> We may display promotional messages related to the bot or its services.\n\n"
            
            "<b>Data Security</b>\n\n"
            "   - We implement strong security measures to protect your data, ensuring it remains private and secure at all times.\n"
            "   - Your personal information will not be shared with any third parties without your consent, except as required by law.\n\n"
            
            "<b>Graphics Services We Provide</b>\n"
            "━━━━━━━━━━━━━━━━━\n\n"
            "1. <u>Envato Files:</u> 🌐\n"
            "   - Access and download premium design files, templates, and assets from Envato.\n\n"
            
            "2. <u>Motion Array Files:</u> 🎬\n"
            "   - Download video templates, stock footage, sound effects, and music from Motion Array.\n\n"
            
            "3. <u>Freepik Files:</u> 🖼\n"
            "   - Access Freepik’s vast collection of vectors, illustrations, and stock images for personal or commercial use.\n\n"
            
            "4. <u>Unsplash Images:</u> 📸\n"
            "   - Get high-resolution, royalty-free photos from Unsplash for your creative projects.\n\n"
            
            "5. <u>And More:</u> 💡\n"
            "   - We continuously add new services to help you with your creative needs.\n\n"
            
            "<b>Your Rights</b>\n\n"
            "   - You have the right to request access to your personal data, ask for it to be deleted, or opt out of receiving promotional messages.\n\n"
            
            "Thank you for using Design Vault Bot! We are committed to ensuring your privacy and offering you the best experience possible.\n\n"
            
            "<b>If you have any questions or concerns, feel free to contact us.</b>\n"
            "━━━━━━━━━━━━━━━━━\n\n"
            "For more information about our services, visit our website or contact support.\n"
        )

        # Adding a button to return to the main menu
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Main Menu", callback_data="main_menu")]
            ]
        )

        # Use ParseMode.HTML instead of "html"
        await app.send_message(message.chat.id, privacy_message, parse_mode=ParseMode.HTML, reply_markup=keyboard)
