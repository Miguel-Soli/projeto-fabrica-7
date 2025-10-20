import sqlite3 as sq

DB_PATH = 'albert_DADOS/hospital.db'

def get_conection():
    return sq.connect(DB_PATH)

def consultas_do_medico(id_medico):
    with get_conection() as conn:
        cur = conn.cursor()
        cur.execute('''
            SELECT data, hora
            FROM consultas
            WHERE id_medico = ?
            ORDER BY data, hora
        ''', (id_medico,))
        
        resultados = cur.fetchall()
        return resultados


cr = consultas_do_medico(1)


for data, hora in cr:
    print(f"Consulta em {data} às {hora}")
