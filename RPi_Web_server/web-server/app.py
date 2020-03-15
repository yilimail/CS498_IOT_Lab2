
from flask import Flask, render_template, request
import json
import sqlite3

app = Flask(__name__)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



@app.route("/")
def main():
   # connects to SQLite database. File is named "sensordata.db" without the quotes
   # WARNING: your database file should be in the same directory of the app.py file or have the correct path
   conn=sqlite3.connect('sensordata.db')
   conn.row_factory = dict_factory
   c=conn.cursor()
   c.execute("SELECT * FROM airqua ORDER BY currenttime DESC LIMIT 1")
   readings = c.fetchall()

   return render_template('main.html', readings = readings)
   #return render_template('main.html', readings=readings)

   #return render_template('main.html', readings=readings)
   #return render_template('main.html', readings, readings1)


if __name__ == "__main__":
   app.run(host='192.168.1.34', port=8181, debug=True)