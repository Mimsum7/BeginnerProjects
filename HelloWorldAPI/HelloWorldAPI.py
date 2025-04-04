from flask import Flask

app = Flask(__name__) # Creating a Flask application instance

@app.route("/") #is a decorator that tells Flask "Whenever someone visits the root URL /, run the function below."
def hello_world():    # defines a function that will be executed when the user accesses /.
    return {"message": "Hello, World!"}

if __name__ == "__main__": # ensures that the script runs only if it's executed directly (not imported as a module).
    app.run(debug=True) #enables debug mode
