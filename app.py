from flask import Flask

TOKEN = '9148022055:AAGoqODy8B5DqwJ0VYLZ1keREhDAdCzlHZo'

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bot is running'

if __name__ == '__main__':
    app.run(debug=True)
    
