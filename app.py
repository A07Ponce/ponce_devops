from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
        <head>
            <title>Proyecto CI/CD - Alisson</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f1f1f1;
                    text-align: center;
                    padding-top: 100px;
                }
                .box {
                    background: white;
                    padding: 30px;
                    margin: auto;
                    width: 400px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #333;
                }
                p {
                    color: #555;
                }
            </style>
        </head>
        <body>
            <div class="box">
                <h1>Hola, soy Alisson</h1>
                <p>Este es mi proyecto Flask para el examen de CI/CD.</p>
                <p>Versión 3.0.0</p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
