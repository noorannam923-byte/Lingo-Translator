from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

try:
    from deep_translator import GoogleTranslator
except Exception:
    GoogleTranslator = None

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

app = Flask(__name__)
CORS(app)


def translate_via_gemini(api_key: str, text: str, source: str, target: str) -> str:
    # Use Google Generative Language API to translate via a prompt.
    endpoint = f"https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generate?key={api_key}"
    prompt = f"Translate the following text from {source} to {target}: \"{text}\""
    body = {
        "prompt": {"text": prompt},
        "temperature": 0.0,
        "maxOutputTokens": 1024
    }
    resp = requests.post(endpoint, json=body, timeout=15)
    resp.raise_for_status()
    j = resp.json()
    # Attempt to extract generated text
    candidates = j.get('candidates') or []
    if candidates:
        return candidates[0].get('content', '')
    # Some API versions return 'output' -> 'text'
    output = j.get('output')
    if isinstance(output, list) and output:
        return ''.join([o.get('content', '') for o in output if isinstance(o, dict)])
    return ''


def translate_text(text: str, source: str, target: str) -> str:
    # If GEMINI key provided, try using Gemini (Generative Language API)
    if GEMINI_API_KEY:
        try:
            res = translate_via_gemini(GEMINI_API_KEY, text, source or 'auto', target)
            if res:
                return res
        except Exception:
            # If Gemini fails, fall back to deep_translator
            pass

    # Fallback: use deep_translator.GoogleTranslator (no API key required)
    if GoogleTranslator:
        src = None if source in (None, '', 'auto') else source
        translator = GoogleTranslator(source=src or 'auto', target=target)
        return translator.translate(text)

    # Final fallback: return original text
    return text


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json() or {}
    text = data.get('text', '')
    source = data.get('source', 'auto')
    target = data.get('target', 'en')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        translated = translate_text(text, source, target)
        return jsonify({'translatedText': translated})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
