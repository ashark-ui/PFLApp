
# NFL Pick'em Pool Web App

A lightweight web application for managing an NFL Pick'em pool, built using Flask and SQLAlchemy, and deployed on PythonAnywhere.

## 🏈 Project Overview
This app allows users to:
- Register and log in
- Submit weekly NFL picks
- View their picks and standings
- Admin dashboard to manage users and results

## 🚀 Features
- User authentication
- Weekly pick submission form
- SQLite database integration
- Responsive HTML templates
- Admin dashboard for scoring

## 🛠 Tech Stack
- Python
- Flask
- SQLAlchemy
- HTML/CSS
- SQLite
- PythonAnywhere (for deployment)

## ⚙️ Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nfl-pickem.git
   cd nfl-pickem
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```python
   from app import app, db
   with app.app_context():
       db.create_all()
   ```
5. Run the app locally:
   ```bash
   flask run
   ```

## 📦 Deployment on PythonAnywhere
1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com/)
2. Upload your project files
3. Set up a new web app using Flask
4. Configure the WSGI file to point to `app.py`
5. Install dependencies in the Bash console:
   ```bash
   pip install --user -r requirements.txt
   ```
6. Reload your web app from the Web tab

## 📄 License
This project is licensed under the MIT License.
