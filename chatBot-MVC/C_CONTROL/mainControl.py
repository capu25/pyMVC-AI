from flask import Flask, render_template, request
from C_CONTROL.chatControl import askQuestion

app = Flask(__name__, template_folder=('../V_VIEW'))

messaggi = []

@app.route('/')
def index():
    return render_template('chatView.html', messaggi = messaggi)

@app.route('/rispondi', methods=['POST'])
def risposta():
    if request.method == 'POST':
        user_input = request.form['user_input']
        ris = askQuestion(user_input)
        messaggi.append({'role': 'Utente', 'content': user_input})
        messaggi.append({'role':'Sistema', 'content':ris})
        return render_template('chatView.html', messaggi=messaggi)

if __name__ == '__main__':
    app.run(debug=True)
