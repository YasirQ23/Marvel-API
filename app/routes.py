from app import app

@app.route('/')
def home():
    greeting = 'Hello, World'
    print(greeting)
    return 'Hello, World'