import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

# /start ইমপোর্ট
from start import start_command

# আলাদা ফাইল থেকে সব কমান্ড ইমপোর্ট
from commands.myaccount import myaccount_command
from commands.signup import signup_command
from commands.login import login_command
from commands.email import email_command
from commands.passkey import passkey_command
from commands.username import username_command
from commands.date_birth import date_birth_command
from commands.gender import gender_command
from commands.call_coin import call_coin_command
from commands.profile_photo import profile_photo_command
from commands.banner_photo import banner_photo_command
from commands.short_1 import short_1_command
from commands.short_2 import short_2_command
from commands.short_3 import short_3_command
from commands.image_1 import image_1_command
from commands.image_2 import image_2_command
from commands.image_3 import image_3_command
from commands.withdraw import withdraw_command
from commands.recharge import recharge_command

# .env ফাইল থেকে টোকেন লোড করা
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN পাওয়া যায়নি! দয়া করে .env ফাইল চেক করুন।")

    app = Application.builder().token(TOKEN).build()

    # কমান্ড হ্যান্ডলার রেজিস্টার করা
    handlers = [
        ("start", start_command),
        ("myaccount", myaccount_command),
        ("signup", signup_command),
        ("login", login_command),
        ("email", email_command),
        ("passkey", passkey_command),
        ("username", username_command),
        ("date_birth", date_birth_command),
        ("gender", gender_command),
        ("call_coin", call_coin_command),
        ("profile_photo", profile_photo_command),
        ("banner_photo", banner_photo_command),
        ("short_1", short_1_command),
        ("short_2", short_2_command),
        ("short_3", short_3_command),
        ("image_1", image_1_command),
        ("image_2", image_2_command),
        ("image_3", image_3_command),
        ("withdraw", withdraw_command),
        ("recharge", recharge_command),
    ]

    for cmd_name, cmd_func in handlers:
        app.add_handler(CommandHandler(cmd_name, cmd_func))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
