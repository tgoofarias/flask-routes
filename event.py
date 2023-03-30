from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))


def read_all():
    from app import mysql
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM agenda_evento;')
    rv = cur.fetchall()
    column_names = [i[0] for i in cur.description]
    rows = [dict(zip(column_names, row)) for row in rv]
    return rows


def create(event):
    from app import mysql
    evento_id = event.get('evento_id')
    evento_data_hora = event.get('evento_data_hora')
    evento_descricao = event.get('evento_descricao')
    evento_nome = event.get('evento_nome')
    evento_status = event.get('evento_status')
    usuario_id = event.get('usuario_id')
    cur = mysql.connection.cursor()
    cur.execute(f"INSERT INTO agenda_evento(evento_id, evento_data_hora, evento_descricao, evento_nome, evento_status, usuario_id) VALUES ('{evento_id}', '{evento_data_hora}', '{evento_descricao}', '{evento_nome}', '{evento_status}', '{usuario_id}');")
    mysql.connection.commit()
    cur.close()


def read_one(event_id):
    try:
        from app import mysql
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM agenda_evento WHERE evento_id='{event_id}';")
        rv = cur.fetchall()
        column_names = [i[0] for i in cur.description]
        rows = [dict(zip(column_names, row)) for row in rv]
        return rows[0]
    except:
        abort(404, f'Event not found')


def update(event_id, event):
    try:
        from app import mysql
        evento_nome = event.get('evento_nome')
        cur = mysql.connection.cursor()
        cur.execute(f"UPDATE agenda_evento SET evento_nome='{evento_nome}' WHERE evento_id='{event_id}';")
        mysql.connection.commit()
        cur.close()
    except:
        abort(404, f'Event not found')


def delete(event_id):
    try:
        from app import mysql
        cur = mysql.connection.cursor()
        cur.execute(f"DELETE FROM agenda_evento WHERE evento_id='{event_id}';")
        mysql.connection.commit()
        cur.close()
    except:
        abort(404, f'Event not found')