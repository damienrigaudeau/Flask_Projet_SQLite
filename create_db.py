import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUPONT', 'Emilie', '123, Rue des Lilas, 75001 Paris'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('TREMBLAY', 'Antoine', '1010, Boulevard de la Mer, 13008 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LAMBERT', 'Sarah', '222, Avenue de la Liberté, 59000 Lille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('GAGNON', 'Nicolas', '456, Boulevard des Cerisiers, 69003 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUBOIS', 'Charlotte', '789, Rue des Roses, 13005 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))


cur.execute("INSERT INTO livres (titre, auteur, genre, disponible) VALUES (?, ?, ?, ?)",
            ('Le Petit Prince', 'Antoine de Saint-Exupéry', 'Conte philosophique', 'oui'))

cur.execute("INSERT INTO livres (titre, auteur, genre, disponible) VALUES (?, ?, ?, ?)",
            ('Les Misérables', 'Victor Hugo', 'Roman historique', 'oui'))

cur.execute("INSERT INTO livres (titre, auteur, genre, disponible) VALUES (?, ?, ?, ?)",
            ('1984', 'George Orwell', 'Science-fiction', 'oui'))

cur.execute("INSERT INTO livres (titre, auteur, genre, disponible) VALUES (?, ?, ?, ?)",
            ('Harry Potter à l\'école des sorciers', 'J.K. Rowling', 'Fantasy', 'oui'))

cur.execute("INSERT INTO livres (titre, auteur, genre, disponible) VALUES (?, ?, ?, ?)",
            ('L\'Étranger', 'Albert Camus', 'Roman', 'oui'))

cur.execute("INSERT INTO livres (titre, auteur, genre, disponible) VALUES (?, ?, ?, ?)",
            ('Voyage au bout de la nuit', 'Louis-Ferdinand Céline', 'Roman', 'oui'))


connection.commit()
connection.close()
