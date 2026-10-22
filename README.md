# Telegram To-Do Bot

Telegram orqali vazifalarni boshqarish uchun Python bot.

## Imkoniyatlari
- Vazifa qo‘shish
- Vazifalar ro‘yxatini ko‘rish
- Vazifani bajarilgan deb belgilash
- Vazifani o‘chirish
- Vazifalarni JSON faylida saqlash

## O‘rnatish va ishga tushirish

1. Loyihani GitHub’dan yuklab oling.
2. Kerakli kutubxonani o‘rnating:

   ```bash
   pip install pyTelegramBotAPI
   ```

3. Telegram’da [@BotFather](https://t.me/BotFather) orqali bot yarating va token oling.
4. Loyiha papkasida `config.py` faylini yarating:

   ```python
   TOKEN = "BU_YERGA_TOKENINGIZ"
   ```

5. Botni ishga tushiring:

   ```bash
   python main.py
   ```

## Xavfsizlik

Haqiqiy bot tokenini GitHub’ga joylamang. `config.py` va `todo.json` `.gitignore` orqali Git kuzatuvidan chiqarilgan.
