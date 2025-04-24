import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

API_TOKEN = ("7590491235:AAHmGbiv1dN2GZ86UR6l-UhjrQ01QJe7pOM")
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

user_languages = {}

# /start
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    user_languages[message.from_user.id] = "eng"
    await message.answer(
        "Привет! Отправь мне фото с текстом — и я распознаю его 🧠\n\n"
        "Язык по умолчанию: English 🇬🇧\n"
        "Чтобы поменять язык: /lang eng или /lang rus"
    )

# /lang <код_языка>
@dp.message(Command("lang"))
async def change_language(message: types.Message):
    args = message.text.split()
    if len(args) == 2 and args[1] in ["eng", "rus"]:
        user_languages[message.from_user.id] = args[1]
        lang_name = "Английский 🇬🇧" if args[1] == "eng" else "Русский 🇷🇺"
        await message.answer(f"🔄 Язык OCR установлен: {lang_name}")
    else:
        await message.answer("⚠️ Используй формат: /lang eng или /lang rus")

# Обработка фото
@dp.message(lambda msg: msg.photo)
async def handle_photo(message: types.Message):
    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)
    downloaded = await bot.download_file(file.file_path)

    file_path = "temp.jpg"
    with open(file_path, "wb") as f:
        f.write(downloaded.read())

    lang = user_languages.get(message.from_user.id, "eng")

    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image, lang=lang)
    except Exception as e:
        await message.answer(f"❌ Ошибка при распознавании: {e}")
        return
    finally:
        os.remove(file_path)

    if text.strip():
        await message.answer(f"📝 Распознанный текст:\n\n{text}")
    else:
        await message.answer("😕 Не удалось распознать текст.")

# Запуск
if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
