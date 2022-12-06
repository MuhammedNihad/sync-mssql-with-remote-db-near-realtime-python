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

    try:
        # Execute query to fetch rows that are modified within 5 minutes ago
        cursor = conn.cursor().execute(f"SELECT name, code, price, stock FROM {config('TABLE_NAME')} WHERE modified_at > '{last_executed_time}'")
    except Exception as error:
        print(f"Failed to execute query. \n{error}")
    else:
        results = []

        """
        Converting query result as list of key value pairs which is the desired format for sending through API.
        Otherwise, looping through data in cursor will be in tuple without column name. eg: ('milk','M23',19.90,10)
        """
        # Fetch all columns in the query result
        columns = [column[0] for column in cursor.description]
        # Fetch all rows in the query result
        for row in cursor.fetchall():
            # Append all columns and rows as dict into results list.
            # eg: [{'name':'milk','code':'M23','price':19.90,'stock':10}]
            results.append(dict(zip(columns, row)))

        print(results)