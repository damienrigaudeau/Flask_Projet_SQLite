import sqlite3

# Connexion à la base de données
connection = sqlite3.connect('bibliotheque.db')

# Création du schéma de la base de données
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insertion des livres avec disponibilité par défaut à 'oui'
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

# Sauvegarde et fermeture de la connexion
connection.commit()
connection.close()
