# Language Translator (Flask)

Simple translator UI (Flask backend) that uses `deep-translator`'s `GoogleTranslator` by default.

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
