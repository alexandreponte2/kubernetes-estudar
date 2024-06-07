from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello():
    return 'Hello, World GOKU!'

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
