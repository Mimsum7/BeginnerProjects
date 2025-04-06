# -*- coding: utf-8 -*-  # Declare UTF-8 encoding at the top of the file

from flask import Flask, jsonify, render_template  # Flask is for creating the web app, jsonify is for returning JSON responses, and render_template is for rendering HTML templates
import random  # random is used to choose a random quote from the list

app = Flask(__name__)  # Create a Flask app instance

# List of quotes to choose from in an array
quotes = [
    "You miss 100% of the shots you don't take.",  # Fixed curly apostrophe
    "Whether you think you can or you think you can't, you're right.",  # Fixed curly apostrophes
    "Hard work beats talent when talent doesn't work hard.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "It does not matter how slowly you go as long as you do not stop.",  # Fixed missing comma
    "The only way to do great work is to love what you do.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Dont watch the clock; do what it does. Keep going.",  # Fixed curly apostrophe
    "The way to get started is to quit talking and begin doing."
]

@app.route('/')  # Define the home route
def index():
    return render_template("index.html")  # Flask will look in the templates folder and load index.html

@app.route('/quote')  # Define the quote route
def get_quote():
    return jsonify({'quote': random.choice(quotes)})  # Return a random quote as a JSON response

# This block ensures the script runs only if executed directly (not imported as a module)
if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Run the app in debug mode
