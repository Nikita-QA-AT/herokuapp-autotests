# herokuapp-autotests

Автотесты на **Python + Selenium + Pytest**  
для тренажёрного сайта: [the-internet.herokuapp.com](https://the-internet.herokuapp.com)

---

## 📦 Стек технологий

- Python 3.12+
- Selenium WebDriver
- Pytest
- Webdriver Manager (`webdriver-manager`)
- (опционально: `pytest-html`, `pytest-xdist`)

---

## 🚀 Как запустить проект

1. Установи зависимости:

```bash
pip install -r requirements.txt
```

2. Запусти тесты:

```bash
pytest tests/
```

---

## 🗂 Структура проекта

```
herokuapp-autotests/
├── tests/              # Тесты (test_*.py)
│   └── __init__.py
├── conftest.py         # Фикстуры pytest
├── requirements.txt    # Зависимости
├── .gitignore
├── README.md           # Этот файл
└── main.py             # Вспомогательные действия (если нужно)
```

---

## 🔄 Как работать с Git

```bash
git pull          # Забрать изменения
git add .
git commit -m "описание"
git push          # Отправить изменения
```

---

## 🤝 Контакт

Автор: Никита  
Проект создан в учебных целях ✌️
