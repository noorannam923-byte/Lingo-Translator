import json
from app import app

client = app.test_client()

def run_test():
    payload = {
        'text': 'Hello, how are you?',
        'source': 'en',
        'target': 'es'
    }
    resp = client.post('/translate', data=json.dumps(payload), content_type='application/json')
    print('Status:', resp.status_code)
    print(resp.get_data(as_text=True))

if __name__ == '__main__':
    run_test()
