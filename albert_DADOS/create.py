import sqlite3 as sq

DB_PATH = 'albert_DADOS/hospital.db'

def get_conection():
    return sq.connect(DB_PATH)

def criar_pc():
    with get_conection() as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            paciente_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            sexo TEXT NOT NULL,
            telefone TEXT
        );
        ''')
criar_pc()

def criar_medico():
    with get_conection() as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS medicos (
            id_medico INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especialidade TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL
        );
        ''')
criar_medico()

def criar_consulta():
    with get_conection() as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS consultas (
            consulta_id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_consulta TEXT NOT NULL,
            horario TEXT NOT NULL,
            status TEXT NOT NULL,
            paciente_id INTEGER NOT NULL,
            id_medico INTEGER NOT NULL,
            FOREIGN KEY (paciente_id) REFERENCES pacientes (paciente_id),
            FOREIGN KEY (id_medico) REFERENCES medicos (id_medico)
        );
        ''')
criar_consulta()
