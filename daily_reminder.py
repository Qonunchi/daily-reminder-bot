import schedule
import time
import telegram

# Бот токени ва фойдаланувчи ID'sи
BOT_TOKEN = "7881051968:AAHFooid3PR5ugWnC5W_KNevRrO-WCCt_iI"
CHAT_ID = 113772884

# Бот объектни яратамиз
bot = telegram.Bot(token=BOT_TOKEN)

# Юбориладиган хабар
def send_reminder():
    message = "Салом, Беҳзод! ⏰ Кун якуни суҳбатимиз вақти келди. Бугунги таассуротлар, фикрлар ва режалар ҳақида гаплашамизми?"
    bot.send_message(chat_id=CHAT_ID, text=message)

# Жадвалга қўшамиз
schedule.every().day.at("21:00").do(send_reminder)

print("⏳ Скрипт ишлаяпти. Ҳар куни соат 21:00 да хабар юборилади.")

# Доимий равишда ишлаш учун цикл
while True:
    schedule.run_pending()
    time.sleep(60)
