
#Create Database and table

import sqlite3

conn=sqlite3.connect('file_database.db')

with conn:
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS file_database(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                File_List TEXT \
                )")
    conn.commit()
# Insert Data
conn = sqlite3.connect("file_database.db")
with conn:
    cur = conn.cursor()
    # Use executemany to insert multiple rows
    cur.executemany("INSERT INTO file_database(File_List) VALUES (?)",
                    [('information.docx',),
                     ('Hello.txt',),
                     ('myImage.png',),
                     ('myMovie.mpg',),
                     ('World.txt',),
                     ('data.pdf',),
                     ('myPhoto.jpg',)])
    conn.commit()
conn.close()

#Query for files ending with .txt

conn=sqlite3.connect("file_database.db")


with conn:
    cur=conn.cursor()
    cur.execute('SELECT File_List FROM file_database WHERE File_List LIKE "%.txt"')
    rows=cur.fetchall()
    for row in rows:
        print(row)
