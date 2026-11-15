# analyze_semantic_similarity

Сравнение постов Telegram-каналов по семантическому сходству (cosine / Jaccard, BM25, MiniLM).

## Установка

```bash
pip install -r requirements.txt
cp .env.example .env
```

Заполни `.env` (Telegram API и Hugging Face токен).

## Запуск

```bash
# парсинг канала → data/posts.db
python -m parsing.parsing_channel

# сравнение постов
python main.py

# MiniLM через HF API
python -m models.modelMiniLM
```

## Структура

```
├── main.py
├── parsing/      # Telethon, очистка текста
├── models/       # cosine/Jaccard, BM25, MiniLM
├── db/           # SQLite
├── analyze/      # теплокарта
├── data/         # БД, сессия, результаты
└── tests/
```
