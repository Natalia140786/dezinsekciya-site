import psycopg2
import os

# Данные суперпользователя (postgres)
conn = psycopg2.connect(
    dbname='dezinsect',
    user='postgres',
    password='SuperDezinsect2026',  # замените на ваш пароль суперпользователя
    host='amvera-tekhinanaty-1407-cnpg-dezinsect-d-rw',
    port='5432'
)
conn.autocommit = True
cur = conn.cursor()

# Выдаём права пользователю djangouser
cur.execute("GRANT ALL PRIVILEGES ON DATABASE dezinsect TO djangouser;")
cur.execute("GRANT ALL ON SCHEMA public TO djangouser;")
cur.execute("ALTER SCHEMA public OWNER TO djangouser;")

cur.close()
conn.close()
print("Права успешно выданы!")