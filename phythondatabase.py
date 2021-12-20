"""
    Create Virtual environment $ python -m venv env
    Activate virtual environment $ source ".\env\Scripts\activate"
    Install python packages $ pip install -r requirements.txt
    Update packages $ pip freeze > requirements.txt

"""

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root"
)
