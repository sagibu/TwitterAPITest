from app import app
from flask import request
import json
from FrequentWordCalculator import FrequentWordCalculator

frequent_words = FrequentWordCalculator('settings/settings.json')

@app.route('/')
@app.route('/index')
def index():
    print("ABC")
    return "Hellao, World!"

@app.route('/monitor/<topic>', methods=['POST'])
def monitor(topic):
    frequent_words.monitor_topic(topic, 1800.0)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}