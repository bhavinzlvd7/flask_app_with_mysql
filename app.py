import os
from flask import Flask
from flaskext.mysql import MySQL      # For newer versions of flask-mysql 
# from flask.ext.mysql import MySQL   # For older versions of flask-mysql
from mysql_config import app_config

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config.update(app_config)
mysql.init_app(app)

print(app.config)

conn = mysql.connect()

cursor = conn.cursor()

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/read from database')
def read():
    cursor.execute("SELECT * FROM employees")
    row = cursor.fetchone()
    result = []
    while row is not None:
      result.append(row[0])
      row = cursor.fetchone()

    return ",".join(result)

if __name__ == "__main__":
    app.run()
