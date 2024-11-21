from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Lucas aqui, professor! Suas aulas foram muito boas."})

if __name__ == "__main__":
    app.run(debug=True)
