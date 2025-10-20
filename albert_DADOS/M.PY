import sqlite3 as sq 

DB_PATH = 'albert_DADOS/hospital.db'

def get_conection():
    return sq.connect(DB_PATH)

def criar_consulta():
    with get_conection() as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXSISTS consultas(
            cunsulta_id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_consulta_ TEXT NOT NULL,
            horario TEXT NOT NULL,
            status TEXT NOT NULL,
            paciente_id INTERGER PRIMARY KEY AUTOINCREMENT,
            id_medico INTEGER PRIMARY KEY AUTOINCREMENT
            );
        ''')
criar_consulta()