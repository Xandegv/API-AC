from flask import Flask, jsonify

app = Flask(__name__)

frutas = ['maca', 'banana', 'laranja', 'abacaxi']

@app.route('/frutas', methods=['GET'])
def get_frutas():
    return jsonify(frutas)

if __name__ == '__main__':
    app.run(port=5001)
