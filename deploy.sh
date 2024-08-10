#!/bin/bash

# Loyihaning joylashgan papkasiga o'tish
cd /home/user/user-bot

# Virtual environment yaratish yoki yangilash
python3 -m venv venv

# Virtual environmentni faollashtirish
source venv/bin/activate

# Yangi paketlarni o'rnatish
pip install -r requirements.txt

# .conf faylini joylashtirish
sudo cp user_bot.conf /etc/supervisor/conf.d/user_bot.conf

# Supervisorctl konfiguratsiyasini yangilash
sudo supervisorctl reread
sudo supervisorctl update

# Dasturni qayta ishga tushirish
sudo supervisorctl stop user_bot
sudo supervisorctl start user_bot
