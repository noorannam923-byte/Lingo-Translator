# LINGO TRANSLATOR

The Lingo Translator is a language translation tool designed to break communication barriers by enabling seamless conversion of text between multiple languages.

<img width="700" height="500" alt="{6E7F6819-E3D4-4444-A811-F5487B3B3ADC}" src="https://github.com/user-attachments/assets/ee8e642e-0c6d-4e25-93c0-1df58bdfbe2d" />


Quickstart (Windows):

```powershell
python -m venv venv
venv\Scripts\python -m pip install --upgrade pip
venv\Scripts\python -m pip install -r requirements.txt

set FLASK_APP=app.py
venv\Scripts\python -m flask run
```

Open http://127.0.0.1:5000 in your browser.

Notes:
- If you have a paid Translate API (Google Cloud / Microsoft / Gemini) you can adapt `app.py` to call that API instead. The current implementation uses `deep-translator` which works without an API key for many languages.
