from decouple import config
import pyodbc


try:
    # Connect MSSQL database server
    conn = pyodbc.connect(
        "Driver={" + config("DRIVER") + "};"
        "Server=" + config("SERVER_NAME") + ";"
        "Database=" + config("DATABASE_NAME") + ";"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
except Exception as error:
    print(f"Connection failed. \n{error}")
else:
    cursor = conn.cursor().execute(f"SELECT * FROM {config('TABLE_NAME')}")
    for data in cursor:
        print(data)