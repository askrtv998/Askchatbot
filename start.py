from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """🤖 **Bot Commands List**

⚙️ **Settings:**
1️⃣ /myaccount - Check Your Account Status
2️⃣ /signup - Create Your Account
3️⃣ /login - Login on Server to Access Use App

🛡️ **Security:**
4️⃣ /email - Check Your email, Change Email
5️⃣ /passkey - Get Your Passkey, Change Passkey

👤 **Personal Details:**
6️⃣ /username - Get Username, Change Username
7️⃣ /date_birth - Check Birth Year, Change Birth Year
8️⃣ /gender - Check Gender Status, Change Gender Status
9️⃣ /call_coin - Get Call Rate per Minute, Change Call Rate

🖼️ **Avatar:**
🔟 /profile_photo - Get Profile Photo, Change Profile Photo
1️⃣1️⃣ /banner_photo - Get Banner Photo, Change Banner Photo

⚡ **Social Shorts:**
1️⃣2️⃣ /short_1 - Get Short_1, Change Short_1
1️⃣3️⃣ /short_2 - Get Short_2, Change Short_2
1️⃣4️⃣ /short_3 - Get Short_3, Change Short_3

🖼️ **Social Images:**
1️⃣5️⃣ /image_1 - Get Image_1, Change Image_1
1️⃣6️⃣ /image_2 - Get Image_2, Change Image_2
1️⃣7️⃣ /image_3 - Get Image_3, Change Image_3

🌐 **Helper Website:**
1️⃣8️⃣ /withdraw - Go to Withdraw Website
1️⃣9️⃣ /recharge - Go to Recharge Website"""

    await update.message.reply_text(message, parse_mode="Markdown")
