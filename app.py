from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Define a route and corresponding function
@app.route('/')
def hello():
    return 'Hello, Flask!'

# Run the application
if __name__ == '__main__':
    app.run()
