import sqlite3

#connexion a la base de donnée
conn= sqlite3.connect('bibliotheque.db')
curser=conn.cursor()

curser.execute('''CREATE TABLE IF NOT EXISTS LIVRE(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titre TEXT,
               auteur TEXT,
               isbn TEXT,
               disponible BOOLEAN,
               date_emprunt TEXT,
               date_retour TEXT,)''')