from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []

@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    expense = request.form.get('expense')
    expenses.append(expense)
    return redirect('/')

@app.route('/delete_expense/<int:index>', methods=['POST'])
def delete_expense(index):
    del expenses[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
