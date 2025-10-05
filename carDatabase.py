# THIS IS NOT FINISHED YET
"""
import csv, sqlite3

con = sqlite3.connect("carDatabase.db") 
cur = con.cursor()
cur.execute("CREATE TABLE t (make, model, production_date, colour, location);")

with open('static/cars.csv','r') as fin: 
    dr = csv.DictReader(fin) 
    to_db = [(i['col1'], i['col2']) for i in dr]

cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
con.commit()
con.close()
"""