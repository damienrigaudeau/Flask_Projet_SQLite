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

@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/consultation/')
def ReadBDD():
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    return render_template('formulaire.html')

@app.route('/enregistrer_client', methods=['POST'])
def enregistrer_client():
    nom = request.form['nom']
    prenom = request.form['prenom']
    adresse = request.form.get('adresse', 'Adresse non renseignée')

    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)', (nom, prenom, adresse))
    conn.commit()
    conn.close()
    return redirect('/consultation/')

@app.route('/livres')
def afficher_livres():
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres')
    livres = cursor.fetchall()
    conn.close()
    return render_template('livres.html', livres=livres)

@app.route('/utilisateurs')
def afficher_utilisateurs():
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    utilisateurs = cursor.fetchall()
    conn.close()
    return render_template('utilisateurs.html', utilisateurs=utilisateurs)

@app.route('/emprunter/<int:livre_id>/<int:client_id>', methods=['POST'])
def emprunter_livre(livre_id, client_id):
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE livres SET disponible = ? WHERE id = ?', ('non', livre_id))
    cursor.execute('INSERT INTO emprunts (client_id, livre_id) VALUES (?, ?)', (client_id, livre_id))
    conn.commit()
    conn.close()
    return redirect(url_for('afficher_livres'))

@app.route('/retourner/<int:livre_id>', methods=['POST'])
def retourner_livre(livre_id):
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE livres SET disponible = ? WHERE id = ?', ('oui', livre_id))
    cursor.execute('UPDATE emprunts SET date_retour = CURRENT_TIMESTAMP WHERE livre_id = ? AND date_retour IS NULL', (livre_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('afficher_livres'))

if __name__ == "__main__":
  app.run(debug=True)
