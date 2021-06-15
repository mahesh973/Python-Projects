# Flask-Notes-App Tutorial
### This is a simple Notes Application in which you can create and delete notes from time to time.
### This website includes all the login,logout and SignUp functionalities and notes will be stored in a Database.
### Website preview can be seen at the bottom of this page
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
# Your Home Page appears in this way
![login_page](https://user-images.githubusercontent.com/59694546/122037005-cc19fe00-cdf1-11eb-9667-73e18332cc6a.png)
# Your SignUp page appears in this way
![Sign_Up_Page](https://user-images.githubusercontent.com/59694546/122037344-1bf8c500-cdf2-11eb-8e23-1b4b373cda0f.png)
# Your Notes Page appears in this way
![Notes_page](https://user-images.githubusercontent.com/59694546/122037469-3b8fed80-cdf2-11eb-8147-d519fa51b8b4.png)


    
