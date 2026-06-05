# Django Chatbot - Fikra API

A minimal Django app with a chat interface powered by [Fikra API](https://fikraapi.co.ke). Drop it into an existing Django project or run it standalone.

---

## Stack

- [Django](https://www.djangoproject.com/) 4.x+
- [Fikra API](https://fikraapi.co.ke) - AI inference (OpenAI-compatible)
- [Fikra Python Repo](https://github.com/ronikisystems/fikra-python)
- Vanilla JS frontend - no build step required

---

## Setup

```bash
pip install -r requirements.txt
export FIKRA_API_KEY=your_fikra_api_key

python manage.py migrate
python manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000).

---

## Adding to an existing Django project

1. Copy the `chatbot/` app folder into your project
2. Add `'chatbot'` to `INSTALLED_APPS` in `settings.py`
3. Add `path('chat/', include('chatbot.urls'))` to your root `urls.py`
4. Set `FIKRA_API_KEY` in your environment or `settings.py`

---

## How it works

- The frontend sends POST requests to `/chat/send/` with the user message
- Django calls Fikra API and returns the response as JSON
- Conversation history is stored in the Django session

---

Get your Fikra API key at [fikraapi.co.ke](https://fikraapi.co.ke/account/signup).
