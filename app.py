from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense_tracker.db'
db = SQLAlchemy(app)

@app.route('/about', methods=['GET'])
def about():
    data = {
        "name": "Adetunji Fatai B",
        "gender": "Male",
        "github_url": "https://github.com/Ingenious464",
        "framework": "Flask",
        "location": "Nigeria"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)