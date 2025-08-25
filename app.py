from flask import Flask, session, redirect, url_for, request, jsonify, flash, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
# from flask_bcrypt import Bcrypt
# from flask_session import Session
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'dif239JJ(#Rnfwoe0(WJ)!dj1-d1)'  # Required for session management and flash messages
# MongoDB Configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['bookstore']

# Index Page
@app.route('/')
def home():
    name = None
    # Safely check if 'email' is in session
    if session.get('email'):
        users_collection = db['users']
        user = users_collection.find_one({"email": session['email']})
        if user:  # Ensure user exists
            name = user['name']
    
    # Fetching the page number from the query parameters (default is page 1)
    page = int(request.args.get('page', 1))
    books_per_page = 16
    books_collection = db['books']
    
    # Calculate the number of books to skip for pagination
    skip_books = (page - 1) * books_per_page

    # Fetch the books for the current page using limit and skip
    books = list(books_collection.find().skip(skip_books).limit(books_per_page))
    
    # If there are not enough books in the database, repeat the list for display purposes (temporary solution)
    if books:
        # Repeat the book list 10 times for display (temporary fix for having few books)
        repeated_books = books * 10  
        books = repeated_books[:books_per_page]  # Only display the current page's worth of books
    
    # Get the total count of books to calculate the number of pages
    total_books = books_collection.count_documents({})
    total_pages = (total_books // books_per_page) + (1 if total_books % books_per_page != 0 else 0)
    
    return render_template('home.html', books=books, name=name, page=page, total_pages=total_pages)



@app.route('/book/<book_id>')
def book_detail(book_id):
    # Fetch a specific book by its ID
    books_collection = db['books']
    # Convert book_id to ObjectId if necessary
    try:
        book = books_collection.find_one({"_id": ObjectId(book_id)})
    except Exception as e:
        return f"Invalid book ID: {str(e)}", 400
    print(book)
    if not book:
        return "Book not found", 404
    return render_template('book_detail.html', book=book)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users_collection = db['users']
        # Query the MongoDB database for the user
        user = users_collection.find_one({"email": email})
        if user and user['password'] == password:
            # Set session data if login is successful
            session.permanent = True  # Make the session permanent
            session['user_id'] = str(user['_id'])
            session['email'] = user['email']
            flash('Login successful!', 'success')
            return redirect(url_for('home'))  # Redirect to home page or dashboard
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        users_collection = db['users']

        # Check if the email is already registered
        if users_collection.find_one({"email": email}):
            flash('Email is already registered. Please log in.', 'danger')
            return redirect(url_for('login'))

        # Insert the new user data into MongoDB
        users_collection.insert_one({
            "name": name,
            "email": email,
            "password": password
        })

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('sign_up.html')

@app.route('/logout')
def logout():
    session.clear()  # Clear the session data
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))  # Redirect to home page after logout

@app.route('/cart')
def cart():
    # Example of checking if a user is logged in
    if 'user_id' not in session:
        flash('Please log in to access your cart.', 'warning')
        return redirect(url_for('login'))
    # Fetch user's cart items from the database and render them
    return render_template('cart.html')  # Replace with your cart template

@app.route('/placed-order')
def placed_order():
    return render_template('in_progress.html')

@app.route('/about-us')
def about_us():
    return render_template('in_progress.html')


@app.route("/seller-registration")
def seller_registration():
    return render_template('in_progress.html')


@app.route("/Buy-Now")
def Buy_Now():
    return render_template("payment.html")


if __name__ == '__main__':
    app.run(debug=True)
