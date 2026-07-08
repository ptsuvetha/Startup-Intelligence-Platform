from app.databases.database import engine

try:
    connection = engine.connect()
    print("✅ Connected to MySQL successfully!")
    connection.close()
except Exception as e:
    print(e)