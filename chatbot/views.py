import os
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from openai import OpenAI

# Initialize client. Fikra API is fully OpenAI-compatible.
# It pulls the key from the environment variable as per your README.
client = OpenAI(
    base_url="https://api.fikraapi.co.ke/v1",
    api_key=os.environ.get("FIKRA_API_KEY", "missing_key")
)

@ensure_csrf_cookie
def chat_page(request):
    """Renders the chat interface and initializes session memory."""
    # Ensure Django session exists
    if not request.session.session_key:
        request.session.save()
    
    # Initialize conversation history if it's a new session
    if 'chat_history' not in request.session:
        request.session['chat_history'] = [
            {"role": "system", "content": "You are a helpful AI assistant powered by Fikra API."}
        ]
    
    # Pass history to template so reloading the page doesn't clear the UI
    # We filter out the system prompt so it doesn't show in the chat bubbles
    display_history = [msg for msg in request.session['chat_history'] if msg['role'] != 'system']
    
    return render(request, 'chatbot.html', {'history': display_history})

def chat_send(request):
    """Receives user message, calls Fikra API, and updates session history."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
            
            if not user_message:
                return JsonResponse({'error': 'Message cannot be empty'}, status=400)

            # Retrieve memory and append new message
            history = request.session.get('chat_history', [])
            history.append({"role": "user", "content": user_message})

            # Call Fikra API
            response = client.chat.completions.create(
                model="fikra-fast-8b",
                messages=history
            )

            # Extract response and append to memory
            ai_message = response.choices[0].message.content
            history.append({"role": "assistant", "content": ai_message})
            
            # Save the updated memory back to the Django session
            request.session['chat_history'] = history
            request.session.modified = True

            return JsonResponse({'message': ai_message})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def chat_clear(request):
    """Wipes the conversation memory from the session."""
    if request.method == 'POST':
        request.session['chat_history'] = [
            {"role": "system", "content": "You are a helpful AI assistant powered by Fikra API."}
        ]
        request.session.modified = True
        return JsonResponse({'status': 'cleared'})
    return JsonResponse({'error': 'Invalid request method'}, status=405)
