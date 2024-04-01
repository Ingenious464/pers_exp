# routes
@app.route('/dashboard')
def dashboard():
    # Fetch user data and display on the dashboard
    return render_template('dashboard.html')

@app.route('/set_budget', methods=['POST'])
def set_budget():
    # Handle form submission to set user's monthly budget
    return redirect('/dashboard')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    # Handle form submission to add an expense
    return redirect('/dashboard')

