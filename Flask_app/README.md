# Flask-Notes-App Tutorial
## Setup and Installation

### 1. Install virtual environment wrapper (pip install virtualenvwrapper-win)
    pip install virtualenvwrapper-win
    
### 2. Create a virtual environment
     mkvirtualenv (envname)
     
### 3. Setup the folder structure(in the similar manner)
        |--- Flask_Website
             |-- templates
                 |-- base.html
                 |-- home.html
                 |-- login.html
                 |-- sign_up.html
             |-- __init__.py
             |-- auth.py
             |-- database.db
             |-- models.py
             |-- views.py
           
        |-- main.py
        |-- requirements.txt
             
### 4. Run using the following command
      python main.py
    
# View the website in the browser by typing the following address
       https://127.0.0.1:5000
# Login Page
![Login Page Image](/Flask_Website/login_page.png?raw=true "Login Page")
    
