from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/api/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
