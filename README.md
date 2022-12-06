# Sync MSSQL database with remote database in near-realtime using Python


## Dependencies

ODBC Driver for SQL Server is required to run this project. [Download driver](https://learn.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver15)



## Run Locally

Clone the project and navigate to the project directory:

```bash
git clone https://github.com/MuhammedNihad/sync-mssql-with-remote-db-near-realtime-python && cd sync-mssql-with-remote-db-near-realtime-python
```
Create .env file. Set environment variable by referring `.env.example` file.
```
cp .env.example .env
```

Install python dependencies:

```bash
pip install -r requirements.txt
```

Run project:

```bash
python script.py
```

