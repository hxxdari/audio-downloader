from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Audio Downloader!"

if __name__ == "__main__":
    app.run()