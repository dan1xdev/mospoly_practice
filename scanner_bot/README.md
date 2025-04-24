# 🧠 Telegram OCR Бот: Руководство по созданию сканера текста с фото

## 📚 Содержание
1. [Обзор и исследование предметной области](#обзор)
2. [Требования](#требования)
3. [Установка и настройка окружения](#установка)
4. [Создание Telegram-бота](#создание-бота)
5. [Интеграция Tesseract OCR](#интеграция-ocr)
6. [Разработка функциональности бота](#разработка)
7. [Иллюстрации и схемы](#иллюстрации)
8. [Размещение в GitHub](#размещение)
9. [Заключение](#заключение)

---

## 🧪 Обзор и исследование предметной области <a name="обзор"></a>

**Цель**: создать Telegram-бота, который принимает изображения и распознает текст, возвращая результат пользователю. Используемая технология — OCR (оптическое распознавание символов).

**Исследуемые компоненты**:
- **Telegram API** — взаимодействие с пользователями.
- **Aiogram** — асинхронный фреймворк для написания Telegram-ботов.
- **Tesseract OCR** — популярный open-source движок для распознавания текста.
- **Pillow (PIL)** — работа с изображениями.
- **Python** — основной язык реализации.

---

## 🛠️ Требования <a name="требования"></a>

- Python 3.9+
- pip (пакетный менеджер Python)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Библиотеки:
  ```bash
  pip install aiogram pillow pytesseract
  ```

---

## ⚙️ Установка и настройка окружения <a name="установка"></a>

1. Установите Python и pip.
2. Установите Tesseract:
   - Windows: загрузите с [официального сайта](https://github.com/tesseract-ocr/tesseract).
   - Укажите путь в коде:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
     ```
3. Установите Python-зависимости:
   ```bash
   pip install aiogram pillow pytesseract
   ```

---

## 🤖 Создание Telegram-бота <a name="создание-бота"></a>

1. Перейдите в [BotFather](https://t.me/BotFather) в Telegram.
2. Введите команду `/newbot`, задайте имя и получите API-токен.
3. Вставьте токен в переменную `API_TOKEN`.

---

## 🧩 Интеграция Tesseract OCR <a name="интеграция-ocr"></a>

```python
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(Image.open("example.jpg"), lang="eng")
```

---

## 👨‍💻 Разработка функциональности бота <a name="разработка"></a>

### 1. Инициализация

```python
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
```

### 2. Команда /start

```python
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    ...
```

### 3. Изменение языка OCR

```python
@dp.message(Command("lang"))
async def change_language(message: types.Message):
    ...
```

### 4. Обработка изображения и распознавание

```python
@dp.message(lambda msg: msg.photo)
async def handle_photo(message: types.Message):
    ...
```

---

## 🖼️ Иллюстрации и схемы <a name="иллюстрации"></a>

### Пример входного изображения

![input-example](https://github.com/user-attachments/assets/e07e7f3b-49be-4340-88b4-7f99e6f25623)


---

### Пример выхода

![output-example](https://github.com/user-attachments/assets/4c34103f-6987-4ab1-80fa-6423a049133a)


---

### Схема взаимодействия
![architecture](https://github.com/user-attachments/assets/f7bb2313-99a2-4f5e-b29a-d6605acd26be)

---

### Команды пользователя

| Команда        | Описание                      |
|----------------|-------------------------------|
| /start         | Приветствие и инструкция      |
| /lang eng/rus | Сменить язык распознавания   |

---

### Структура проекта

```
scanner_bot/
│
├── main.py
├── requirements.txt
└── README.md
```

---


