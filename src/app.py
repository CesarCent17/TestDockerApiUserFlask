from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/nombres')
def nombres():
    lista_nombres = ['Juan', 'María', 'Pedro', 'Ana']
    return jsonify(lista_nombres)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
