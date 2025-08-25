# 📚 Online Library Management System

An **Online Library Web Application** built with **Flask** and **MongoDB**.
This project allows users to **sign up, log in, browse books with pagination, view book details, and manage their session**.
It also includes placeholder pages for future features like **Cart, Orders, Seller Registration, and Payment**.

---

## 🚀 Features

* 🏠 **Home Page** with book listings and pagination
* 📖 **Book Details Page** – view more information about a book
* 🔑 **User Authentication** – register, login, and logout
* 🛒 **Cart (WIP)** – secure cart page accessible only to logged-in users
* 📦 **Orders & Checkout (WIP)** – placeholder for placed orders
* 🏬 **Seller Registration (WIP)** – placeholder page
* 💳 **Buy Now (Payment Page)** – template for future payment integration
* 📄 **About Us Page (WIP)**

---

## 🛠️ Tech Stack

* **Backend:** [Flask](https://flask.palletsprojects.com/) (Python)
* **Database:** [MongoDB](https://www.mongodb.com/)
* **Frontend:** HTML, CSS, Bootstrap (via templates)
* **Session Management:** Flask Sessions
* **Flash Messages:** For user feedback (login/signup/etc.)

---

## 📂 Project Structure

```
Online_Library/
│
├── app.py                # Main Flask application
├── templates/            
│   ├── home.html
│   ├── book_detail.html
│   ├── login.html
│   ├── sign_up.html
│   ├── cart.html
│   ├── payment.html
│   └── in_progress.html
└── static/               # (Optional) CSS, JS, images
```

---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Vishal-Solanki-18/Online_Library.git
cd Online_Library
```

### 2. Create & Activate a Virtual Environment

```bash
# On Windows
python -m venv BookStoreENV
BookStoreENV\Scripts\activate

# On macOS/Linux
python3 -m venv BookStoreENV
source BookStoreENV/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask pymongo flask-bcrypt
```

### 4. Setup MongoDB

* Make sure **MongoDB** is installed and running locally on default port (`27017`).
* Create a database named `bookstore`.
* Add collections:

  * `users` → to store user info (name, email, password)
  * `books` → to store book details

Example `books` document:

```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "price": 299,
  "description": "A classic novel set in the Jazz Age."
}
```

### 5. Run the Application

```bash
python app.py
```

App will be available at:
👉 `http://127.0.0.1:5000/`

---

## 🔐 Security Notes

* Passwords should be **hashed** using `Flask-Bcrypt` (currently plain text in demo).
* Replace the hardcoded `secret_key` in `app.py` with an **environment variable**.

---

## 🛣️ Roadmap

* ✅ Authentication (Login / Signup / Logout)
* ✅ Book Listing with Pagination
* ⏳ Cart Management
* ⏳ Orders & Checkout
* ⏳ Seller Registration
* ⏳ Payment Gateway Integration
* ⏳ Admin Dashboard for Book Management

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch (`feature-new-thing`)
3. Commit changes
4. Push & open a Pull Request

---