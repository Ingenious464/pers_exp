from flask import Flask
from routes import register_routes
from model import create_database

app = Flask(__name__)
app.secret_key = 'd0e60654c3e7d9a6469f62ede323cfcf' 

# Register routes
register_routes(app)

if __name__ == '__main__':
    create_database()  # Create the database and tables
    app.run(debug=True)
