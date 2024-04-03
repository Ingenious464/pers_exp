from flask import render_template, request, redirect, session
from flask import Flask

import sqlite3

# Function to register routes
def register_routes(app: Flask):
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            with sqlite3.connect('expenses.db') as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
                conn.commit()
            return redirect('/login')
        return render_template('register.html')

    # Function to get user ID from session
    def get_user_id():
        return session.get('user_id')

    # Function to get username from session
    def get_username():
        return session.get('username')

    # Route to log in
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            with sqlite3.connect('expenses.db') as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
                user = cursor.fetchone()
                if user:
                    session['user_id'] = user[0]
                    session['username'] = user[1]
                    return redirect('/')
                else:
                    return 'Invalid username or password'
        return render_template('login.html')

    # Route to log out
    @app.route('/logout')
    def logout():
        session.pop('user_id', None)
        session.pop('username', None)
        return redirect('/')

    # Route to display expenses
    @app.route('/')
    def index():
        user_id = get_user_id()
        if user_id:
            with sqlite3.connect('expenses.db') as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM expenses WHERE user_id = ?', (user_id,))
                expenses = cursor.fetchall()
            return render_template('index.html', expenses=expenses)
        return redirect('/login')

    # Route to add an expense
    @app.route('/add_expense', methods=['POST'])
    def add_expense():
        user_id = get_user_id()
        if user_id:
            category = request.form['category']
            amount = float(request.form['amount'])
            date = request.form['date']
            with sqlite3.connect('expenses.db') as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO expenses (user_id, category, amount, date) VALUES (?, ?, ?, ?)', (user_id, category, amount, date))
                conn.commit()
        return redirect('/')

    # Route to delete an expense
    @app.route('/delete_expense/<int:expense_id>', methods=['POST'])
    def delete_expense(expense_id):
        user_id = get_user_id()
        if user_id:
            with sqlite3.connect('expenses.db') as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM expenses WHERE id = ? AND user_id = ?', (expense_id, user_id))
                conn.commit()
        return redirect('/')
