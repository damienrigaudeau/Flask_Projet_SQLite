from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)                                                                                                                  
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Vérification de l'authentification
def est_authentifie():
    return session.get('authentifie')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/lecture')
def lecture():
    if not est_authentifie():
        return redirect(url_for('authentification'))
    return "<h2>Bravo, vous êtes authentifié</h2>"

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['authentifie'] = True
            return redirect(url_for('lecture'))
        else:
            return render_template('formulaire_authentification.html', error=True)
    return render_template('formulaire_authentification.html', error=False)

@app.route('/consultation_livres')
def consultation_livres():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres;')
    livres = cursor.fetchall()
    conn.close()
    return render_template('liste_livres.html', livres=livres)

@app.route('/ajouter_livre', methods=['GET', 'POST'])
def ajouter_livre():
    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        genre = request.form['genre']
        disponible = request.form.get('disponible', 'oui')

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO livres (titre, auteur, genre, disponible) VALUES (?, ?, ?, ?)', (titre, auteur, genre, disponible))
        conn.commit()
        conn.close()
        return redirect('/consultation_livres')
    return render_template('formulaire_livre.html')

@app.route('/supprimer_livre/<int:id>', methods=['POST'])
def supprimer_livre(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM livres WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/consultation_livres')

@app.route('/recherche_livres')
def recherche_livres():
    query = request.args.get('query', '')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres WHERE disponible = "oui" AND titre LIKE ?', ('%' + query + '%',))
    livres = cursor.fetchall()
    conn.close()
    return render_template('liste_livres.html', livres=livres)

@app.route('/emprunter_livre', methods=['POST'])
def emprunter_livre():
    client_id = request.form['client_id']
    livre_id = request.form['livre_id']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO emprunts (client_id, livre_id) VALUES (?, ?)', (client_id, livre_id))
    cursor.execute('UPDATE livres SET disponible = "non" WHERE id = ?', (livre_id,))
    conn.commit()
    conn.close()
    return redirect('/consultation_livres')

@app.route('/retourner_livre', methods=['POST'])
def retourner_livre():
    livre_id = request.form['livre_id']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE emprunts SET date_retour = CURRENT_TIMESTAMP WHERE livre_id = ? AND date_retour IS NULL', (livre_id,))
    cursor.execute('UPDATE livres SET disponible = "oui" WHERE id = ?', (livre_id,))
    conn.commit()
    conn.close()
    return redirect('/consultation_livres')

if __name__ == "__main__":
  app.run(debug=True)
