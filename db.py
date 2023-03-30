from flask_mysqldb import MySQL
from app import app

mysql = MySQL(app.app)

def get_db_cursor():
    mysql = MySQL(app.app)
    return mysql.connection.cursor()