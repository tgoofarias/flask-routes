from flask import render_template
from flask_mysqldb import MySQL
import connexion

app = connexion.App(__name__, specification_dir='./')
app.app.config['MYSQL_HOST'] = 'localhost'
app.app.config['MYSQL_PORT'] = 3306
app.app.config['MYSQL_USER'] = 'mps'
app.app.config['MYSQL_PASSWORD'] = '123456'
app.app.config['MYSQL_DB'] = 'mydb'
app.add_api('swagger.yml')
mysql = MySQL(app.app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM agenda_usuario;')
    rv = cur.fetchall()
    return str(rv)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)