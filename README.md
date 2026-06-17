# Fikra API Examples: Django Chatbot

Welcome to `fikra-examples`. This repository contains reference implementations and frontend code to help you build production-ready applications on top of the [Fikra API](https://fikraapi.co.ke).

Currently, this repository houses a minimal, drop-in **Django Chatbot** powered by Fikra API.

## 🌍 The Fikra Ecosystem

Depending on what you are trying to build, you might be looking for our other official repositories:

* [**fikra-python**](https://github.com/ronikisystems/fikra-python)**:** The official Python SDK for interacting with Fikra API. Use this if you are building backend applications in Python.


## ⚡ Don't want to write code? (5-Minute Deploy)

If you just need an AI chatbot for your business and don't want to host the code yourself, **you do not need this repository.**

Through our partnership with **Lacesse Pages**, you can instantly deploy a fully-hosted, custom AI agent in under 5 minutes directly from the Fikra Dashboard.

👉 [**Deploy a Hosted Bot on Fikra API**](https://fikraapi.co.ke/dashboard)

## 🛠️ Example 1: Django Chatbot Integration

A minimal Django app with a chat interface powered by Fikra API. You can drop it into an existing Django project or run it standalone. It uses a Vanilla JS frontend, meaning no complex Node.js build steps are required.

### Stack

* **Backend:** [Django](https://www.djangoproject.com/) 4.x+

* **AI Inference:** [Fikra API](https://fikraapi.co.ke) (OpenAI-compatible)

* **Frontend:** Vanilla JavaScript & HTML

### Local Setup

Clone this repository and run the following commands to start the standalone chatbot:

```bash
# Install required dependencies
pip install -r requirements.txt

# Export your Fikra API Key
export FIKRA_API_KEY=your_fikra_api_key

# Run database migrations and start the server
python manage.py migrate
python manage.py runserver

```
Open http://localhost:8000 in your browser to start chatting.

# Adding to an existing Django project

If you want to integrate this chatbot into an application you've already built:

    Copy the core files from this repository into a new chatbot/ app folder in your project.

    Add 'chatbot' to your INSTALLED_APPS list in settings.py.

    Route the URLs by adding path('chat/', include('chatbot.urls')) to your root urls.py.

    Ensure FIKRA_API_KEY is securely set in your environment variables.
