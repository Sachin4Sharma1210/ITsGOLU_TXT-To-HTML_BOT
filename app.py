from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from ➤ 𝕊𝔸ℂℍ𝕀ℕ 𝕊ℍ𝔸ℝ𝕄𝔸'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
