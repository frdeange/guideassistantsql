import os
import pyodbc

def ejecutar_consulta_sql(sql_query):
    server = os.getenv("SQLSERVER_HOST", "localhost")
    database = 'AsistenteDB'
    username = os.getenv("SQLSERVER_USER", "SA")
    password = os.getenv("SQLSERVER_PASSWORD", "TuPassword123")
    driver= '{ODBC Driver 17 for SQL Server}'
    port = os.getenv("SQLSERVER_PORT", "1433")

    connection_string = f'DRIVER={driver};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}'

    with pyodbc.connect(connection_string) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            resultados = [dict(zip(columns, row)) for row in rows]
    return resultados
