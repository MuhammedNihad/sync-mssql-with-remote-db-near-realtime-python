from datetime import datetime, timedelta
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
    # Assign 5 minutes ago explicitly as last executed time
    five_minutes_ago = datetime.now() - timedelta(minutes=5)
    # Strip last 3 string by converting to isoformat for matching time string with db time string
    last_executed_time = five_minutes_ago.isoformat(timespec='milliseconds')

    cursor = conn.cursor().execute(f"SELECT name, code, price, stock FROM {config('TABLE_NAME')} WHERE modified_at > '{last_executed_time}'")
    for data in cursor:
        print(data)