from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {"status": "success", "message": "Backend API is running"}

@app.route('/health')
def health_check():
    return {"status": "healthy"}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
