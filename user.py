from datetime import datetime
from flask import abort, make_response
import json


def get_timestamp():
    return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))


def read_all():
    from app import mysql
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM agenda_usuario;')
    rv = cur.fetchall()
    column_names = [i[0] for i in cur.description]
    rows = [dict(zip(column_names, row)) for row in rv]
    return rows


def create(user):
    usuario_id = user.get('usuario_id')
    usuario_nome = user.get('usuario_nome', '')
    usuario_email = user.get('usuario_email')
    usuario_senha = user.get('usuario_senha')
    usuario_status = 1

    from app import mysql
    cur = mysql.connection.cursor()
    cur.execute(f"INSERT INTO agenda_usuario(usuario_id, usuario_nome, usuario_email, usuario_senha, usuario_status) VALUES ('{usuario_id}', '{usuario_nome}', '{usuario_email}', '{usuario_senha}', '{usuario_status}')")
    mysql.connection.commit()
    cur.close()


def read_one(user_id):
    from app import mysql
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM agenda_usuario WHERE usuario_id='{user_id}';")
    rv = cur.fetchall()
    column_names = [i[0] for i in cur.description]
    rows = [dict(zip(column_names, row)) for row in rv]
    return rows[0]


def update(user_id, user):
    from app import mysql
    usuario_email = user.get('usuario_email')
    cur = mysql.connection.cursor()
    cur.execute(f"UPDATE agenda_usuario SET usuario_email='{usuario_email}' WHERE usuario_id={user_id};")
    mysql.connection.commit()
    cur.close()


def delete(user_id):
    from app import mysql
    cur = mysql.connection.cursor()
    cur.execute(f"DELETE FROM agenda_usuario WHERE usuario_id={user_id};")
    mysql.connection.commit()
    cur.close()


def read_all_events(user_id):
    from app import mysql
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM agenda_evento WHERE usuario_id='{user_id}';")
    rv = cur.fetchall()
    column_names = [i[0] for i in cur.description]
    rows = [dict(zip(column_names, row)) for row in rv]
    return rows