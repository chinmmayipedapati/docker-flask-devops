
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Chinmmayi DevOps Project</title>
        </head>
        <body style="font-family: Arial; text-align: center;
                     padding: 80px; background: #eef2ff;">
            <h1>Welcome to My DevOps Project!</h1>
            <h2>Docker + Python + Flask</h2>
            <p>My first containerized application is running.</p>
            <p>Developed by Chinmmayi Pedapati</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)