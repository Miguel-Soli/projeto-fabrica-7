import sqlite3 as sq

DB_PATH = 'albert_DADOS/hospital.db'

def get_conection():
    return sq.connect(DB_PATH)

def consultas_do_paciente(pacientes_id):
    with get_conection() as conn:
        cur = conn.cursor()
        cur.execute('''
            SELECT data, hora
            FROM consultas
            WHERE paciente_id = ?
            ORDER BY data, hora
        ''', (pacientes_id,))
        
        resultados = cur.fetchall()
        return resultados


cr = consultas_do_paciente(1)


for data, hora in cr:
    print(f"Consulta em {data} às {hora}")
