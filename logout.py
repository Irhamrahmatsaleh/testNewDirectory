from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ganti dengan secret key yang aman

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Hapus session user
    return redirect(url_for('login'))  # Arahkan kembali ke halaman login

@app.route('/login')
def login():
    return "Halaman Login"  # Ganti dengan halaman login yang sesuai

if __name__ == '__main__':
    app.run(debug=True)
